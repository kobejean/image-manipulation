###########################################################################
#                 Assignment 7 -- Image Manipulation                      #
#                                                                         #
#  Programmed by Jean Flaherty and Griffin Myers (06-03-2017)             #
#  Instructor:  Dean Zeller                                               #
#                                                                         #
#  Description:  This file contains solutions to ten problems dealing     #
#  with image manipulation.                                               #
#                                                                         #
#  Functions:                                                             #
#       template    --  Contains the basic structure for solutions        #
#       <describe others>                                                 #
#                                                                         #
#  This program is copyright (c) 2017 Jean Flaherty, Griffin Myers        #
#  and Dean Zeller. All rights reserved.  Permission granted to use and   #
#  modify for educational purposes only.  Any commercial use of this code #
#  must receive permission from the author(s).                            #
###########################################################################
from graphics import GraphicsImage, GraphicsWindow
from ColorUtils import *

SHOULD_DISPLAY_IMAGE = False

##  Template
# Use this function as a template for solving the problems below.
def template(filename):
    image = GraphicsImage(filename)
    width = image.width()
    height = image.height()
    for row in range(height):
        for col in range(width):
            # get the current pixel
            red = image.getRed(row,col)
            green = image.getGreen(row,col)
            blue = image.getBlue(row,col)
            # do something to the pixel
            if (red > green):   # meaningless comparison
                image.setPixel(row,col,0,0,0)  # set to black
            else:
                image.setPixel(row,col,255,255,255)  #set to white

    # save and display new image
    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(image)
    image.save("template-"+filename)

##  Problem 1
# Add a function to the image processing toolkit that puts a border
# of a given color around an image.  Parameters:  color, width

def border(filename, color, border_width):
    image = GraphicsImage(filename)
    width = image.width()
    height = image.height()
    for row in range(height):
        for col in range(width):
            # get the current pixel
            red = image.getRed(row,col)
            green = image.getGreen(row,col)
            blue = image.getBlue(row,col)

            # get border color
            (b_red, b_green, b_blue) = hex_to_rgb(color)

            # set booleans for conditions
            isTopBorder = row < border_width
            isBottomBorder = row >= height - border_width
            isLeftBorder = col < border_width
            isRightBorder = col >= width - border_width

            if (isTopBorder or isBottomBorder or isLeftBorder or isRightBorder):
                image.setPixel(row,col,b_red,b_green,b_blue)  # set to border color
            else:
                image.setPixel(row,col,red,green,blue)  # set to original color

    # save and display new image
    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(image)
    image.save("border-"+filename)

##  Problem 2
# Add a function to the image processing toolkit that reduces an image by half,
# discarding every second pixel.

##  Problem 3
# Add a function to the image processing toolkit that doubles an image in
# size, replicating each pixel horizontally and vertically.

def double(filename):
    image = GraphicsImage(filename)
    width = image.width()
    height = image.height()

    new_width = image.width()*2
    new_height = image.height()*2
    new_image = GraphicsImage(new_width, new_height)

    for row in range(0, new_height, 2):
        for col in range(0, new_width, 2):
            orig_row = row//2
            orig_col = col//2

            # get the current pixel
            red = image.getRed(orig_row,orig_col)
            green = image.getGreen(orig_row,orig_col)
            blue = image.getBlue(orig_row,orig_col)

            # set representative pixels
            new_image.setPixel(row,col,red,green,blue)      # set top left pixel
            new_image.setPixel(row+1,col,red,green,blue)    # set bottom left pixel
            new_image.setPixel(row,col+1,red,green,blue)    # set top right pixel
            new_image.setPixel(row+1,col+1,red,green,blue)  # set bottom right pixel

    # save and display new image
    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(new_image)
    new_image.save("size-double-"+filename)

##  Problem 4
# Add a function to the image processing toolkit that places two copies
# of an image next to each other, and another function that places two
# copies of an image below each other.

##  Problem 5
# Add a function to the image processing toolkit that changes an
# image to grayscale, using a darkness ratio calculated by the following
# formula:    21.3% red + 71.5% green and 5.2% blue

def greyscale(filename):
    image = GraphicsImage(filename)
    width = image.width()
    height = image.height()
    for row in range(height):
        for col in range(width):
            # get the current pixel
            red = image.getRed(row,col)
            green = image.getGreen(row,col)
            blue = image.getBlue(row,col)

            grey = int(red * 0.213 + green * 0.715 + blue * 0.052)

            image.setPixel(row,col,grey,grey,grey)  # set to grey

    # save and display new image
    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(image)
    image.save("greyscale-"+filename)

##  Problem 6
# Modify problem 1 so that the border color is somehow selected based on
# the image itself, rather than as a parameter.  It could be through an
# average, most common pixel, or a complimentary color not used often.
# In the documentation, explain your algorithm for selecting the color.
# It should not be selected randomly.

##  Problem 7
# Modify the code for problems 2 and 3 to include a scale parameter that
# applies to the picture.  A scale factor of .5 should halve the size (as
# problem 2), whereas a scale factor of 2.0 should double the size (as
# problem 3).  The tricky part is determining which pixels to replicate
# for off-numbers, such as 2.3.

##  Problem 8
# Modify the code for problem 4 to accept horizontal and vertical
# multiplicity factors for the image.  For example, a factor of (3,2)
# produces a single image replicating the original three copies wide and
# two copies tall.

##  Problem 9
# Modify the code from problem 5 to allow for other photographic print toning,
# such as alternate-ratio greyscale, pure black-and-white (with threshold
# parameters), sepia toning, hot-tone (reds), cold-tone (blues), negative,
# color substitution, or other color-related ideas.

##  Problem 10
# Create a photo manipulation effect of your own design.  Ideas can include
# stretch, blur, mosaic, 8-bit, etc...
