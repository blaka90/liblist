import importlib, __builtin__
import os
from prettytable import PrettyTable
from time import sleep



path = open("/Users/blaka/Documents/python//liblist/temp/mod_list.txt", "r")
path_mod = path.readlines()

num_list = []
path_list =[]
path_len = len(path_mod)

for num in range(0, path_len):
	num_list.append(str(num))

for p in path_mod:
	path_list.append(p)

mod_dict = dict(zip(num_list, path_list))

'''for pair in mod_dict.items():
	print pair'''

print mod_dict



def library_list():
	print "--------------------------------------------------"
	print "Here are the available library's:"
	print "--------------------------------------------------"
	table = PrettyTable(["Index", "Package"])
	count = 0
	for mod in path_mod:
		table.add_row(["%d" % count, "%s" % mod])
		count += 1
	print table
	print "--------------------------------------------------"
	ans = raw_input("what library would you like to look at?: ")
	print "--------------------------------------------------"
	print "You have chosen to look at %s" % ans
	print "--------------------------------------------------"
	sleep(1)
	try:
		global module
		module = __builtin__.__import__(ans)
	except ImportError:
		print "no such file(try changing lower/uppercase)"
		sleep(3)
		library_list()
	contents = dir(module)
	for c in contents:
		print c

repeat = ''
while repeat != "no":
	library_list()
	print "--------------------------------------------------"
	print "would you like to look at another library?"
	print "--------------------------------------------------"
	repeat = raw_input(">(yes/no) ").lower()

