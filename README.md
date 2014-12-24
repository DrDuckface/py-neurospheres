# Py-Neurospheres

Py-Neurospheres is a CLI tool for batch analysis of neurosphere images. It can be used to hasten the process of counting and measuring the diameter of the neurospheres.

## Pre-requisites

- Python 2.7x or 3.x

## Usage

Call the program from the command line and provide some parameters for analysis.

```
$ python py-neurospheres.py relative_folder_location min_diameter pixels_per_micron output_format
```

Parameters:

- `relative_folder_location`: The location of folder containing the images, relative to the script
- `min_diameter`: The minimum threshold (in microns) for inclusion
- `pixels_per_micron`: The number of pixels per micron
- `output_format`: csv, txt

Example:

```
$ python py-neurospheres.py ../folder 15 10 csv
```

## Output

When run, two output files will be generated in the containing folder: a list of all neurosphere diameters (grouped by filename) and the number of neurospheres counted in each file.

|Filename  |Diameter (microns)|
|----------|------------------|
|file1.png |175               |
|file1.png |312               |
|file2.jpg |230               |
|file2.jpg |111               |
|file3.gif |150               |
|file3.gif |156               |
|file3.gif |199               |
|file3.gif |211               |

|Filename  |Number of Neuropheres|
|----------|---------------------|
|file1.png |12                   |
|file2.jpg |15                   |
|file3.gif |9                    |


## Acknowledgments

- {placeholder}


## Contact

If you have questions or comments, please contact Brianna Goldenstein <brianna.goldenstein@gmail.com>. Contributions welcome!

