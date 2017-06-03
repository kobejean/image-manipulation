###########################################################################
#                 Assignment 7 -- Image Manipulation                      #
#                                                                         #
#  Programmed by <YourName> (<TodaysDate>)                                #
#  Instructor:  Dean Zeller                                               #
#                                                                         #
#  Description:  This file contains solutions to ten problems dealing     #
#  with image manipulation.                                               #
#                                                                         #
#  Functions:                                                             #
#       template    --  Contains the basic structure for solutions        #
#       <describe others>                                                 #
#                                                                         #
#  This program is copyright (c) 2017 <YourName> and Dean Zeller.         #
#  All rights reserved.  Permission granted to use and modify for         #
#  educational purposes only.  Any commercial use of this code must       #
#  receive permission from the author(s).                                 #
###########################################################################
from graphics import GraphicsImage, GraphicsWindow
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
    win = GraphicsWindow()
    canvas = win.canvas()
    canvas.drawImage(image)
    image.save("template-"+filename)

##  Problem 1
# Add a function to the image processing toolkit that puts a border
# of a given color around an image.  Parameters:  color, width

##  Problem 2
# Add a function to the image processing toolkit that reduces an image by half,
# discarding every second pixel.

##  Problem 3
# Add a function to the image processing toolkit that doubles an image in
# size, replicating each pixel horizontally and vertically.

##  Problem 4
# Add a function to the image processing toolkit that places two copies
# of an image next to each other, and another function that places two
# copies of an image below each other.

##  Problem 5
# Add a function to the image processing toolkit that changes an
# image to grayscale, using a darkness ratio calculated by the following
# formula:    21.3% red + 71.5% green and 5.2% blue 

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
