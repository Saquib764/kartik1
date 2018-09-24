#!/usr/bin/env python
# Code Developer: Kartik Seshadri Chari
# Date: 06 Sept 2018
# Lab: 1 Task: 3
# This task wants us to design a wall follower that publishes the desired linear and angular velocities for the cartesian
# controller which acts as the subscriber

# This file subscribes to the ADC values and publishes the desired linear and angular velocities as a Twist message

# Importing dependencies and required message types
import rospy
from geometry_msgs.msg import Twist
from ras_lab1_msgs.msg import ADConverter

ADC_VAR = None
# Desired linear velocity in m/s
desired_velocity = 0.5
# Alpha factor which determines the desired angular velocity
alpha = 0.01

# Call-back function
def adc_input(adc_var):
    global ADC_VAR
    ADC_VAR = adc_var

# Main functin definition
def start():
    # Node initalization
    rospy.init_node("WallFollower")
    # Subscriber definition
    rospy.Subscriber("/kobuki/adc", ADConverter, adc_input)
    # Twist Publisher definition
    twist_pub = rospy.Publisher("/motor_controller/twist", Twist, queue_size=1)
    # Setting Publishing frequency
    r = rospy.Rate(10)
    # Twist message type object declaration
    twist_var = Twist()

    # Condition for the while loop
    while not rospy.is_shutdown():
        if ADC_VAR == None:
            continue
        # Assigning the values of adc distances to variables
        distance_sensor_1 = ADC_VAR.ch1
        distance_sensor_2 = ADC_VAR.ch2

        # Desired angular velocity
        desired_angular_velocity = alpha * (distance_sensor_1 - distance_sensor_2)

        # Assigning the linear and angular velocities to the twist_var
        twist_var.linear.x = desired_velocity
        twist_var.angular.z = desired_angular_velocity

        # Publishing the message
        twist_pub.publish(twist_var)
        r.sleep()

# Main Function Call
if __name__ == "__main__":
	start()
