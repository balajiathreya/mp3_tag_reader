# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import eyeD3
import os
import shutil
path = "/home/balaji/Music/"
i = 0
files = os.listdir( path)
for file_name in files:
	print "file name "+file_name
#	file_name = file_name.replace(u'®','')
	full_file_name = path + file_name
	if not os.path.isdir(full_file_name):
		tag = eyeD3.Tag()
		tag.link(full_file_name)
		album =  tag.getAlbum()
		#album = album.replace(u'®','')
		if album == '':
			album = 'Unknown'
		album_folder = path+album
		print "album folder: "+album_folder
		if not os.path.exists(album_folder):
			os.makedirs(album_folder)
		else:
			print "dir exists"
		#shutil.copy(full_file_name,album_folder+file_name)
		os.rename(full_file_name,album_folder+"/"+file_name)
	
