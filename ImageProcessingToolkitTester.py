###########################################################################
#            Assignment 7 -- Image Manipulation (tester)                  #
#                                                                         #
#  Programmed by <YourName> (<TodaysDate>)                                #
#  Instructor:  Dean Zeller                                               #
#                                                                         #
#  Description:  This file contains the tester for the                    #
#                ImageProcessingToolkit.                                  #
#                                                                         #
#  External Files:                                                        #
#      graphics.py  -- Contains the commands for image manipulation       #
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
from ImageProcessingToolkit import *

template("arrow.gif")
template("jellyfish.gif")
template("totoro.gif")

# 1
border("arrow.gif", "#FFFF00", 5)
border("jellyfish.gif", "#FFFF00", 5)
border("totoro.gif", "#FF00FF", 5)
# 2
half("arrow.gif")
half("jellyfish.gif")
half("totoro.gif")
# 3
double("arrow.gif")
double("jellyfish.gif")
double("totoro.gif")
# 4
sideClone("arrow.gif")
sideClone("jellyfish.gif")
sideClone("totoro.gif")
# 5
greyscale("arrow.gif")
greyscale("jellyfish.gif")
greyscale("totoro.gif")
# 7
scale_factor = float(input("SCALE FACTOR:"))
scale("arrow.gif", scale_factor)
scale("jellyfish.gif", scale_factor)
scale("totoro.gif", scale_factor)
