import os
import re

from send2trash import send2trash

# lv_match = re.compile(r"\d")
#
# p = None
#
# press_me = sys.argv[1]
#
# if not str(press_me).endswith("/"):
# 	press_me += "/"
#
# level = sys.argv[2]
#
# other_flags = None
#
# argument_list = sys.argv[1:]
#
# ignore_pre_existing = True
#
# if not os.ppath.exists(press_me):
# 	print(Fore.LIGHTRED_EX, "object '%s' doesn't exist.. \nexiting..\n" % press_me)
# 	print(Fore.RESET)
# 	quit()
#
# if not lv_match.match(str(level)):
# 	print(Fore.LIGHTRED_EX, "missing level operator")
# 	print(Fore.LIGHTRED_EX, "exiting..")
# 	print(Fore.RESET)
# 	quit()
#
#
# try:
# 	press_me = argument_list[0]
#
# 	level = int(argument_list[1])
#
# 	other_flags = str(argument_list[2])
#
# 	print(Fore.LIGHTGREEN_EX, "\n#\n#\ncompressing %s at level %d with flags %s\n#\n#" % (press_me, level, other_flags))
# 	print(Fore.RESET)
#
#
# except Exception:
#
# 	press_me = argument_list[0]
#
# 	level = int(argument_list[1])
#
# 	print(Fore.LIGHTRED_EX, "no encryption. compressing %s at level %d" % (press_me, level))
# 	print(Fore.LIGHTRED_EX, "to encrypt, run again and pass 'enc' as a third argument")
# 	print(Fore.RESET)
#
# if 'E' in other_flags:
# 	p = 'enc'


# auto_do = sys.argv[3]

del_list = []

file_catch = re.compile(r"\.[a-zA-Z0-9]{1,6}$")


def compressor(chew_it, lv):
	if str(chew_it).endswith('/'):
		chew_it = re.sub(r"/$", '', chew_it)
	
	# if p == 'enc':
	#
	# 	os.system("""7z a -t7z -p -m0=lzma -mx=%d -mfb=64 -md=32m -ms=on "%s.7z" "%s" """ % (lv, chew_it, chew_it))
	#
	# else:
		
		os.system("""7z a -t7z -m0=lzma -mx=%d -mfb=64 -md=32m -ms=on "%s.7z" "%s" """ % (lv, chew_it, chew_it))


def sub_compressor(root, chew_it, lv):
	if str(chew_it).endswith('/'):
		chew_it = re.sub(r"/$", '', chew_it)
		
	os.system("""cd "%s" && 7z a -t7z -m0=lzma -mx=%d -mfb=64 -md=32m -ms=on "%s.7z" "%s" """ % (root, lv, chew_it, chew_it))


# noinspection DuplicatedCode
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


# noinspection DuplicatedCode
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





# if 'D' in other_flags:
#
# 	recursor(press_me, level)
#
# 	acquire_dirs(press_me)
#
# 	compressor(press_me, level)
# 	del_list.append(press_me)
#
# 	if input("Remove Source Files ?\n").lower() == 'y':
#
# 		# parent
# 		try:
# 			# os.remove(press_me)
# 			for successful in del_list:
# 				send2trash(successful)
# 				print(Fore.LIGHTRED_EX, "removed %s" % successful)
# 			print(Fore.LIGHTRED_EX, "Source Removed.")
# 		except Exception as e:
# 			print(e)
# 			print(Fore.LIGHTRED_EX, "Couldn't Remove Source")
# 		finally:
# 			print(Fore.RESET)
# 	else:
# 		print(Fore.LIGHTRED_EX, "Source Preserved.")
# 		print(Fore.RESET)
#
#
# else:
#
# 	if 'S' in other_flags:
#
# 		sub_del_list = []
#
# 		for k in os.listdir(press_me):
#
# 			if k.startswith('.'):
# 				continue
#
# 			if not ignore_pre_existing:
# 				if k.endswith('.7z'):
# 					print(Fore.GREEN, "'%s' is already a 7z archive.." % k)
#
# 					if input("continue ?\n") == 'y':
#
# 						sub_press = press_me+'/'+k
#
# 						sub_compressor(press_me, sub_press, level)
#
# 						sub_del_list.append(sub_press)
#
# 					else:
# 						print("skipping '%s'\n" % k)
# 						continue
#
# 			print(Fore.RESET)
#
# 			sub_press = press_me + '/' + k
#
# 			sub_compressor(press_me, sub_press, level)
#
# 			sub_del_list.append(sub_press)
#
#
# 		if 'R' in other_flags:
# 			try:
# 				for sd in sub_del_list:
# 					if os.ppath.exists(sd):
# 						send2trash(sd)
# 						print(Fore.LIGHTGREEN_EX, "removed %s" % sd)
#
# 					else:
# 						print(Fore.LIGHTRED_EX, "ppath '%s' doesn't exist" % sd)
#
# 					print(Fore.RESET)
#
# 			except Exception as e:
# 				print(Fore.LIGHTRED_EX, e)
#
# 			finally:
# 				print(Fore.RESET)
#
# 		elif 'R' not in other_flags:
# 			# if input(Fore.LIGHTCYAN_EX, "remove children ?\n").lower() == 'y':
# 			#     print(Fore.RESET)
# 			if input("remove children ?\n").lower() == 'y':
#
# 				# sub-folders in parent
#
# 				try:
# 					for sd in sub_del_list:
# 						if os.ppath.exists(sd):
# 							send2trash(sd)
# 							print(Fore.LIGHTGREEN_EX, "removed %s" % sd)
#
# 						else:
# 							print(Fore.LIGHTRED_EX, "ppath '%s' doesn't exist" % sd)
#
# 						print(Fore.RESET)
#
# 				except Exception as e:
# 					print(Fore.LIGHTRED_EX, e)
#
# 				finally:
# 					print(Fore.RESET)
#
# 		else:
# 			print(Fore.MAGENTA, 'children preserved')
# 			print(Fore.RESET)
#
# 	if 'P' in other_flags:
# 		compressor(press_me, level)
# 		del_list.append(press_me)
#
#
# 		if input("Remove Source Files ?\n").lower() == 'y':
#
# 			# parent
# 			try:
# 				# os.remove(press_me)
# 				for successful in del_list:
# 					send2trash(successful)
# 					print(Fore.LIGHTRED_EX, "removed %s" % successful)
# 				print(Fore.LIGHTRED_EX, "Source Removed.")
# 			except Exception as e:
# 				print(e)
# 				print(Fore.LIGHTRED_EX, "Couldn't Remove Source")
# 			finally:
# 				print(Fore.RESET)
# 		else:
# 			print(Fore.LIGHTRED_EX, "Source Preserved.")
# 			print(Fore.RESET)


