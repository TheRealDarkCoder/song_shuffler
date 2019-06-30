import os
import random

os.chdir('./')

fp = 0
files = len(os.listdir())

print(f"Removing previous shuffles of {files} files...")
for filename in os.listdir():
	fp = fp + 1
	new_name = filename.split("_", 1)[-1]
	if(filename != "shuffle.py" and filename != new_name):
		os.rename(filename, f"{new_name}")
	else:
		continue


used_random = []

print("Done!...")
if(fp != files):
	pass
if(fp == files):
	print(f"Shuffling {files} files...")
	for filename in os.listdir():
	    n = random.randint(1, len(os.listdir()))
	    while n in used_random:
	        n = random.randint(1, len(os.listdir()))
	    used_random.append(n)
	    if(filename != "shuffle.py"):
	    	os.rename(filename, f"{n}_{filename}")
	    else:
	    	continue
	print("Shuffling successfully done!")

