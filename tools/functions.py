import os
# all termcolor attributes: ["bold","dark","underline","blink","reverse","concealed"]
# text colors: [grey, red, green, yellow, blue, magenta, cyan, white]
# highlight colors: [on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white]
#
from os.path import join as oj

from colorama import Fore, Style, Back


def dir_mkr(specified_path):
	if not os.path.isdir(specified_path):
		os.makedirs(specified_path)


def walker(mydir):
	for root, dirs, files in os.walk(mydir):
		
		for f in files:
			
			f_abs = oj(root, f)
			
			# skips & removes '.DS_Store' files
			if f.startswith('.'):
				os.remove(f_abs)
				continue


def gprint(st):
	print(Fore.BLUE + st + Style.RESET_ALL)


def tprint(st):
	print("TEST PRINT: ", end="")
	print(Fore.GREEN + st + Style.RESET_ALL)


def eprint(st):
	print(Fore.RED + Back.WHITE + st + Style.RESET_ALL)











