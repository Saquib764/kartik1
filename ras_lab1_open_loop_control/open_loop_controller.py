#!/usr/bin/env python
# Code Developer: Kartik Seshadri Chari
# Date: 06 Sept 2018
# Lab: 1 Task: 1
# This task wants us to create an open loop controller and send signals to both the motors to move

# Importing dependencies and required message types
import rospy
from ras_lab1_msgs.msg import PWM

#Function definition
def start():
	# Node initialixe
	rospy.init_node("PWM_Publisher")
	# Creating a publisher object