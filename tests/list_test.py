
__author__ = 'blaka'


# pipe the output of Python help() to a string
import subprocess
import os

os.chdir("/Users/blaka/Desktop/")
code_str = """\
help("modules")
"""
def create():
	# save the code
	filename = "help_code.py"
	fout = open(filename, "w")
	fout.write(code_str)
	fout.close()
	# execute the .py code and pipe the result to a string
	# give the full path of python.exe (here Windows path)
	test = "/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python " + filename
	process = subprocess.Popen(test, shell=True, stdout=subprocess.PIPE)
	# important, wait for external program to finish
	process.wait()
	print process.returncode  # 0 = success, optional check
	# read the result to a string
	help_str = process.stdout.read()
	# the result of the code is now in help_str
	print('-'*70)
	print(help_str)  # test
	# optionally write to a file
	# change the filename as needed
	fname = "help_print.txt"
	fout = open(fname, "w")
	fout.write(help_str)
	fout.close()
	print('-'*70)
	print("file %s written" % fname)

create()