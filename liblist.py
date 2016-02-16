#! /usr/bin/env python -W ignore::DeprecationWarning
# -*- coding: utf-8 -*-

__author__ = "Blaka90"

import importlib
import __builtin__
import os
import sys
from prettytable import PrettyTable
from time import sleep
import liblist_newlist as nl
import collections
import threading
import platform
import inspect
import argparse
import warnings
import getpass


"""-----------------ONLY WORKING ON UNIX SO FAR----------------"""


warnings.filterwarnings("ignore", category=DeprecationWarning)


parser = argparse.ArgumentParser(description="Module for listing all modules available")
parser.add_argument("q", nargs="?", help="uses pre-existing library list for quickness", default="empty")
args = parser.parse_args()


# below was the old way, been optimized since, just keeping incase
ui = threading.Thread(target=nl.printing)
ui2 = threading.Thread(target=nl.printing_output)
# sc = threading.Thread(target=nl.start_create)


platform = platform.uname()
user = getpass.getuser()

# just the old way, will remove when i know new way is reliable on all systems
'''
# open the newly created module list
global path_mod
if platform[1] == "MacBookPro":
	macbook = open("/Users/" + user + "/Documents/python/liblist/temp/mod_list.txt", "r")
	path_mod = macbook.readlines()
	macbook.close()  # just some housekeeping
elif platform[1] == "MacMini":
	macmini = open("/Users/" + user + "/Documents/python/liblist/temp/mod_list.txt", "r")
	path_mod = macmini.readlines()
	macmini.close()  # just some housekeeping
else:
	print "this version is only for " + __author__
'''

# added since i am trying to make more universal
try:
	user_path = open("/Users/" + user + "/Documents/python/liblist/temp/mod_list.txt", "r")
except IOError as e:
	user_path = open("/Users/" + user + "/mod_list.txt", "r")
path_mod = user_path.readlines()
user_path.close()


num_list_p1 = []  # put half into here
num_list_p2 = []  # and the other half in here for other half of table
path_list_p1 = []
path_list_p2 = []  # same goes for the numbers that associate with them
path_len = len(path_mod)  # count the number of modules


def table_sort():
	global path_len_p1
	global path_len_p2
	if path_len % 2 == 0:  # checks if number of modules is even
		path_len_p1 = path_len / 2
		path_len_p2 = path_len / 2
	else:  # if not adds 1 to the first table
		path_len_p1 = (path_len / 2) + 1
		path_len_p2 = path_len / 2

	for num_p1 in range(0, path_len_p1):
		num_list_p1.append(str(num_p1))

	for num_p2 in range(path_len_p1, path_len):
		num_list_p2.append(str(num_p2))

	for p1 in path_mod[:path_len_p1]:
		path_list_p1.append(p1)

	for p2 in path_mod[path_len_p2:]:
		path_list_p2.append(p2)

	global mod_dict_p1
	global mod_dict_p2
	global mod_dict_p
	mod_dict_p = dict(zip((num_list_p1 + num_list_p2), (path_list_p1 + path_list_p2)))
	mod_dict_p1 = collections.OrderedDict(zip(num_list_p1, path_list_p1))
	mod_dict_p2 = collections.OrderedDict(zip(num_list_p2, path_list_p2))


def library_list():
	global lib
	global lib2
	global ans
	print "--------------------------------------------------"
	print "Here are the available library's:"
	print "--------------------------------------------------"
	table1 = PrettyTable(["Index", "Package", "index", "package"])  # initiate prettytable
	table1.sortby = "Index"

	for (key1,value1), (key2,value2) in zip(mod_dict_p1.iteritems(), mod_dict_p2.iteritems()):
		table1.add_row(["%s" % key1, "%s" % value1, "%s" % key2, "%s" % value2])

	table1.sortby = "Package"

	print table1
	print "--------------------------------------------------"
	ans = raw_input("what library would you like to look at?: ")
	print "--------------------------------------------------"
	if ans.isdigit():
		if ans in mod_dict_p1.keys():
			check_dict_1()
		elif ans in mod_dict_p2.keys():
			check_dict_2()
	elif ans == "x":
		exit(0)
	elif ans.isalpha() and ans.isdigit():
		check_word()
	elif ans.isalpha():
		check_word()
	else:
		print "not valid choice"


def check_dict_1():
		try:
			lib = mod_dict_p1[ans]  # check if input is in module dictionary
			lib = lib.replace("\n", "")
			# ^get rid of all newlines so only actual module name is checked
			print "You have chosen to look at %s" % lib
			print "--------------------------------------------------"
			sleep(1)
			check_import(lib)
		except KeyError:
			print "Please choose a valid number associating to a library"
			sleep(3)  # ^ error checking for invalid input
			library_list()


def check_dict_2():
		try:
			lib2 = mod_dict_p2[ans]
			lib2 = lib2.replace("\n", "")
			# ^get rid of all newlines so only actual module name is checked
			print "You have chosen to look at %s" % lib2
			print "--------------------------------------------------"
			sleep(1)
			check_import(lib2)
		except KeyError:
			print "Please choose a valid number associating to a library"
			sleep(3)  # ^ error checking for invalid input
			library_list()
			# print repr(lib)   - shows raw string literal


def check_word():
	lib3 = ans
	lib3 = lib3.replace("\n", "")
	# ^get rid of all newlines so only actual module name is checked
	print "You have chosen to look at %s" % lib3
	print "--------------------------------------------------"
	sleep(1)
	check_import(lib3)


def check_import(lib):
	try:
		global module
		module = __builtin__.__import__(lib) or importlib.import_module(lib)

	# try importing module
	except ImportError:
		print "Library does not exist: check your spelling or make sure library is installed"
		# module not in library or mispelled/ out of range
		sleep(4)
		library_list()
	print_output()


def print_output():
	global docs
	contents = dir(module)  # handle for the module contents
	for c in contents:  # iterate over contents of module showing whats inside
		print c

	print "--------------------------------------------------"
	print "Want more information on module contents?"
	print "--------------------------------------------------"
	try:
		expand = raw_input(">(y/n)").lower()
		print "\t"
		if expand == "y":
			for name,  mod in inspect.getmembers(module):
				if name == '__builtins__':
					continue
				elif name == "__doc__":
					docs = name + " : " + mod
					continue
				print '%s :' % name, mod
			print "\t"
			print docs
			print "\t"
			print "/\\" * 40
			print "\t"
		else:
			print "\t"
			print "/\\" * 40
			print "\t"
			pass
	except TypeError:
		print "\t"
		print "** __docs__ is unavailable with this package **"
		print "\t"
		sleep(3)

if __name__ == "__main__":
	repeat = ''  # holder for the user input
	if args.q == "q":
		table_sort()
		while repeat != "n":
			library_list()
			print "--------------------------------------------------"
			print "would you like to look at another library?"
			print "--------------------------------------------------"
			repeat = raw_input(">(y/n) ").lower()
		else:
			sys.exit(0)
	elif args.q == "empty":
		nl.start_create()
		print "-_-" * 26
		print " " * 35 + "LIBLIST"
		print "_-_" * 26 + "\n"
		ui.start()
		# sc.start()
		ui.join()
		ui2.start()
		# sc.join()
		ui2.join()
		table_sort()
		while repeat != "n":
			library_list()
			print "--------------------------------------------------"
			print "would you like to look at another library?"
			print "--------------------------------------------------"
			repeat = raw_input(">(y/n) ").lower()
		else:
			sys.exit(0)
	else:
		parser.print_help()
