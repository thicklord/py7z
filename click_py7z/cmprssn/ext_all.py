import os
from os import makedirs
from os import path
from os.path import isdir as pid
from os.path import isfile as piff
from os.path import join as oj

from colorama import Fore, Back, Style
from send2trash import send2trash


master_archives_set = set()


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


def ext_7z(arc_path):
	cd = os.path.dirname(arc_path)
	# print(cd)
	
	os.system(""" cd "%s" && 7z x "%s" -aoa """ % (cd, arc_path))
	
	pass


# noinspection DuplicatedCode
def remove_all(pt):
	
	for root, drz, flz in os.walk(pt, topdown=True):
		
		for fl in flz:
			if fl.startswith("."):
				continue
			
			if fl.endswith(".7z"):
				
				arc = oj(root, fl)
				
				try:
					send2trash(arc)
					
					print(Fore.CYAN + "Trashed: " + Fore.GREEN + arc + Style.RESET_ALL)
				
				except Exception as e:
					print("problem trashing file: ", end="")
					eprint(arc)
					print('-' * 15 + "\nexception:")
					eprint(e)
					print('\n' + '-' * 15)
	
	pass


# noinspection DuplicatedCode
def walker(p, argset, mas):
	
	arc_count = 0
	
	archive_types = ['7z']
	
	a_list = []
	
	if argset.ext:
		
		if ',' in argset.ext:
			
			include = str(argset.ext).split(',')
			
			for i in include:
				archive_types.append(i)
		
		else:
			archive_types.append(argset.ext)
	
	for root, drz, flz in os.walk(p, topdown=True):
		
		for fl in flz:
			if fl.startswith("."):
				continue
			
			fext = os.path.splitext(fl)[1][1:]
			
			# if fl.endswith(".7z"):
			if fext in archive_types:
				
				arc_count += 1
				
				arc = oj(root, fl)
				
				if arc not in mas:
					ext_7z(arc)
				
				h, t = os.path.splitext(fl)
				
				new_dir = oj(os.path.dirname(arc), h)
				
				# if pid(new_dir) and rm_bool:
				# 	send2trash(arc)

				walker(new_dir, argset, mas)
				
				master_archives_set.add(arc)
				
				a_list.append(arc)
				
	
	if arc_count == 0:
		return True
	else:
		return a_list


def check_existence(obj, chk):
	
	if not obj.endswith(chk) or not pid(obj):
		print(Fore.LIGHTRED_EX + "'%s' not %s" % (obj, chk) + Style.RESET_ALL)
		quit()


# noinspection DuplicatedCode
def master_blaster(some_path, argset):
	
	new_root = None
	
	# master_archives_set = set()

	if piff(some_path):
		
		ext_7z(some_path)
		
		par = os.path.dirname(some_path)
		
		new_name = os.path.splitext(os.path.basename(some_path))[0]
		
		new_root = oj(par, new_name)
	
	elif pid(some_path):
		new_root = some_path
	
	tl = None
	
	while True:
		
		breaker = walker(new_root, argset, master_archives_set)
		
		if breaker:
			break
		
		elif tl == breaker:
			print("infinite loop")
			break
		
		tl = breaker
	
	for ap in master_archives_set:
		if piff(ap) and argset.remove:
			send2trash(ap)

