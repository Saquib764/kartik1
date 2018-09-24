#! /usr/bin/env python3

import numpy as np
"""
    # {Kartik Chari}
    # {kartikc@kth.se}
"""
# Parameter Declaration
l0 = 0.07
l1 = 0.3
l2 = 0.35

def scara_IK(point):
    x = point[0]
    y = point[1]
    z = point[2]
    x1 = x - l0
    q = [0.0, 0.0, 0.0]

    """
    Fill in your IK solution here and return the three joint values in q
    """
    # Declaring the terms for q2 calculation
    # q2 = acos(x1^2 + y^2 - l1^2 - l2^2 /(2*l1*l2))
    q21 = np.power(x1,2) + np.power(y,2) - np.power(l1,2) - np.power(l2,2)
    q22 = 2 * l1 * l2
    q[1] = np.arccos(q21/q22)

    # Declaring the terms for q1 calclation
    # q1 = atan(y/x) - atac(l2*sin(q2) / (l1 + l2*cos(q2)))
    q11 = np.arctan2(y,x1)
    q12 = np.arctan2((l2 * np.sin(q[1])),(l1 + (l2 * np.cos(q[1]))))
    q[0] = q11 - q12

    # Declaring the terms for d3 calculation
    # d3 = z
    q[2] = z

    return q

def kuka_IK(point, R, joint_positions):
    x = point[0]
    y = point[1]
    z = point[2]
    q = joint_positions #it must contain 7 elements

    q = np.array(q)
    q1 = q[0]
    q2 = q[1]
    q3 = q[2]
    q4 = q[3]
    q5 = q[4]
    q6 = q[5]
    q7 = q[6]

    L = 0.4
    M = 0.39
    l0 = 0.311

    """
    Fill in your IK solution here and return the seven joint values in q
    """
    #K = np.matrix([[(39*np.cos(q2)*(np.sin(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) + np.cos(q4)*np.cos(q7)*np.sin(q6)))/500 - (39*np.sin(q2)*(np.cos(q3)*(np.cos(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) - np.cos(q7)*np.sin(q4)*np.sin(q6)) + np.sin(q3)*(np.cos(q5)*np.sin(q7) + np.cos(q6)*np.cos(q7)*np.sin(q5))))/500 + L*(np.sin(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) + np.cos(q4)*np.cos(q7)*np.sin(q6)) + M*np.cos(q7)*np.sin(q6)],[(39*np.sin(q2)*(np.cos(q3)*(np.cos(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) + np.sin(q4)*np.sin(q6)*np.sin(q7)) + np.sin(q3)*(np.cos(q5)*np.cos(q7) - np.cos(q6)*np.sin(q5)*np.sin(q7))))/500 - (39*np.cos(q2)*(np.sin(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) - np.cos(q4)*np.sin(q6)*np.sin(q7)))/500 - L*(np.sin(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) - np.cos(q4)*np.sin(q6)*np.sin(q7)) + M*np.sin(q6)*np.sin(q7)],[L*(np.cos(q4)*np.cos(q6) + np.cos(q5)*np.sin(q4)*np.sin(q6)) + (39*np.sin(q2)*(np.cos(q3)*(np.cos(q6)*np.sin(q4) - np.cos(q4)*np.cos(q5)*np.sin(q6)) + np.sin(q3)*np.sin(q5)*np.sin(q6)))/500 + M*np.cos(q6) + (39*np.cos(q2)*(np.cos(q4)*np.cos(q6) + np.cos(q5)*np.sin(q4)*np.sin(q6)))/500],[1]])

    K = np.array([(39*np.cos(q2)*(np.sin(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) + np.cos(q4)*np.cos(q7)*np.sin(q6)))/500 - (39*np.sin(q2)*(np.cos(q3)*(np.cos(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) - np.cos(q7)*np.sin(q4)*np.sin(q6)) + np.sin(q3)*(np.cos(q5)*np.sin(q7) + np.cos(q6)*np.cos(q7)*np.sin(q5))))/500 + L*(np.sin(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) + np.cos(q4)*np.cos(q7)*np.sin(q6)) + M*np.cos(q7)*np.sin(q6), (39*np.sin(q2)*(np.cos(q3)*(np.cos(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) + np.sin(q4)*np.sin(q6)*np.sin(q7)) + np.sin(q3)*(np.cos(q5)*np.cos(q7) - np.cos(q6)*np.sin(q5)*np.sin(q7))))/500 - (39*np.cos(q2)*(np.sin(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) - np.cos(q4)*np.sin(q6)*np.sin(q7)))/500 - L*(np.sin(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) - np.cos(q4)*np.sin(q6)*np.sin(q7)) + M*np.sin(q6)*np.sin(q7), L*(np.cos(q4)*np.cos(q6) + np.cos(q5)*np.sin(q4)*np.sin(q6)) + (39*np.sin(q2)*(np.cos(q3)*(np.cos(q6)*np.sin(q4) - np.cos(q4)*np.cos(q5)*np.sin(q6)) + np.sin(q3)*np.sin(q5)*np.sin(q6)))/500 + M*np.cos(q6) + (39*np.cos(q2)*(np.cos(q4)*np.cos(q6) + np.cos(q5)*np.sin(q4)*np.sin(q6)))/500, 1])

    J = np.array([[ 0, - (39*np.sin(q2)*(np.sin(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) + np.cos(q4)*np.cos(q7)*np.sin(q6)))/500 - (39*np.cos(q2)*(np.cos(q3)*(np.cos(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) - np.cos(q7)*np.sin(q4)*np.sin(q6)) + np.sin(q3)*(np.cos(q5)*np.sin(q7) + np.cos(q6)*np.cos(q7)*np.sin(q5))))/500,  (39*np.sin(q2)*(np.sin(q3)*(np.cos(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) - np.cos(q7)*np.sin(q4)*np.sin(q6)) - np.cos(q3)*(np.cos(q5)*np.sin(q7) + np.cos(q6)*np.cos(q7)*np.sin(q5))))/500,   (39*np.cos(q2)*(np.cos(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) - np.cos(q7)*np.sin(q4)*np.sin(q6)))/500 + L*(np.cos(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) - np.cos(q7)*np.sin(q4)*np.sin(q6)) + (39*np.cos(q3)*np.sin(q2)*(np.sin(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) + np.cos(q4)*np.cos(q7)*np.sin(q6)))/500,   (39*np.sin(q2)*(np.sin(q3)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) - np.cos(q3)*np.cos(q4)*(np.cos(q5)*np.sin(q7) + np.cos(q6)*np.cos(q7)*np.sin(q5))))/500 + (39*np.cos(q2)*np.sin(q4)*(np.cos(q5)*np.sin(q7) + np.cos(q6)*np.cos(q7)*np.sin(q5)))/500 + L*np.sin(q4)*(np.cos(q5)*np.sin(q7) + np.cos(q6)*np.cos(q7)*np.sin(q5)), (39*np.cos(q2)*(np.cos(q4)*np.cos(q6)*np.cos(q7) + np.cos(q5)*np.cos(q7)*np.sin(q4)*np.sin(q6)))/500 + L*(np.cos(q4)*np.cos(q6)*np.cos(q7) + np.cos(q5)*np.cos(q7)*np.sin(q4)*np.sin(q6)) + (39*np.sin(q2)*(np.cos(q3)*(np.cos(q6)*np.cos(q7)*np.sin(q4) - np.cos(q4)*np.cos(q5)*np.cos(q7)*np.sin(q6)) + np.cos(q7)*np.sin(q3)*np.sin(q5)*np.sin(q6)))/500 + M*np.cos(q6)*np.cos(q7), (39*np.cos(q2)*(np.sin(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) - np.cos(q4)*np.sin(q6)*np.sin(q7)))/500 - (39*np.sin(q2)*(np.cos(q3)*(np.cos(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) + np.sin(q4)*np.sin(q6)*np.sin(q7)) + np.sin(q3)*(np.cos(q5)*np.cos(q7) - np.cos(q6)*np.sin(q5)*np.sin(q7))))/500 + L*(np.sin(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) - np.cos(q4)*np.sin(q6)*np.sin(q7)) - M*np.sin(q6)*np.sin(q7)], [ 0,   (39*np.sin(q2)*(np.sin(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) - np.cos(q4)*np.sin(q6)*np.sin(q7)))/500 + (39*np.cos(q2)*(np.cos(q3)*(np.cos(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) + np.sin(q4)*np.sin(q6)*np.sin(q7)) + np.sin(q3)*(np.cos(q5)*np.cos(q7) - np.cos(q6)*np.sin(q5)*np.sin(q7))))/500, -(39*np.sin(q2)*(np.sin(q3)*(np.cos(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) + np.sin(q4)*np.sin(q6)*np.sin(q7)) - np.cos(q3)*(np.cos(q5)*np.cos(q7) - np.cos(q6)*np.sin(q5)*np.sin(q7))))/500, - (39*np.cos(q2)*(np.cos(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) + np.sin(q4)*np.sin(q6)*np.sin(q7)))/500 - L*(np.cos(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) + np.sin(q4)*np.sin(q6)*np.sin(q7)) - (39*np.cos(q3)*np.sin(q2)*(np.sin(q4)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) - np.cos(q4)*np.sin(q6)*np.sin(q7)))/500, - (39*np.sin(q2)*(np.sin(q3)*(np.cos(q7)*np.sin(q5) + np.cos(q5)*np.cos(q6)*np.sin(q7)) - np.cos(q3)*np.cos(q4)*(np.cos(q5)*np.cos(q7) - np.cos(q6)*np.sin(q5)*np.sin(q7))))/500 - (39*np.cos(q2)*np.sin(q4)*(np.cos(q5)*np.cos(q7) - np.cos(q6)*np.sin(q5)*np.sin(q7)))/500 - L*np.sin(q4)*(np.cos(q5)*np.cos(q7) - np.cos(q6)*np.sin(q5)*np.sin(q7)), (39*np.cos(q2)*(np.cos(q4)*np.cos(q6)*np.sin(q7) + np.cos(q5)*np.sin(q4)*np.sin(q6)*np.sin(q7)))/500 + L*(np.cos(q4)*np.cos(q6)*np.sin(q7) + np.cos(q5)*np.sin(q4)*np.sin(q6)*np.sin(q7)) + (39*np.sin(q2)*(np.cos(q3)*(np.cos(q6)*np.sin(q4)*np.sin(q7) - np.cos(q4)*np.cos(q5)*np.sin(q6)*np.sin(q7)) + np.sin(q3)*np.sin(q5)*np.sin(q6)*np.sin(q7)))/500 + M*np.cos(q6)*np.sin(q7), (39*np.cos(q2)*(np.sin(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) + np.cos(q4)*np.cos(q7)*np.sin(q6)))/500 - (39*np.sin(q2)*(np.cos(q3)*(np.cos(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) - np.cos(q7)*np.sin(q4)*np.sin(q6)) + np.sin(q3)*(np.cos(q5)*np.sin(q7) + np.cos(q6)*np.cos(q7)*np.sin(q5))))/500 + L*(np.sin(q4)*(np.sin(q5)*np.sin(q7) - np.cos(q5)*np.cos(q6)*np.cos(q7)) + np.cos(q4)*np.cos(q7)*np.sin(q6)) + M*np.cos(q7)*np.sin(q6)], [ 0, (39*np.cos(q2)*(np.cos(q3)*(np.cos(q6)*np.sin(q4) - np.cos(q4)*np.cos(q5)*np.sin(q6)) + np.sin(q3)*np.sin(q5)*np.sin(q6)))/500 - (39*np.sin(q2)*(np.cos(q4)*np.cos(q6) + np.cos(q5)*np.sin(q4)*np.sin(q6)))/500, -(39*np.sin(q2)*(np.sin(q3)*(np.cos(q6)*np.sin(q4) - np.cos(q4)*np.cos(q5)*np.sin(q6)) - np.cos(q3)*np.sin(q5)*np.sin(q6)))/500, (39*np.cos(q3)*np.sin(q2)*(np.cos(q4)*np.cos(q6) + np.cos(q5)*np.sin(q4)*np.sin(q6)))/500 - (39*np.cos(q2)*(np.cos(q6)*np.sin(q4) - np.cos(q4)*np.cos(q5)*np.sin(q6)))/500 - L*(np.cos(q6)*np.sin(q4) - np.cos(q4)*np.cos(q5)*np.sin(q6)), (39*np.sin(q2)*(np.cos(q5)*np.sin(q3)*np.sin(q6) + np.cos(q3)*np.cos(q4)*np.sin(q5)*np.sin(q6)))/500 - L*np.sin(q4)*np.sin(q5)*np.sin(q6) - (39*np.cos(q2)*np.sin(q4)*np.sin(q5)*np.sin(q6))/500, - L*(np.cos(q4)*np.sin(q6) - np.cos(q5)*np.cos(q6)*np.sin(q4)) - (39*np.sin(q2)*(np.cos(q3)*(np.sin(q4)*np.sin(q6) + np.cos(q4)*np.cos(q5)*np.cos(q6)) - np.cos(q6)*np.sin(q3)*np.sin(q5)))/500 - M*np.sin(q6) - (39*np.cos(q2)*(np.cos(q4)*np.sin(q6) - np.cos(q5)*np.cos(q6)*np.sin(q4)))/500, 0], [ 0, 0, 0, 0, 0, 0, 0]])

    J_inv = np.linalg.pinv(J)
    print(J_inv.shape)

    #X = np.matrix([[x],[y],[z-l0],[1]])
    X = np.array([x,y,(z),1])
    print(X.shape)

    X_cap = K
    print(X_cap.shape)

    Ex = X_cap - X
    print(Ex.shape)

    #Ex = np.transpose(Ex)

    Eq = np.matmul(J_inv,Ex)
    eQ = Eq.flatten()
    print(eQ)
    print(eQ.shape)
    print(q.shape)

    q = q - eQ
    q.flatten()
    print(q.shape)

    return q
