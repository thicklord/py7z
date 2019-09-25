from os.path import isdir as pid
from os.path import isfile as piff

from send2trash import send2trash

from py7z.tools.functions import *

master_archives_set = set()


def ext_7z(archive_path):
	cwd = os.path.dirname(archive_path)
	
	os.system(""" cd "%s" && 7z x "%s" -aoa """ % (cwd, archive_path))
	
	pass


def remove_all(given_path):
	
	for root, drz, flz in os.walk(given_path, topdown=True):
		
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


def find_7zs(path_obj, args, archive_list):
	arc_count = 0
	
	archive_types = ['7z']
	
	a_list = []
	
	included_types = str(args.ext).split(',')
	
	if included_types:
		for i, e in enumerate(included_types):

			# //db&t
			print("type: %s" % str(e))
			# //db&t

			if str(e).startswith('.'):
				included_types[i] = e[1:]
			else:
				included_types[i] = e
		
		archive_types += included_types
	
	for root, drz, flz in os.walk(path_obj, topdown=True):
		
		# noinspection DuplicatedCode,DuplicatedCode
		for fl in flz:
			if fl.startswith("."):
				continue
			
			file_extension = os.path.splitext(fl)[1][1:]
			
			# if fl.endswith(".7z"):
			if file_extension in archive_types:
				
				arc_count += 1
				
				arc = oj(root, fl)
				
				if arc not in archive_list:
					ext_7z(arc)
				
				h, t = os.path.splitext(fl)
				
				new_dir = oj(os.path.dirname(arc), h)
				
				walker(new_dir, args, archive_list)
				
				master_archives_set.add(arc)
				
				a_list.append(arc)
				
	if arc_count == 0:
		return True
	else:
		return a_list


def walker(walk_path, argset, mas):
	
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
	
	for root, drz, flz in os.walk(walk_path, topdown=True):
		
		# noinspection DuplicatedCode,DuplicatedCode
		for fl in flz:
			
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
			
			if fl.startswith("."):
				continue
	
	
	if arc_count == 0:
		return True
	else:
		return a_list


def check_existence(obj, chk):
	
	if not obj.endswith(chk) or not pid(obj):
		print(Fore.LIGHTRED_EX + "'%s' not %s" % (obj, chk) + Style.RESET_ALL)
		quit()


def master_blaster(some_path, args):
	
	new_root = None
	
	if piff(some_path):
		
		ext_7z(some_path)
		
		par = os.path.dirname(some_path)
		
		new_name = os.path.splitext(os.path.basename(some_path))[0]
		
		new_root = oj(par, new_name)
	
	elif pid(some_path):
		new_root = some_path
	
	tl = None
	
	while True:
		breaker = find_7zs(new_root, args, master_archives_set)
		
		if breaker:
			break
		
		elif tl == breaker:
			print("infinite loop")
			break
		
		tl = breaker
	
	for ap in master_archives_set:
		if piff(ap) and args.remove:
			send2trash(ap)