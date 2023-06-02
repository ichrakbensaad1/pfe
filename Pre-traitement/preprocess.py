import os, sys
from os import listdir


main_folder = 'DCSASS Dataset/'
fps = 25

for folder in listdir(main_folder):
	folder_url = main_folder+folder
	for file in listdir(folder_url):
		file_url = folder_url+'/'+file
		if os.path.isfile(file_url):
			if not os.path.isdir(file_url[:-4]):
				os.mkdir(file_url[:-4])
				print("Extracting frames from ", file_url)
				os.system('ffmpeg -i "{}" -vf fps={} "{}/%05d.jpg"'.format(file_url, fps, file_url[:-4]))
				os.remove(file_url)