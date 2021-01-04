#!/usr/bin/env python3

import os
import argparse
import cv2

### TO-DO: ###
#add default option of current directory to -dir argument
    #research how os deals with relative vs absolute file paths
#research supported image file extensions and add them to help section
    #research ways to combine different types of image files into video
#research ways to deal with different sized images
#support multiple output video extensions/codecs?
#research industry standard way for these to-do lists
#research version numbering/changelog industry standards

# Create argument parser and possible arguments
parser = argparse.ArgumentParser()
parser.add_argument('-dir', '--directory', dest = 'dir', type = str, help = 'Directory that image files are stored in.')
parser.add_argument('-ext', '--extension', dest = 'ext', type = str, help = 'File extension of image files.')
parser.add_argument('-fr', '--framerate', dest = 'fr', type = int, default = 30, help = 'Frame rate of output video as int. Default = 30.')
parser.add_argument('-out', '--output', dest = 'out', type = str, help = 'Output video file name.')
args = parser.parse_args()

# Gather inputted arguments from argument parser
dir = args.dir
ext = args.ext
fr = args.fr
output = args.out

# Create list of images in directory with certain extension
images = []
for file in os.listdir(dir):
    if file.endswith(ext):
        images.append(file)

# Raise error if no images were found in the provided directory
if len(images) == 0:
    raise RuntimeError("No images found in directory provided")

# Get video size data from first image in array
first_image = cv2.imread(os.path.join(dir, images[0]))
height, width, layers = first_image.shape
video_size = (width, height)

# Create output cv2 VideoWriter
out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'DIVX'), fr, video_size)

# Write each image in the images array to the output video
for i in images:
    img = cv2.imread(os.path.join(dir, i))
    out.write(img)

# Release the output video
out.release()
