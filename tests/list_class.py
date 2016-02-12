import sys
import os

os.chdir("/Users/blaka/Documents/python/liblist/temp")
#print "...creating library list"
make_file = "help_modules.txt"


def create_output():
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

create_output()