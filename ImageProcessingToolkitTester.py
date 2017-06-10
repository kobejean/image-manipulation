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

##template("griffin.gif")
##template("jean.gif")
##template("totoro.gif")
##
### problem 1
##border("griffin.gif", "#00FF00", 30)
##border("jean.gif", "#FF0000", 30)
##border("totoro.gif", "#0000FF", 100)
### problem 2
##half("griffin.gif")
##half("jean.gif")
##half("totoro.gif")
### problem 3
##double("griffin.gif")
##double("jean.gif")
##double("totoro.gif")
### problem 4
##sideClone("griffin.gif")
##sideClone("jean.gif")
##sideClone("totoro.gif")
##downClone("griffin.gif")
##downClone("jean.gif")
##downClone("totoro.gif")
### problem 5
##greyscale("griffin.gif")
##greyscale("jean.gif")
##greyscale("totoro.gif")
### problem 6
##smartBorder("griffin.gif",30)
##smartBorder("jean.gif",30)
##smartBorder("totoro.gif",100)
### problem 7
### scale_factor = float(input("SCALE FACTOR:"))
##scale_factor = 0.25
##scale("griffin.gif", scale_factor)
##scale("jean.gif", scale_factor)
##scale("totoro.gif", scale_factor)
### problem 8
##smartClone("griffin.gif",3,2)
##smartClone("jean.gif",3,2)
##smartClone("totoro.gif",3,2)
##tile("griffin.gif",3,2)
##tile("jean.gif",3,2)
##tile("totoro.gif",3,2)
### problem 9
##colorSubstitution("griffin.gif", 0.55, 0.15, 1.0)
##colorSubstitution("jean.gif", 0.5, 0.5, 1.0)
##colorSubstitution("totoro.gif", 0.5, 0.5, 1.0)
##contrastBorder("griffin.gif",30)
##contrastBorder("jean.gif",30)
##contrastBorder("totoro.gif",100)
### problem 10
##stretch("griffin.gif",math.pi,1)
##stretch("jean.gif", 0.5,1)
##stretch("totoro.gif",0.5,0.75)
### problem 11
##harrisShutter("jellyfish.gif",20,0)
harrisShutter("totoro.gif",50,0)
