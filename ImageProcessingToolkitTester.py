###########################################################################
#            Assignment 7 -- Image Manipulation (tester)                  #
#                                                                         #
#  Programmed by Jean Flaherty and Griffin Myers (06-03-2017)             #
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
#  This program is copyright (c) 2017 Jean Flaherty, Griffin Myers,       #
#  and Dean Zeller.                                                       #
#  All rights reserved.  Permission granted to use and modify for         #
#  educational purposes only.  Any commercial use of this code must       #
#  receive permission from the author(s).                                 #
###########################################################################
from ImageProcessingToolkit import *
import math

# template("arrow.gif")
# template("jellyfish.gif")
# template("totoro.gif")
#
# # problem 1
# border("arrow.gif", "#FFFF00", 5)
# border("jellyfish.gif", "#FFFF00", 5)
# border("totoro.gif", "#FF00FF", 5)
# # problem 2
# half("arrow.gif")
# half("jellyfish.gif")
# half("totoro.gif")
# # problem 3
# double("arrow.gif")
# double("jellyfish.gif")
# double("totoro.gif")
# # problem 4
# sideClone("arrow.gif")
# sideClone("jellyfish.gif")
# sideClone("totoro.gif")
# downClone("arrow.gif")
# downClone("jellyfish.gif")
# downClone("totoro.gif")
# # problem 5
# greyscale("arrow.gif")
# greyscale("jellyfish.gif")
# greyscale("totoro.gif")
# # problem 6
smartBorder("griffin.gif",30)
smartBorder("jean.gif",30)
##smartBorder("totoro.gif",100)
# # problem 7
# # scale_factor = float(input("SCALE FACTOR:"))
# scale_factor = 0.25
# scale("arrow.gif", scale_factor)
# scale("jellyfish.gif", scale_factor)
# scale("totoro.gif", scale_factor)
# # problem 8
# smartClone("arrow.gif",3,2)
# smartClone("jellyfish.gif",3,2)
# smartClone("totoro.gif",3,2)
# # problem 9
# colorSubstitution("arrow.gif", 0.55, 0.15, 1.0)
# colorSubstitution("jellyfish.gif", 0.5, 0.5, 1.0)
# colorSubstitution("totoro.gif", 0.5, 0.5, 1.0)
contrastBorder("griffin.gif",30)
contrastBorder("jean.gif",30)
##contrastBorder("totoro.gif",100)
# # problem 10
# stretch("arrow.gif",math.pi,1)
# stretch("jellyfish.gif", 0.5,1)
# stretch("totoro.gif",0.5,0.75)
