#!/usr/local/bin/env python -W ignore::DeprecationWarning
# !/usr/local/bin/env python
__author__ = "Blaka"

import importlib
import __builtin__
# import os, sys
from prettytable import PrettyTable
from time import sleep
import num_list_newlist as nl
# import threading
import platform

'''to do:
		implement argv later so can use with command line for ease
		(DONE)add the script so that mod_list is always up to date
		more columns for the pretty table
		implement so can use name or number
'''
'''
dictionary = {1:"hello", 2: "blaka"}

for func in dir(dictionary):
	print func
'''
# use this ^^^^ as inspiration for expanding the modules functions

'''ui = threading.Thread(target=nl.printing)
ui.start()
ui.join()
'''
# open the newly created module list
platform = platform.uname()
global path_mod
if platform[1] == "MacBookPro":
	macbook = open("/Users/blaka/Documents/python/liblist/temp/mod_list.txt", "r")
	path_mod = macbook.readlines()
	macbook.close()  # just some housekeeping
elif platform[1] == "MacMini":
	macmini = open("/Users/blaka7/Documents/python/liblist/temp/mod_list.txt", "r")
	path_mod = macmini.readlines()
	macmini.close()  # just some housekeeping
else:
	print "this version is only for " + __author__

num_list = []  # put half into here
num_list_p2 = []  # and the other half in here for other half of table
path_list = []
path_list_p2 = []  # same goes for the numbers that associate with them
path_len = len(path_mod)  # count the number of modules

if path_len % 2 == 0:  # checks if number of modules is even
	path_len_p1 = path_len / 2
	path_len_p2 = path_len / 2
else:  # if not adds 1 to the first table
	path_len_p1 = (path_len / 2) + 1
	path_len_p2 = path_len / 2

for num in range(0, path_len):
	num_list.append(str(num))

for p in path_mod:
	path_list.append(p)

mod_dict = dict(zip(num_list, path_list))




def library_list():
	global lib
	print "--------------------------------------------------"
	print "Here are the available library's:"
	print "--------------------------------------------------"
	table = PrettyTable(["Index", "Package"])  # initiate prettytable
	count = 0
	for mod in path_mod:  # adds numbers and modules to prettytable
		table.add_row(["%d" % count, "%s" % mod])
		count += 1
	print table
	print "--------------------------------------------------"
	ans = raw_input("what library would you like to look at?: ")
	print "--------------------------------------------------"
	try:
		lib = mod_dict[ans]  # check if input is in module dictionary
	except KeyError:
		print "Please choose a valid number associating to a library"
		sleep(3)  # ^ error checking for invalid input
		library_list()
	# print repr(lib)   - shows raw string literal
	lib = lib.replace("\n", "")
	# ^get rid of all newlines so only actual module name is checked
	print "You have chosen to look at %s" % lib
	print "--------------------------------------------------"
	sleep(1)
	try:
		global module
		module = __builtin__.__import__(lib) or importlib.import_module(lib)
	# try importing module
	except ImportError:
		print "Please choose a valid number associating to a library"
		# module not in library or mispelled/ out of range
		sleep(3)
		library_list()
	contents = dir(module)  # handle for the module contents
	for c in contents:
		print c  # iterate over contents of module showing whats inside


if __name__ == "__main__":
	nl.printing()  # just cosmetic
	nl.create_output()  # creates the module list
	nl.create_handle()  # just a handle for the contents of the list
	nl.delete_unused()  # trims any unwanted/unneeded modules from list
	nl.sort_list()  # sorts the list into alphabetical order
	repeat = ''  # holder for the user input
	while repeat != "no":
		library_list()
		print "--------------------------------------------------"
		print "would you like to look at another library?"
		print "--------------------------------------------------"
		repeat = raw_input(">(yes/no) ").lower()
