import os, sys
from os import listdir
import shutil

DIR = 'DCSASS Dataset/'

for folder in os.listdir(DIR):
	folder_url = DIR + folder + '/'
	for subfolder in os.listdir(folder_url):
		subfolder_url = folder_url + subfolder + '/'
		for clip in os.listdir(subfolder_url):
			clip_url = subfolder_url + clip
			shutil.move(clip_url, folder_url, copy_function = shutil.copytree)
		os.rmdir(subfolder_url)