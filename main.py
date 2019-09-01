import sys
from argparse import ArgumentParser
from tools.compression import *
from tools.extraction import *
from tools.functions import *


def prse():
	parser = ArgumentParser(
		description='Python script to pipe 7zip commands'
	)
	
	# path argument
	parser.add_argument(
		'path',
		# dest='path',
		help='Path to 7z file or directory for compression'
	)
	
	# sub-parsers to split compression and extraction
	subpz = parser.add_subparsers(
		help="7z mode. Extraction or Compression",
		dest='type',
	)
	
	cparse = subpz.add_parser('C')
	xparse = subpz.add_parser('X')
	
	# # extraction parser and arguments
	# flag to delete archives after extracting them
	xparse.add_argument(
		'-d',
		'--delete-archives',
		dest='remove',
		action='store_true',
		help='Triggers removal of archives after successful decompression'
	)
	# option to include other archive types other than 7z
	xparse.add_argument(
		'-i',
		'--include-type',
		dest='ext',
		help='Optional argument to include other archive formats'
	)
	# # //extraction parser and arguments//
	
	# ————————————————————————————————————————
	# ————————————————————————————————————————
	# ————————————————————————————————————————
	
	# # compression parser and arguments
	# delete directories after compressed
	cparse.add_argument(
		'-d',
		'--delete-compressed',
		dest='remove',
		action='store_true',
		help='Triggers removal of directories after successful compression',
		default=None,
	)
	
	# compresssion level, between 0-9, default=0
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
	
	# set compression mode
	# 'S' for sub-directories only, given the following tree:
	"""
	./tstng
	├── dir1
	│   ├── a_sub_dir
	│   └── b_sub_dir
	├── dir2
	│   ├── c_sub_dir
	│   └── d_sub_dir
	├── dir3
	└── dir4
	"""
	# only dir1, dir2, dir3, and dir4 are compressed. Child directories of those directories are left uncompressed
	# ————————————————————————————————————————
	# 'P' for only the parent directory, this is the default.
	# ————————————————————————————————————————
	# 'R' for recursive directory compression, all
	# directories get compressed, the deepest leveled
	# first, and then it works its way up to the top
	# most level directory
	cparse.add_argument(
		'-m',
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
	
	squeezer(argz.path, argz.level, argz.mode, argz)


def x_func(argz):
	
	master_blaster(argz.path, argz)
	
	pass


def main_implementation(args, debug=False):
	
	if debug:
		print(args.remove)
		
		quit()
	
	global bin_file
	
	bin_file = shutil.which("7z")
	
	args.path = os.path.abspath(args.path)
	
	obj = InfoGather(get_du_size(args.path), args.path, arguments=args)
	
	# # //db&t
	# attrs = vars(obj)
	#
	# print(', '.join("%s: %s" % item for item in attrs.items()))
	#
	# print(args)
	#
	# obj.display_values()
	#
	# quit()
	# # //db&t
	
	if not bin_file:
		eprint("7zip executable not found, please install 7zip binaries and try again")
		quit(1)
	
	# if the directory doesn't exist, exit
	if not os.path.exists(args.path):
		print(Fore.RED + "directory doesn't exist: %s" % args.path + Style.RESET_ALL)
		sys.exit(1)
	
	
	if args.type == 'C':
		compression_wrapper(args)
		
		obj.get_compressed_size()
		
		obj.display_values()
		
		obj.logger_json()
	
	
	
	elif args.type == 'X':
		x_func(args)


main_implementation(prse())
















