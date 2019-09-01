import os
import subprocess
from os import getcwd as og
from os import path
from os.path import isfile as piff
from os.path import join as oj
from pathlib import Path as plb
import pandas as pd
import fleep
import simplejson as json


def get_du_size(true_path):
	size_val = subprocess.check_output(['du', '-sh', true_path]).split()[0].decode('utf-8')
	
	return size_val


def get_all_ftypes(compression_path: path):
	ftypes = []
	
	# noinspection PyUnusedLocal
	fnames = []
	
	tzz = []
	
	for i in plb(compression_path).rglob("*.*"):
		
		# ftypes.add(os.path.splitext(i.name)[-1])
		
		if not piff(oj(i.parent, i.name)):
			continue
		
		# print(oj(i.parent, i.name))
		
		with open(oj(i.parent, i.name), 'rb') as FLE:
			
			extension = fleep.get(FLE.read(128)).extension
		
		# # //db&t
		# print(extension)
		# # //db&t
		
		tzz.append(os.path.splitext(i.name)[-1])
		
		ftypes.append(extension)
	
	# ftypes.add(extension)
	
	# fnames.append(i.name)
	
	# #flatten the lists
	# flattened_list = [y for x in list_of_lists for y in x]
	
	ftypes = list(set(q for f in ftypes for q in f))
	
	# # //db&t
	# print(ftypes)
	# # //db&t
	
	return ftypes


class InfoGather:
	
	def __init__(self, initial_size, original_path, arguments=None):
		
		self.initial_size = initial_size
		
		self.original_path = original_path
		
		self.destination_path = self.generate_destination()
		
		self.arguments = arguments
		
		self.file_types = get_all_ftypes(self.original_path)
		
		self.compressed_size = None
		
		# parse for compression
		# if any([arguments.mode, arguments.remove, arguments.level]):
		if arguments.type is "C":
			
			self.details = {
				'compression_level': arguments.level,
				'compression_mode': arguments.mode,
				'remove_boolean': arguments.remove,
				'compression': True
			}
		
		# parse for extraction
		# elif any([arguments.ext, arguments.remove]):
		elif arguments.type is "X":
			
			self.details = {
				'extraction': True,
				'included_extensions': str(arguments.ext).split(','),
				'removal_post_extraction': arguments.remove
			}
	
	def generate_destination(self):
		
		# noinspection PyUnusedLocal
		destination_path = ''
		
		if str(self.original_path).endswith('.7z'):
			
			destination_path = str(self.original_path).split('.7z')[0]
		
		
		elif str(self.original_path).endswith('/'):
			
			destination_path = str(self.original_path)[:-1] + ".7z"
		
		else:
			
			destination_path = str(self.original_path) + ".7z"
		
		return destination_path
	
	def display_values(self):
		
		# GENERAL STATIC INFO
		print("INITIAL SIZE: %s" % self.initial_size)
		
		print("ORIGINAL PATH: %s" % self.original_path)
		
		print("DESTINATION PATH/FILE: %s" % self.destination_path)
		# //GENERAL STATIC INFO//
		
		for k, v in self.details.items():
			print("%s: %s" % (k.upper(), v))
		
		print("CONTAINING FILE TYPES: %s" % str(self.file_types))
		
		print("COMPRESSED SIZE: %s" % self.compressed_size)
	
	def get_compressed_size(self):
		
		if piff(self.destination_path):
			self.compressed_size = get_du_size(self.destination_path)
	
	def to_dict(self):
		
		info = {
			"INITIAL_SIZE": self.initial_size,
			"ORIGINAL_PATH": self.original_path,
			"DESTINATION_PATH": self.destination_path,
			"COMPRESSION_DETAILS": str(self.details),
			"CONTAINING_FILE_TYPES": str(self.file_types),
			"COMPRESSED_SIZE": self.compressed_size
		}
		
		return info
	
	def logger_json(self):
		
		# # old log file setup
		# log_file_path = oj("/Users/chris/Dropbox/[Programming]/Scripts/[Python Scripts]/ThickPyToolkit/_testing/py7z/", "py7z.json")
		
		log_file_path = oj(og(), "log.json")
		
		# noinspection PyUnusedLocal
		loaded_log = []
		
		if piff(log_file_path):
			
			with open(log_file_path, 'r') as JRD:
				loaded_log = list(json.load(JRD))
			
			loaded_log.append(self.to_dict())
			
			# with open(os.path.join('/Users/chris/Desktop/ODCT.json'), 'w') as JSW:
			#     JSW.write(json.dumps(sort_objects(odct_mentions.values()), indent=4))
			
			with open(log_file_path, 'w') as JWRT:
				JWRT.write(json.dumps(loaded_log, indent=4))
		
		else:
			loaded_log = [self.to_dict()]
			
			with open(log_file_path, 'w') as JWRT:
				JWRT.write(json.dumps(loaded_log, indent=4))
	
	def logger_pd(self):
		
		# log_frame = pd.DataFrame(columns=list(self.to_dict().keys()), data=self.to_dict().values())
		
		# noinspection PyUnusedLocal
		log_frame = pd.DataFrame.from_dict(self.to_dict(), orient='index')
		
		log_file_path = oj(og(), "py7z.log")
		
		if piff(log_file_path):
			pass
		
		# print(log_frame.head())
		
		pass




