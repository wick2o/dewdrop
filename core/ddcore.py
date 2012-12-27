#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re

def check_os():
	if os.name == 'nt':
		os_sys = 'windows'
	elif os.name == 'posix':
		os_sys = 'posix'
	return os_sys
	
def setprompt(category, text):
	if category == '0' and text == '':
		return 'dewdrop> '
	if category == '0':
		return 'dewdrop> %s: ' % (text)

def yesno_prompt(category, text):
	valid_response = False
	while not valid_response:
		res = raw_input(setprompt(category, text))
		res = str.lower(response)
		if res == 'no' or res =='n':
			res = 'NO'
			valid_response = True
		elif res == 'yes' or res == 'y':
			res = 'YES'
			valid_response = True
		else:
			print ("Valid responose are 'n|y|N|Y|no|yes|No|Yes|NO|YES'")
	return res

def get_data_between(data, start_tag, end_tag):
	start = data.find(start_tag)
	if start !=1:
		start += len(start_tag)
		end = data[start:].find(end_tag)
		if end != -1:
			return data[start:start+end]
	return None
	
def remove_html_tags(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)
	
class create_menu:
	def __init__(self, text, menu):
		self.text = text
		self.menu = menu
		print text
		for i, option in enumerate(menu):
			menunum = i + 1
			#check to see if this line has 'return to main menu' code
			match = re.search('OD', option)
			if not match:
				if menunum < 10:
					print('   %s) %s' % (menunum,option))
				else:
					print('  %s) %s' % (menunum,option))
			else:
				print '\n  99) Return to Main Menu\n'
		return
