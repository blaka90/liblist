import sys
import os
from itertools import chain

os.chdir("/Users/blaka/Desktop/")
print os.getcwd()

sort_in = open("lib_modules.txt", 'r')
sort_out = open("lib_split.txt",'w')

results = []
sortfile = sort_in.readlines()

for words in sortfile:
    for word in words.split():
        results.append(word)

results.sort()

for word in results:
    if word.startswith("_"):
        continue
    else:
        sort_out.write(word + "\n")

sort_in.close()
sort_out.close()
    

