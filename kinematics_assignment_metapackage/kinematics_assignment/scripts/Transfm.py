#! /usr/bin/env python3

import numpy as np
from sympy import *

q1 = Symbol('q1')
q2 = Symbol('q2')
q3 = Symbol('q3')
q4 = Symbol('q4')
q5 = Symbol('q5')
q6 = Symbol('q6')
q7 = Symbol('q7')
L = 0.4
M = 0.39
d1 = 0.311
d2 = 0
d3 = L
d4 = 0
d5 = M
d6 = 0
d7 = 0.078
a1 = pi/2
a2 = -pi/2
a3 = -pi/2
a4 = pi/2
a5 = pi/2
a6 = -pi/2
a7 = -pi/2

Tz7 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,d7],[0,0,0,1]])
Tz6 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,d6],[0,0,0,1]])
Tz5 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,d5],[0,0,0,1]])
Tz4 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,d4],[0,0,0,1]])
Tz3 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,d3],[0,0,0,1]])
Tz2 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,d2],[0,0,0,1]])
Tz1 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,d1],[0,0,0,1]])

Tx = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

Rx7 = np.array([[1,0,0,0],[0,sp.cos(a7),-np.sin(a7),0],[0,np.sin(a7),np.cos(a7),0],[0,0,0,1]])
Rx6 = np.array([[1,0,0,0],[0,sp.cos(a6),-np.sin(a6),0],[0,np.sin(a6),np.cos(a6),0],[0,0,0,1]])
Rx5 = np.array([[1,0,0,0],[0,sp.cos(a5),-np.sin(a5),0],[0,np.sin(a5),np.cos(a5),0],[0,0,0,1]])
Rx4 = np.array([[1,0,0,0],[0,np.cos(a4),-np.sin(a4),0],[0,np.sin(a4),np.cos(a4),0],[0,0,0,1]])
Rx3 = np.array([[1,0,0,0],[0,np.cos(a3),-np.sin(a3),0],[0,np.sin(a3),np.cos(a3),0],[0,0,0,1]])
Rx2 = np.array([[1,0,0,0],[0,np.cos(a2),-np.sin(a2),0],[0,np.sin(a2),np.cos(a2),0],[0,0,0,1]])
Rx1 = np.array([[1,0,0,0],[0,np.cos(a1),-np.sin(a1),0],[0,np.sin(a1),np.cos(a1),0],[0,0,0,1]])

Rz7 = np.array([[np.cos(q7),-np.sin(q7),0,0],[np.sin(q7),np.cos(q7),0,0],[0,0,1,0],[0,0,0,1]])
Rz6 = np.array([[np.cos(q6),-np.sin(q6),0,0],[np.sin(q6),np.cos(q6),0,0],[0,0,1,0],[0,0,0,1]])
Rz5 = np.array([[np.cos(q5),-np.sin(q5),0,0],[np.sin(q5),np.cos(q5),0,0],[0,0,1,0],[0,0,0,1]])
Rz4 = np.array([[np.cos(q4),-np.sin(q4),0,0],[np.sin(q4),np.cos(q4),0,0],[0,0,1,0],[0,0,0,1]])
Rz3 = np.array([[np.cos(q3),-np.sin(q3),0,0],[np.sin(q3),np.cos(q3),0,0],[0,0,1,0],[0,0,0,1]])
Rz2 = np.array([[np.cos(q2),-np.sin(q2),0,0],[np.sin(q2),np.cos(q2),0,0],[0,0,1,0],[0,0,0,1]])
Rz1 = np.array([[np.cos(q1),-np.sin(q1),0,0],[np.sin(q1),np.cos(q1),0,0],[0,0,1,0],[0,0,0,1]])

temp7z = np.matmul(Tz7,Rz7)
temp7x = np.matmul(Tx,Rx7)
T7 = np.matmul(temp7z,temp7x)

temp6z = np.matmul(Tz6,Rz6)
temp6x = np.matmul(Tx,Rx6)
T6 = np.matmul(temp6z,temp6x)

temp5z = np.matmul(Tz5,Rz5)
temp5x = np.matmul(Tx,Rx5)
T5 = np.matmul(temp5z,temp5x)

temp4z = np.matmul(Tz4,Rz4)
temp4x = np.matmul(Tx,Rx4)
T4 = np.matmul(temp4z,temp4x)

temp3z = np.matmul(Tz3,Rz3)
temp3x = np.matmul(Tx,Rx3)
T3 = np.matmul(temp3z,temp3x)

temp2z = np.matmul(Tz2,Rz2)
temp2x = np.matmul(Tx,Rx2)
T2 = np.matmul(temp2z,temp2x)

temp1z = np.matmul(Tz1,Rz1)
temp1x = np.matmul(Tx,Rx1)
T1 = np.matmul(temp1z,temp1x)

Temp1 = np.matmul(T7,T6)
Temp2 = np.matmul(Temp1,T5)
Temp3 = np.matmul(Temp2,T4)
Temp4 = np.matmul(Temp3,T3)
Temp5 = np.matmul(Temp4,T2)
T = np.matmul(Temp5,T1)


