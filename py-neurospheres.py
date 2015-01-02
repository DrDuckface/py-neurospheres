#!/usr/bin/python

# libraries
import sys, getopt

# globals
folder = None
min_d = None
px_per_micron = None

def main(argv):
	global folder, min_d, px_per_micron
	try: 
		opts, args = getopt.getopt(argv, 'hi:d:s:', ['folder=', 'min_d=', 'px_per_micron='])
	except getopt.GetoptError:
		print 'Invalid input'
		print 'Usage: py-neurospheres.py -i <folder> -d <min_d> -s <px_per_micron>'
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-i', '--folder'):
			folder = arg
		elif opt in ('-d', '--min_d'):
			min_d = arg
		elif opt in ('-s', '--px_per_micron'):
			px_per_micron = arg
	
	if folder == None or min_d == None or px_per_micron == None:
		print 'Invalid input'
		print 'Usage: py-neurospheres.py -i <folder> -d <min_d> -s <px_per_micron>'
		sys.exit()
	else:
		print 'input folder:', folder
		print 'minimum diameter:', min_d
		print 'image scale (pixels per micron):', px_per_micron
		
if __name__ == '__main__': 
	main(sys.argv[1:])