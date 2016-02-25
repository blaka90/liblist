#!/usr/bin/env python -W ignore::DeprecationWarning
# -*- coding: utf-8 -*-

__author__ = 'Blaka90'

# simplified version of sending help() output to a file
import sys
import os
from time import sleep
from progressbar import *
import platform
import threading
import pydoc
import getpass


"""-----------------ONLY WORKING ON MAC OS X SO FAR----------------"""

'''
	tested on linux and got error- test on linux and windows for correct paths
	start making compatible with python3.5 as joining the dark side
	may need to look at create_output() see if works on windows
'''


# change into the desired working path
plat = platform.uname()
user = getpass.getuser()


# added since i am trying to make more universal
if os.path.isfile("/Users/" + user + "/Documents/python/liblist/temp/help_modules.txt"):
	os.chdir("/Users/" + user + "/Documents/python/liblist/temp/")  # just because its my script and
else:																# that's where it lives on my machine
	os.chdir(os.environ['HOME'])


make_file = "help_modules.txt"  # initial output file for the module list


# actually slows down the program but just wanted some visual appeal
widgets = ['Preparing files: ', Percentage(), ' ', Bar(marker='0', left='[', right=']'),
			' ', ' ', SimpleProgress()]  # see docs for other options

widgets2 = ['Creating Output: ', Percentage(), ' ', Bar(marker='0', left='[', right=']'),
			' ', ' ', SimpleProgress()]  # see docs for other options


def printing():  # just for cosmetics
		print "...creating library list..."
		pbar = ProgressBar(widgets=widgets, maxval=100)
		pbar.start()

		for i in range(0, 100+1, 10):  # here do something long at each iteration
			pbar.update(i)  # this adds the progress at each iteration
			sleep(1)
		pbar.finish()
		print


def printing_output():
		pbar2 = ProgressBar(widgets=widgets2, maxval=100)
		pbar2.start()

		for i in range(0, 100+1, 10):  # here do something long at each iteration
			pbar2.update(i)  # this adds the progress at each iteration
			sleep(1)
		pbar2.finish()
		print


# below is just an alternative/test
'''def create_output():
	f = file(make_file, 'w')
	sys.stdout = f
	pydoc.help("modules")
	f.close()
	sys.stdout = sys.__stdout__
	os.system("clear")'''


def create_output():  # saves the output of help('modules') to text file
	# save present stdout
	out = sys.stdout
	# set stdout to file handle
	sys.stdout = open(make_file, "w")
	# run your help code
	# its console output goes to the file now
	help("modules")
	sys.stdout.close()
	# reset stdout
	sys.stdout = out
	os.system("clear")


def create_handle():  # creates a handle to work with the contents of the file
	try:
		the_file = open("help_modules.txt", 'r')
		global handle
		handle = the_file.readlines()
		the_file.close()
	except ImportError:
		print "can't open file"


def delete_unused():
	try:  # trims anything not a module name
		new_file = open("lib_modules.txt", 'w')

		for line in handle:
			if line.startswith("\n"):
				line.replace("\n", "")
			elif line.startswith("Please"):
				line.replace("Please", "")
			elif line.startswith("Enter"):
				line.replace("Enter", "")
			elif line.startswith("for"):
				line.replace("for", "")
			else:
				new_file.write(line)
		# removes anything not a module name and writes it to a new file
		new_file.close()
	except ImportError:
		print "couldn't find file"
	sort_list()


def sort_list():  # sorts the list into alphabetical order
	sort_in = open("lib_modules.txt", 'r')
	sort_out = open("mod_list.txt", 'w')

	results = []
	sortfile = sort_in.readlines()

	for words in sortfile:
		for word in words.split():
			results.append(word)

	results.sort()

	for word in results:  # removes all private modules
		if word.startswith("_"):
			continue
		else:
			sort_out.write(word + "\n")

	sort_in.close()
	sort_out.close()  # housekeeping


def start_create():
	create_output()
	create_handle()
	delete_unused()
	sort_list()


