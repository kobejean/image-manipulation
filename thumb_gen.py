###########################################################################
#                          Thumbnail Generation                           #
#                                                                         #
#  Programmed by Jean Flaherty (06-10-2017)                               #
#                                                                         #
#  Description:  This file generates thumbnails for the input and output  #
#       images                                                            #
#                                                                         #
#                                                                         #
#  This program is copyright (c) 2017 Jean Flaherty, Griffin Myers,       #
#  and Dean Zeller. All rights reserved.  Permission granted to use and   #
#  modify for educational purposes only.  Any commercial use of this code #
#  must receive permission from the author(s).                            #
###########################################################################

from graphics import GraphicsImage, GraphicsWindow
from color_utils import *
import glob, os

def thumb(filename, scale):
    filepath = os.path.abspath(filename)
    original_image = GraphicsImage(filepath)
    filename = os.path.basename(filepath)
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

    new_image.save("docs/media/thumb-" + filename)

for filename in os.listdir("input"):
    if filename.endswith(".gif"):
        thumb("input/" + filename, 0.25)

for filename in os.listdir("output"):
    if filename.endswith(".gif"):
        thumb("output/" + filename, 0.25)
