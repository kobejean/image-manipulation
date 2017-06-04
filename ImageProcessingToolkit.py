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
#  This program is copyright (c) 2017 Jean Flaherty, Griffin Myers,       #
#  and Dean Zeller. All rights reserved.  Permission granted to use and   #
#  modify for educational purposes only.  Any commercial use of this code #
#  must receive permission from the author(s).                            #
###########################################################################

from graphics import GraphicsImage, GraphicsWindow
from ColorUtils import *

SHOULD_DISPLAY_IMAGE = True

##  Template
# Use this function as a template for solving the problems below.
def template(filename):
    image = GraphicsImage(filename)
    width = image.width()
    height = image.height()
    for row in range(height):
        for col in range(width):
            # get the current pixel
            (red, green, blue) = image.getPixel(row,col)
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
    image.save("output/template-"+filename)

##  Problem 1
# Add a function to the image processing toolkit that puts a border
# of a given color around an image.  Parameters:  color, width

def border(filename, color, border_width):
    orig_image = GraphicsImage(filename)
    orig_width = orig_image.width()
    orig_height = orig_image.height()

    new_width = orig_width + 2 * border_width
    new_height = orig_height + 2 * border_width
    new_image = GraphicsImage(new_width,new_height)
    for row in range(0,new_height):
        for col in range(0,new_width):

            # set booleans for conditions
            isTopBorder = row < border_width
            isBottomBorder = row >= new_height - border_width
            isLeftBorder = col < border_width
            isRightBorder = col >= new_width - border_width

             # get border color
            (b_red, b_green, b_blue) = hex_to_rgb(color)

            if (isTopBorder or isBottomBorder or isLeftBorder or isRightBorder):
                new_image.setPixel(row,col,b_red,b_green,b_blue)  # set to border color
            else:
                orig_row = row - border_width
                orig_col = col - border_width

                # get the current pixel
                (red, green, blue) = orig_image.getPixel(orig_row,orig_col)

                new_image.setPixel(row,col,red,green,blue)  # set to original color




    # save and display new image
    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(new_image)
    new_image.save("output/border-"+filename)

##  Problem 2
# Add a function to the image processing toolkit that reduces an image by half,
# discarding every second pixel.

def half(filename):
    original_image = GraphicsImage(filename)
    original_width = original_image.width()
    original_height = original_image.height()

    new_width = original_image.width()//2
    new_height = original_image.height()//2
    new_image = GraphicsImage(new_width,new_height)

    for row in range (0,original_height,2):
        for col in range (0,original_width,2):
            (red, green, blue) = original_image.getPixel(row,col)
            new_image.setPixel(row//2,col//2,red,green,blue)
    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(new_image)
    new_image.save("output/half-"+filename)

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
            (red, green, blue) = image.getPixel(orig_row,orig_col)

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
    new_image.save("output/double-"+filename)

##  Problem 4
# Add a function to the image processing toolkit that places two copies
# of an image next to each other, and another function that places two
# copies of an image below each other.

def sideClone(filename):
    original_image = GraphicsImage(filename)
    original_width = original_image.width()
    original_height = original_image.height()

    new_width = original_image.width() * 2
    new_height = original_image.height()
    new_image = GraphicsImage(new_width,new_height)

    for row in range (0,original_height):
        for col in range (0,original_width):
            (red, green, blue) = original_image.getPixel(row,col)
            new_image.setPixel(row,col,red,green,blue)
            new_image.setPixel(row,col+original_width,red,green,blue)

    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(new_image)
    new_image.save("output/side-clone-"+filename)

def downClone(filename):
    original_image = GraphicsImage(filename)
    original_width = original_image.width()
    original_height = original_image.height()

    new_width = original_image.width()
    new_height = original_image.height() * 2
    new_image = GraphicsImage(new_width,new_height)

    for row in range (0,original_height):
        for col in range (0,original_width):
            (red, green, blue) = original_image.getPixel(row,col)
            red = original_image.getRed(row,col)
            green = original_image.getGreen(row,col)
            blue = original_image.getBlue(row,col)
            new_image.setPixel(row,col,red,green,blue)
            new_image.setPixel(row+original_height,col,red,green,blue)

    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(new_image)
    new_image.save("output/down-clone-"+filename)


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
            (red, green, blue) = image.getPixel(row,col)

            grey = int(red * 0.213 + green * 0.715 + blue * 0.052)

            image.setPixel(row,col,grey,grey,grey)  # set to grey

    # save and display new image
    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(image)
    image.save("output/greyscale-"+filename)

##  Problem 6
# Modify problem 1 so that the border color is somehow selected based on
# the image itself, rather than as a parameter.  It could be through an
# average, most common pixel, or a complimentary color not used often.
# In the documentation, explain your algorithm for selecting the color.
# It should not be selected randomly.

# The border color is based on an algorithm that finds the average value
# of red, green, and blue in each pixel, and uses each average to create
# its own color. The function achieves this by finding the average values
# for every pixel in a for loop.
# -Griffin

def smartBorder(filename, border_width):
    orig_image = GraphicsImage(filename)
    orig_width = orig_image.width()
    orig_height = orig_image.height()

    new_width = orig_width + 2 * border_width
    new_height = orig_height + 2 * border_width
    new_image = GraphicsImage(new_width,new_height)

    red = 0
    blue = 0
    green = 0

    for row in range(orig_height):
        for col in range(orig_width):
            red += orig_image.getRed(row, col)
            green += orig_image.getGreen(row, col)
            blue += orig_image.getBlue(row, col)

    avg_red = red // (orig_width * orig_height)
    avg_green = green // (orig_width * orig_height)
    avg_blue = blue // (orig_width * orig_height)

    for row in range(0, new_height):
        for col in range(0, new_width):

            # set booleans for conditions
            isTopBorder = row < border_width
            isBottomBorder = row >= new_height - border_width
            isLeftBorder = col < border_width
            isRightBorder = col >= new_width - border_width

            if (isTopBorder or isBottomBorder or isLeftBorder or isRightBorder):
                new_image.setPixel(row,col,avg_red,avg_green,avg_blue)  # set to border color
            else:
                orig_row = row - border_width
                orig_col = col - border_width

                # get the current pixel
                (red, green, blue) = image.getPixel(row,col)
                red = orig_image.getRed(orig_row,orig_col)
                green = orig_image.getGreen(orig_row,orig_col)
                blue = orig_image.getBlue(orig_row,orig_col)

                new_image.setPixel(row,col,red,green,blue)  # set to original color

    # save and display new image
    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(new_image)
    new_image.save("output/smart-border-"+filename)


##  Problem 7
# Modify the code for problems 2 and 3 to include a scale parameter that
# applies to the picture.  A scale factor of .5 should halve the size (as
# problem 2), whereas a scale factor of 2.0 should double the size (as
# problem 3).  The tricky part is determining which pixels to replicate
# for off-numbers, such as 2.3.

def scale(filename, scale):
    original_image = GraphicsImage(filename)
    original_width = original_image.width()
    original_height = original_image.height()

    new_width = int(original_image.width() * scale)
    new_height = int(original_image.height() * scale)
    new_image = GraphicsImage(new_width,new_height)

    for row in range(0, new_height):
        for col in range(0, new_width):
            orig_row = int(row//scale)
            orig_col = int(col//scale)


            (red, green, blue) = original_image.getPixel(orig_row,orig_col)
            new_image.setPixel(row,col,red,green,blue)

    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(new_image)
    new_image.save("output/scale"+str(scale)+"x-" + filename)

##  Problem 8
# Modify the code for problem 4 to accept horizontal and vertical
# multiplicity factors for the image.  For example, a factor of (3,2)
# produces a single image replicating the original three copies wide and
# two copies tall.

def smartClone(filename, side, down):
    if not type(side) == int or not type(down) == int:
        print("Side and down need to be integers.")

    original_image = GraphicsImage(filename)
    original_width = original_image.width()
    original_height = original_image.height()

    new_width = original_image.width() * side
    new_height = original_image.height() * down
    new_image = GraphicsImage(new_width,new_height)

    for row in range (0,original_height):
        for col in range (0,original_width):
            (red, green, blue) = original_image.getPixel(row,col)

            for img_row in range (0, down):
                new_image.setPixel(row+img_row*original_height,col,red,green,blue)
            for img_col in range(0, side):
                new_image.setPixel(row,col+img_col*original_width,red,green,blue)

    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(new_image)
    new_image.save("output/smart-clone-"+filename)

##  Problem 9
# Modify the code from problem 5 to allow for other photographic print toning,
# such as alternate-ratio greyscale, pure black-and-white (with threshold
# parameters), sepia toning, hot-tone (reds), cold-tone (blues), negative,
# color substitution, or other color-related ideas.

# colorsys.rgb_to_hsv(45,201,18)
def colorSubstitution(filename, select_hue, threshhold, result_hue):
    image = GraphicsImage(filename)
    width = image.width()
    height = image.height()
    for row in range(height):
        for col in range(width):
            # get the current pixel
            (r,g,b) = image.getPixel(row,col)
            (h,s,v) = rgb_to_hsv(r,g,b)

            if select_hue - threshhold <= h and h <= select_hue + threshhold:
                h = (result_hue + h - select_hue) % 1.0
                (r,g,b) = hsv_to_rgb(h,s,v)
            image.setPixel(row,col,r,g,b)  # set to grey

    # save and display new image
    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(image)
    image.save("output/color-substitution-"+filename)

def contrastBorder(filename, border_width):
    orig_image = GraphicsImage(filename)
    orig_width = orig_image.width()
    orig_height = orig_image.height()

    new_width = orig_width + 2 * border_width
    new_height = orig_height + 2 * border_width
    new_image = GraphicsImage(new_width,new_height)

    red = 0
    blue = 0
    green = 0

    for row in range(orig_height):
        for col in range(orig_width):
            red += orig_image.getRed(row, col)
            green += orig_image.getGreen(row, col)
            blue += orig_image.getBlue(row, col)

    avg_red = red // (orig_width * orig_height)
    avg_green = green // (orig_width * orig_height)
    avg_blue = blue // (orig_width * orig_height)

    (h,s,v) = rgb_to_hsv(avg_red,avg_green,avg_blue)

    h = (h + 0.5) % 1.0

    (r,g,b) = hsv_to_rgb(h,s,v)

    for row in range(0, new_height):
        for col in range(0, new_width):

            # set booleans for conditions
            isTopBorder = row < border_width
            isBottomBorder = row >= new_height - border_width
            isLeftBorder = col < border_width
            isRightBorder = col >= new_width - border_width

            if (isTopBorder or isBottomBorder or isLeftBorder or isRightBorder):
                new_image.setPixel(row,col,r,g,b)  # set to border color
            else:
                orig_row = row - border_width
                orig_col = col - border_width

                # get the current pixel
                (red, green, blue) = orig_image.getPixel(orig_row,orig_col)

                new_image.setPixel(row,col,red,green,blue)  # set to original color

    # save and display new image
    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(new_image)
    new_image.save("output/smart-border-"+filename)

##  Problem 10
# Create a photo manipulation effect of your own design.  Ideas can include
# stretch, blur, mosaic, 8-bit, etc...

def stretch(filename, x, y):
    original_image = GraphicsImage(filename)
    original_width = original_image.width()
    original_height = original_image.height()

    new_width = int(original_image.width() * x)
    new_height = int(original_image.height() * y)
    new_image = GraphicsImage(new_width,new_height)

    for row in range (0,new_height):
        for col in range (0,new_width):
            orig_row = int(row//y)
            orig_col = int(col//x)

            (red, green, blue) = original_image.getPixel(orig_row,orig_col)
            new_image.setPixel(row,col,red,green,blue) # a value of 1 is default image

    if (SHOULD_DISPLAY_IMAGE):
        win = GraphicsWindow()
        canvas = win.canvas()
        canvas.drawImage(new_image)
    new_image.save("output/stretch-"+filename)
