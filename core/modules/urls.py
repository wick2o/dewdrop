#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2

from core.menu import text
from core.ddcore import *

try:
	while True:
		create_menu(text.urls_text, text.urls_menu)
		
		print '   99) Return to main menu\n'
		
		url_item = raw_input(setprompt('0', 'Task'))
		
		if url_item == '99' or url_item == 'quit' or url_item == 'exit':
			break
			
		if url_item == '1':
			#shorten url
			url_input = raw_input(setprompt('0', 'Enter URL'))
			try:
				req_args = {'source':'indexpage','url':url_input,'submit':'Make+TinyURL!','alias':''}
				req_args_encoded = urllib.urlencode(req_args)
				url = 'http://tinyurl.com/create.php?%s' % (req_args_encoded)
				req = urllib2.Request(url)
				req.add_header('User-Agent', 'Mozilla/5.0 (BeOS; U; Haiku BePC; en-US; rv:1.8.1.14) Gecko/20080429 BonEcho/2.0.0.14')
				page = urllib2.urlopen(req)
				page_content = page.read()
				url_short = 'http://tinyurl.com/%s' % (get_data_between(page_content,'<blockquote><b>http://tinyurl.com/','</b><br><small>'))
				page.close()
				print url_short
			except:
				print 'Error\n'
				
		if url_item == '2':
			#enlongate url
			url_input = raw_input(setprompt('0', 'Enter URL'))
			try:
				req_args = {'url' : url_input, 'format' : 'php'}
				req_args_encoded = urllib.urlencode(req_args)
				url = 'http://api.longurl.org/v2/expand?%s' % (req_args_encoded)
				req = urllib2.Request(url)
				req.add_header('User-Agent', 'Mozilla/5.0 (BeOS; U; Haiku BePC; en-US; rv:1.8.1.14) Gecko/20080429 BonEcho/2.0.0.14')
				page = urllib2.urlopen(req)
				page_content = page.read()
				url_long = page_content[26:-3]
				page.close()
				print 'Enlongatged URL: %s\n' % (url_long)
			except:
				print 'Error\n'

except KeyboardInterrupt:
		pass