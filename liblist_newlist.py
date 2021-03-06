#!/usr/bin/env python -W ignore::DeprecationWarning
# -*- coding: utf-8 -*-

__author__ = 'Blaka90'

# simplified version of sending help() output to a file
from time import sleep
from progressbar import *
import platform
import pydoc
import getpass

'''
	start making compatible with python3.5 as joining the dark side
	may need to look at create_output() see if works on windows

	find where temp||tmp is on each system and store the modlists there(should have read/write on any)
'''


# change into the desired working path
plat = platform.uname()
user = getpass.getuser()
os_sys = sys.platform


# added since i am trying to make more universal
if "darwin" in os_sys:  # just because its my script
	if os.path.isfile("/Users/" + user + "/Documents/python/liblist/temp/help_modules.txt"):
		os.chdir("/Users/" + user + "/Documents/python/liblist/temp/")  # and that's where it lives on my machine
elif "linux" in os_sys:
	# delete this if statement if files do not exit yet or it will fail here(any point in having it anyway?)
	if os.path.isfile("/home/" + user + "/Documents/python/liblist/temp/help_modules.txt"):
		os.chdir("/home/" + user + "/Documents/python/liblist/temp/")
else:
	print("Wrong directory or your operating system is not compatible...")
	sleep(2)
	sys.exit(10)


make_file = "help_modules.txt"  # initial output file for the module list


# actually slows down the program but just wanted some visual appeal
# see docs for other options
widgets = ['Preparing files: ', Percentage(), ' ', Bar(marker='0', left='[', right=']'), ' ', ' ', SimpleProgress()]  

widgets2 = ['Creating Output: ', Percentage(), ' ', Bar(marker='0', left='[', right=']'), ' ', ' ', SimpleProgress()]


def printing():  # just for cosmetics
		print("...creating library list...")
		pbar = ProgressBar(widgets=widgets, maxval=100)
		pbar.start()

		for i in range(0, 100+1, 10):  # here do something long at each iteration
			pbar.update(i)  # this adds the progress at each iteration
			sleep(1)
		pbar.finish()
		print()


def printing_output():
		pbar2 = ProgressBar(widgets=widgets2, maxval=100)
		pbar2.start()

		for i in range(0, 100+1, 10):  # here do something long at each iteration
			pbar2.update(i)  # this adds the progress at each iteration
			sleep(1)
		pbar2.finish()
		print()


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
	sys.stdout = open(make_file, "w+")
	# run your help code
	# its console output goes to the file now
	pydoc.help("modules")
	sys.stdout.close()
	# reset stdout
	sys.stdout = out
	os.system("clear")


def create_handle():  # creates a handle to work with the contents of the file
	try:
		the_file = open(make_file, 'r')
		global handle
		handle = the_file.readlines()
		the_file.close()
	except ImportError:
		print("can't open file")


def delete_unused():
	try:  # trims anything not a module name
		new_file = open("lib_modules.txt", 'w+')

		for line in handle:
			if line.startswith("\n"):
				line.replace("\n", "")
			elif line.startswith("Please"):
				line.replace("Please", "")
			elif line.startswith("Enter"):
				line.replace("Enter", "")
			elif line.startswith("DEBUG"):
				line.replace("DEBUG", "")
			elif line.startswith("for"):
				line.replace("for", "")
			else:
				new_file.write(line)
		# removes anything not a module name and writes it to a new file
		new_file.close()
	except ImportError:
		print("couldn't find file")
	sort_list()


def sort_list():  # sorts the list into alphabetical order
	sort_in = open("lib_modules.txt", 'r')
	sort_out = open("mod_list.txt", 'w+')

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


