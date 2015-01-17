#!/usr/local/bin/python

# libraries
import numpy as np
from os import walk
import skimage
from skimage import data, filter, color, io
from skimage.draw import circle_perimeter
from skimage.feature import peak_local_max
from skimage.transform import hough_circle
from skimage.util import img_as_ubyte


class Analyzer:
	# constructor
	def __init__(self, folder, min_d, px_per_micron):
		self.folder = folder
		self.min_d = min_d
		self.px_per_micron = px_per_micron
        
	def read_folder(self):
		"""
		Read the input folder, read, list, and return the filenames inside folder
		@return {Array} f: all filenames in input folder
		"""
		f = []
		for (_, _, filenames) in walk(self.folder):
			f.extend(filenames)
			break
		print 'Opening', self.folder
		return f
    
	def process_image(self, filename):
		"""
		Read image and write new image to 'processed' folder
		@param {String} file: image path
		"""
		filepath = self.folder + '/' + filename
		image = io.imread(filepath)
		print 'Processing file', filename
		self.render_output(filename, image)
    
	def render_output(self, filename, file):
		"""
		Writes the file to a path
		@param {String} filename: the name of the file (path not included)
		@param {ndarray} file: the data containing the image info (numpy data array)
		"""
		print 'Writing file', filename
		filename = self.folder + '/../analyzed-images/' + filename
		io.imsave(filename, file)
    
	def run(self):
		filenames = self.read_folder()
		for file in filenames:
			self.process_image(file)
    		
    		
if __name__ == '__main__':
	a = Analyzer('/Users/briannaG/GitHub/py-neurospheres/test/sample-images', 30, 92)
	a.run()