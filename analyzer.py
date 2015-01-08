#!/usr/bin/python

# libraries
import skimage
import numpy as np
import matplotlib.pyplot as plt

from skimage import data, filter, color
from skimage.transform import hough_circle
from skimage.feature import peak_local_max
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte


class Analyzer:
	# constructor
	def __init__(self, folder, min_d, px_per_micron):
		self.folder = folder
		self.min_d = min_d
		self.px_per_micron = px_per_micron
        
	def open_folder(self):
		print 'Opening folder...'
		return ['image1.jpg', 'image2.jpg', 'image3.jpg']
    
	def process_image(self, file):
		print 'Processing file ' + file
		self.render_output(file)
    
	def render_output(self, file):
		print 'Rendering output for file ' + file
    
	def run(self):
		filenames = self.open_folder()
		for file in filenames:
			self.process_image(file)
    		
    		
if __name__ == '__main__':
	a = Analyzer('desktop', 30, 92)
	a.run()