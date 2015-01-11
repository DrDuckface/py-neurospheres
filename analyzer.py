#!/usr/bin/python

# libraries
#import matplotlib.pyplot as plt
import numpy as np
from os import walk
import skimage
from skimage import data, filter, color
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
		print 'Opening folder...' + str(f)
		return f
    
	def process_image(self, file):
		print 'Processing file ' + file
		self.render_output(file)
    
	def render_output(self, file):
		print 'Rendering output for file ' + file
    
	def run(self):
		filenames = self.read_folder()
		for file in filenames:
			self.process_image(file)
    		
    		
if __name__ == '__main__':
	a = Analyzer('/Users/briannaG/GitHub/py-neurospheres/test/sample-images', 30, 92)
	a.run()