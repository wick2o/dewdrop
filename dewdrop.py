#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from core.menu import text
from core.ddcore import *

def main():
	while True:
		try:
			show_main_menu = create_menu(text.main_text, text.main_menu)
			
			print '   99) Exit dewdrop toolkit\n'
			
			main_menu_choice = (raw_input(setprompt('0', '')))
			
			if main_menu_choice == 'exit' or main_menu_choice == '99' or main_menu_choice == 'quit':
				sys.exit()
		
			if main_menu_choice == '1':
				try:
					reload(core.modules.urls)
				except:
					import core.modules.urls
					
			if main_menu_choice == '2':
				sys.exit()
		except KeyboardInterrupt:
			pass
			
def setup():
	pass

if __name__ == "__main__":
	main()