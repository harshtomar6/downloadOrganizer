# Let's write some code
# We download a lot of files from internet
# But Over time, these files become so unorganized in,
# Download directory that it's hard to search a file
# This Script is going to organize your downloaded files
# Automatically. 

# With that being said, Let's get started

import getpass
import os
import time

class DirectoryListener:

	def __init__(self, path):
		self.user = getpass.getuser()
		self.path = path
		self.count = 0

	def listen(self):
		while True:
			first_scan = []
			#print("Scaning")
			for entry in os.scandir(self.path):
				first_scan.append(entry)

			if len(first_scan) != self.count:
				#print("Found Something")
				self.count = len(first_scan)
				self.organize(first_scan)

			time.sleep(2)

	def organize(self, content):
		for entry in content:
			if self.isVideo(entry.name):
				os.rename(self.path+'/'+entry.name, '/home/'+self.user+'/Videos/'+entry.name)
			elif self.isAudio(entry.name):
				#print("Moving Audio")
				os.rename(self.path+'/'+entry.name, '/home/'+self.user+'/Music/'+entry.name)
			elif self.isImage(entry.name):
				os.rename(self.path+'/'+entry.name, '/home/'+self.user+'/Pictures/'+entry.name)
			elif self.isDocument(entry.name):
				os.rename(self.path+'/'+entry.name, '/home/'+self.user+'/Documents/'+entry.name)
			elif entry.name.endswith('.crdownload'):
				self.count -= 1


	def isVideo(self, name):
		formats = ['.mp4','.mkv','.webm','.flv','.vob','.ogv','.ogg','.gif','.drc','.gifv','.avi','.mng','.mov','.qt','.wmv','.rm','.yuv','.asf','.rmv','.mp2','.m4v','mpg','.mpeg','.3gp']

		for format in formats:
			if name.endswith(format):
				return True

		return False

	def isAudio(self, name):
		formats = ['.mp3','.wav','.aac','.ogg','.mpeg-4','.midi', '.m4a']

		for format in formats:
			if name.endswith(format):
				return True
		
		return False


	def isImage(self, name):
		formats = ['.jpeg','.png','.jpg','.exif','.tiff','.bmp','.webp','.ppm','.pgm','.pbm','.pnm','.heif','.bpg']

		for format in formats:
			if name.endswith(format):
				return True
		
		return False


	def isDocument(self, name):
		formats = ['.txt','.doc','.docx','.odt','.xml','.pdf','.rtf','.psd','.ai','.svg','.wp','.wpd','.ppt','.csv']

		for format in formats:
			if name.endswith(format):
				return True
		
		return False


if __name__ == '__main__':
	user = getpass.getuser()
	listener = DirectoryListener('/home/'+user+'/Downloads')
	listener.listen()
