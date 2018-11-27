#!/usr/bin/env python

f = open("file_names.txt", "w+")
for i in range(200):
	file_name = "test_file_"+str(i)+"\r\n"
	f.write(file_name)
f.close()
