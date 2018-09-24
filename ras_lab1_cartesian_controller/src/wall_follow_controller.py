#!/usr/bin/env python
# Code Developer: Kartik Seshadri Chari
# Date: 06 Sept 2018
# Lab: 1 Task: 3
# This task wants us to design a wall follower that publishes the desired linear and angular velocities for the cartesian
# controller which acts as the subscriber

# This file subscribes to both the encoder values as well as the Twist message and publishes the PWM values that control the motor velocities

# Importing dependencies and required message types
import rospy
from geometry_msgs.msg import Twist
from ras_lab1_msgs.msg import Encoders
from ras_lab1_msgs.msg import PWM

ENC_VAR = None
TW_VAR = Twist()
# Distance between the 2 wheel bases in m
b = 0.115
# Radius of Curvature of the kobuki diff bot in m
R = 0.0352
# Integral error variable
error_integral_1 = 0
error_integral_2 = 0
# Time interval between 2 readings
dt = 1
# PI Controller gains
Kp1 = 45
Ki1 = 15
Kp2 = 40
Ki2 = 25

# Callback Functions
def enc_feedback(enc_var):
    global ENC_VAR
    ENC_VAR = enc_var

def twist_input(tw_var):
    global TW_VAR
    TW_VAR = tw_var

# Main Function definition
def start():
    # Node initalization
    rospy.init_node("FeedbackController")
    # Subscriber definitions
    rospy.Subscriber("/kobuki/encoders",Encoders,enc_feedback)
    rospy.Subscriber("/motor_controller/twist",Twist,twist_input)
    # PWM Publisher definition
    pwm_pub = rospy.Publisher("/kobuki/pwm",PWM,queue_size=1)
    # Setting Publishing frequency
    r = rospy.Rate(10)
    # PWM message type object declaration
    pwm_var = PWM()

    # Global assignment
    global error_integral_1
    global error_integral_2

    # Condition for the while loop
    while not rospy.is_shutdown():
        if ENC_VAR == None:
            continue

        # Assigning the values of current wheel angular velocities to a variable
        omega_1 = ENC_VAR.delta_encoder1
        omega_2 = ENC_VAR.delta_encoder2

        # Calculating corresponding wheel linear velocities frim the formula V = W.r
        velocity_1 = omega_1 * R
        velocity_2 = omega_2 * R
        #print "Velocity1:",velocity_1, "Velocity2:",velocity_2

        # Calculating the current linear velocity of the Kobuki robot
        current_velocity = 0.5 * (velocity_1 + velocity_2)

        # Calculating the current angular velocity of the Kobuki robot
        current_angular_velocity = (velocity_2 - velocity_1) / (2*b)

        # Defining the desired linear and angular velocity
        desired_velocity = TW_VAR.linear.x
        desired_angular_velocity = TW_VAR.angular.z

        # Calculating the desired wheel velocities
        desired_velocity_1 = desired_velocity - (b*desired_angular_velocity)
        desired_velocity_2 = desired_velocity + (b*desired_angular_velocity)

        # Calculating the linear velocity errors of both the wheels
        error_velocity_1 = desired_velocity_1 - velocity_1
        error_velocity_2 = desired_velocity_2 - velocity_2

        # Reimann Sum approximation of the integral terms
        error_integral_1 = error_integral_1 + (error_velocity_1 * dt)
        error_integral_2 = error_integral_2 + (error_velocity_2 * dt)

        # Control Outputs
        U_wheel_1 = Kp1 * error_velocity_1 + Ki1 * error_integral_1
        U_wheel_2 = Kp2 * error_velocity_2 + Ki2 * error_integral_2

        # Assigning the pwm values to the pwm_var
        pwm_var.PWM1 = U_wheel_1
        pwm_var.PWM2 = U_wheel_2

        # Publishing the message
        pwm_pub.publish(pwm_var)
        r.sleep()

# Main Function Call
if __name__ == "__main__":
	start()