import os
file_path="C:\\111111111111\\jason.txt"
with open(file_path) as file_obj:
	for line in file_obj.readlines():
		print line.rstrip()