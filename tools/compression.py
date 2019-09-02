import os
import re
from os import listdir as ld
from os import makedirs
from os import path
from os.path import isdir as pid
from os.path import join as oj
from colorama import Fore, Back, Style
from send2trash import send2trash
from tools.functions import *
from tools.info import *


def compressor(compression_path, compression_level, zargs=None):
	
	try:
		if not pid(compression_path):
			
			save_dir = os.path.dirname(compression_path)
			
			# replace all spaces in name with '_'
			arc_name = "%s.7z" % re.sub("\s", "_", os.path.basename(os.path.splitext(compression_path)[0]))
			
			os.system(
				"""7z a -t7z -m0=lzma -mx=%d -mfb=64 -md=32m -ms=on "%s" "%s" """ % (compression_level, oj(save_dir, arc_name), compression_path))
		
		elif zargs:
			os.system("""7z a -t7z -m0=lzma -mx=%d -mfb=64 -md=32m -ms=on %s "%s.7z" "%s" """ % (compression_level, zargs, compression_path, compression_path))
		
		else:
			os.system("""7z a -t7z -m0=lzma -mx=%d -mfb=64 -md=32m -ms=on "%s.7z" "%s" """ % (compression_level, compression_path, compression_path))
		
		return compression_path
	
	except NotADirectoryError as NADE:
		eprint("Couldn't compress directory '%s'" % compression_path)
		print(str(NADE))
		return ''


def recursor(r_path, lv):
	if not pid(r_path):
		return
	
	directory_list = []
	
	for root, drz, flz in os.walk(r_path, topdown=True):
		
		for d in drz:
			directory_list.append(oj(root, d))
	
	# reverse directory tree to get the deepest level first
	directory_list = reversed(directory_list)
	
	for dr in directory_list:
		compressor(dr, lv)
		send2trash(dr)


def squeezer(s_path, level, mode, argz):
	
	if argz.remove:
		removal_list = set()
	
	if str(s_path).endswith('/'):
		s_path = str(s_path)[:-1]
	
	# functionality for sub-directories
	if mode == 'S':
		for d in ld(s_path):
			
			sub_path = oj(s_path, d)
			
			# only compress directories
			if pid(sub_path):
				compressor(sub_path, level)
			
			# remove if the '-r' flag is passed
			if argz.remove:
				send2trash(sub_path)
	
	elif mode == 'R':
		recursor(s_path, level)
		compressor(s_path, level)
		
		if argz.remove:
			send2trash(s_path)
	
	elif mode == 'P':
		compressor(s_path, level)
		if argz.remove:
			send2trash(s_path)







