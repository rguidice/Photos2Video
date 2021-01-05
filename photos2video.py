#!/usr/bin/env python3

import os
import argparse
import cv2

### TODO: ###
#research ways to deal with different sized images
    #make video size the size of largest image in array
        #only do this if argument is provided for better performance
#add in file extension to output argument if user doesn't

# Error checking for codec argument parsing
def codec_checker(arg):
    if str(arg) not in ['DIVX', 'mp4v']:
        raise argparse.ArgumentTypeError('Invalid codec argument.')
    return str(arg)

# Create argument parser and possible arguments
parser = argparse.ArgumentParser()
parser.add_argument('-dir', '--directory', dest = 'dir', type = str,
    default = '.', help = ('Directory that image files are stored in. Can take '
    'both relative and absolute file paths. Default = current working '
    'directory.'))
parser.add_argument('-ext', '--extension', dest = 'ext', type = str,
    default = 'any', help = ('File extension of image files. Supported '
    'extensions can be found in the OpenCV docs. Default = any.'))
parser.add_argument('-fr', '--framerate', dest = 'fr', type = int,
    default = 30, help = 'Frame rate of output video as int. Default = 30.')
parser.add_argument('-c', '--codec', dest = 'codec', type = codec_checker,
    default = 'DIVX', help = ('Video codec of output file. Options are "DIVX" '
    '(output extension of .avi) or "mp4v" (output extension of .mp4) Default '
    '= DIVX.'))
parser.add_argument('-out', '--output', dest = 'out', type = str,
    help = ('Output video file name. Can take both relative and absolute file '
    'paths.'))
args = parser.parse_args()

# Gather inputted arguments from argument parser
dir = args.dir
ext = args.ext
fr = args.fr
codec = args.codec
output = args.out

# Add appropriate file extension if it wasn't provided
if codec == 'DIVX':
    if not output.endswith('.avi'):
        output += '.avi'
else:
    if not output.endswith('.mp4'):
        output += '.mp4'

# Create list of images in directory with certain extension
images = []
for file in os.listdir(dir):
    if ext == 'any':
        ext_opts = ['bmp', 'dib', 'jpeg', 'jpg', 'JPG', 'jp2', 'png', 'webp', 'pbm',
         'pgm', 'ppm' 'pxm', 'pnm', 'sr', 'ras', 'tiff', 'tif', 'exr', 'hdr',
         'pic']
        if file.endswith(tuple(ext_opts)):
            images.append(file)
    else:
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
out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*str(codec)), fr, video_size)

# Write each image in the images array to the output video
for i in images:
    img = cv2.imread(os.path.join(dir, i))
    out.write(img)

# Release the output video
out.release()
