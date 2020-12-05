# from src.pypress import *
# from tcsources.ext_all import *
# from tcsources.pprss import *
import sys
from argparse import ArgumentParser
from cmprssn.ext_all import *
from cmprssn.pprss import *
from cmprssn.tools import *


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


def prse():
	parser = ArgumentParser(
		description='Python script to pipe 7zip commands'
	)
	
	parser.add_argument(
		'ppath',
		# dest='ppath',
		help='Path to 7z file or directory for compression'
	)
	
	subpz = parser.add_subparsers(
		help="7z mode. Extraction or Compression",
		dest='type',
	)
	
	cparse = subpz.add_parser('C')
	xparse = subpz.add_parser('X')
	
	# extraction parser and arguments
	xparse.add_argument(
		'-r',
		'--remove-archives',
		dest='remove',
		action='store_true',
		help='Triggers removal of archives after successful decompression'
	)
	
	xparse.add_argument(
		'-ie',
		'--include-extensions',
		dest='ext',
		help='Optional argument to include other archive formats'
	)
	
	# compression parser and arguments
	cparse.add_argument(
		'-r',
		'--remove-compressed',
		dest='remove',
		action='store_true',
		help='Triggers removal of directories after successful compression'
	)
	
	cparse.add_argument(
		'level',
		# '--compression-level',
		type=int,
		# action='store_true',
		default=0,
		# const=0,
		# nargs='?',
		help='Level of compression for all objects to compress (0-9). Default = 0',
		choices=range(0, 10),
	)
	
	cparse.add_argument(
		'-mode',
		'--compression-mode',
		dest='mode',
		# action='store_true',
		choices=['R', 'P', 'S'],
		default='P',
		type=str,
		# const='',
		# nargs='?',
		help="Compress root argument, sub-directories in the root level, or all directories recursively"

	)
	
	return parser.parse_args()


def compression_wrapper(argz):
	
	squeezer(argz.path, argz.level, argz.mode)


def x_func(argz):
	
	master_blaster(argz.path, argz)
	
	# # //db&t
	# print(argz)
	# # //db&t
	
	pass


def main_implementation(arggz):
	
	arggz.path = os.path.abspath(arggz.path)
	
	obj = InfoGather(get_du_size(arggz.path), arggz.path, arguments=arggz)
	
	if not os.path.exists(arggz.path):
		print(Fore.RED + "directory doesn't exist: %s" % arggz.path + Style.RESET_ALL)
		sys.exit(1)
	
	
	if arggz.type == 'C':
		compression_wrapper(arggz)
		
		obj.get_compressed_size()
		
		obj.display_values()
		
		obj.logger_json()
	
	
	
	elif arggz.type == 'X':
		x_func(arggz)

		
main_implementation(prse())

