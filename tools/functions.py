import os
import re
import sys
import requests
import pandas as pd
import time
import shutil
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import colored, cprint
# all termcolor attributes: ["bold","dark","underline","blink","reverse","concealed"]
# text colors: [grey, red, green, yellow, blue, magenta, cyan, white]
# highlight colors: [on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white]
# 
from os.path import join as oj
from os import getcwd as og
from os import listdir as ld
from os.path import isdir as pid
from os.path import isfile as piff
from os.path import abspath as pabs
import urllib.request
from os import path
from os import makedirs
from walkdir import filtered_walk as wdfw
from walkdir import all_paths as wdap
from walkdir import limit_depth as wdld
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











