import os
import re
from os import listdir as ld
from os import makedirs
from os import path
from os.path import isdir as pid
from os.path import join as oj

from colorama import Fore, Back, Style
from send2trash import send2trash


def gprint(st):
	print(Fore.BLUE + st + Style.RESET_ALL)


def tprint(st):
	print("TEST PRINT: ", end="")
	print(Fore.GREEN + st + Style.RESET_ALL)


def eprint(st):
	print(Fore.RED + Back.WHITE + st + Style.RESET_ALL)


def dir_mkr(specified_path):
	if not path.isdir(specified_path):
		makedirs(specified_path)


def compressor(c_path, lv):
	
	if not pid(c_path):
		
		save_dir = os.path.dirname(c_path)
		
		arc_name = "%s.7z" % re.sub("\s", "_", os.path.basename(os.path.splitext(c_path)[0]))
		
		os.system("""7z a -t7z -m0=lzma -mx=%d -mfb=64 -md=32m -ms=on "%s" "%s" """ % (lv, oj(save_dir, arc_name), c_path))
		
	else:
		os.system("""7z a -t7z -m0=lzma -mx=%d -mfb=64 -md=32m -ms=on "%s.7z" "%s" """ % (lv, c_path, c_path))


def recursor(r_path, lv):
	
	if not pid(r_path):
		return
	
	d_list = []
	
	for root, drz, flz in os.walk(r_path, topdown=True):
		
		for d in drz:
			
			# if d.startswith('.'):
			# 	continue
			
			# if ".logic" in d:
			# 	continue
			
			
			d_list.append(oj(root, d))
	
	d_list = reversed(d_list)
	
	for dr in d_list:
		
		compressor(dr, lv)
		
		send2trash(dr)


def squeezer(s_path, level, mode):
	
	if str(s_path).endswith('/'):
		s_path = str(s_path)[:-1]
	
	if mode == 'S':
		
		for d in ld(s_path):
			
			sub_path = oj(s_path, d)
			
			if pid(sub_path):
				compressor(sub_path, level)
				send2trash(sub_path)
	
	elif mode == 'R':
		recursor(s_path, level)
		
		compressor(s_path, level)
		
		send2trash(s_path)
	
	elif mode == 'P':
		
		compressor(s_path, level)
		send2trash(s_path)
	
	
	
	
	
	
	
	
	










































