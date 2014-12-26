# Py-Neurospheres

Py-Neurospheres is a Python CLI tool for batch analysis of neurosphere images. It can be used to hasten the process of counting and measuring the diameter of the neurospheres.

## Pre-requisites

- Python 2.7x or 3.x

## Usage

Call the program from the command line and provide some parameters for analysis. The analysis output will be written to the source folder, within a subdirectory titled "analysis."

```
$ python py-neurospheres.py -i <folder> -d <min_d> -s <px_per_µm>
```

Parameters:

- `folder`: The location of folder containing the images, relative to the script
- `min_d`: The minimum threshold (in microns) for inclusion
- `px_per_µm`: The number of pixels per micron

Example:

```
$ python py-neurospheres.py -i ../folder -d 15 -s 10
```

## Output

When run, two CSV output files will be generated in the containing folder: a list of all neurosphere diameters (grouped by filename) and the number of neurospheres counted in each file.

|Filename  |ID    | D (µm)|
|:---------|:-----|------:|
|file1.png |1     |175    |
|file1.png |2     |312    |
|file2.jpg |3     |230    |
|file2.jpg |4     |111    |
|file3.gif |5     |150    |
|file3.gif |6     |156    |
|file3.gif |7     |199    |
|file3.gif |8     |211    |

|Filename  |Number of Neurospheres|
|----------|---------------------:|
|file1.png |12                    |
|file2.jpg |15                    |
|file3.gif |9                     |

Additionally, processed PNG images corresponding to each neurosphere input image will be generated, which will contain lines across the widest section of each neurosphere counted (and indicating an ID). This is useful for verification of the data.


## Acknowledgments

- Brian Nelson <yonbeastie@gmail.com> for his development help :)


## Contact

If you have questions or comments, please contact Brianna Goldenstein <brianna.goldenstein@gmail.com>. Contributions welcome!