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

# 1
border("arrow.gif", "#FFFF00", 5)
border("jellyfish.gif", "#FFFF00", 5)
# 2
half("arrow.gif")
half("jellyfish.gif")
# 3
double("arrow.gif")
double("jellyfish.gif")
# 4
sideClone("arrow.gif")
sideClone("jellyfish.gif")
# 5
greyscale("arrow.gif")
greyscale("jellyfish.gif")
