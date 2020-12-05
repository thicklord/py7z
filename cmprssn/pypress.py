import os
import re

from send2trash import send2trash
import shutil



del_list = []

file_catch = re.compile(r"\.[a-zA-Z0-9]{1,6}$")

z_executable = shutil.which("7z")

if not z_executable:
	quit(1)

else:
	z_executable = os.path.join(z_executable)




def compressor(chew_it, lv):
	if str(chew_it).endswith('/'):
		chew_it = re.sub(r"/$", '', chew_it)
		
		os.system("""%s a -t7z -m0=lzma -mx=%d -mfb=64 -md=32m -ms=on "%s.7z" "%s" """ % (z_executable, lv, chew_it, chew_it))


def sub_compressor(root, chew_it, lv):
	if str(chew_it).endswith('/'):
		chew_it = re.sub(r"/$", '', chew_it)
		
	os.system("""cd "%s" && %s a -t7z -m0=lzma -mx=%d -mfb=64 -md=32m -ms=on "%s.7z" "%s" """ % (root, z_executable, lv, chew_it, chew_it))


def acquire_dirs(a_path):
	if not str(a_path).endswith('/'):
		a_path += '/'
	
	list_to_rm = []
	
	for d in os.listdir(a_path):
		
		cur = a_path + d
		
		if file_catch.search(str(cur)):
			continue
		
		if os.path.isdir(cur):
			list_to_rm.append(cur)
	
	for item in list_to_rm:
		send2trash(item)


def recursor(some_path, lv):
	if not str(some_path).endswith('/'):
		some_path += '/'
	
	for k2 in os.listdir(some_path):
		
		cur = some_path + k2
		
		if file_catch.search(str(cur)):
			continue
		
		if os.path.isdir(cur):
			
			# @2d0:
			# if os.ppath.basename(cur).startswith('.'):
			# 	print(cur)
			
			recursor(cur, lv)
			acquire_dirs(cur)
			compressor(cur, lv)








