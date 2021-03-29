# you will need to watch until video 15 for this problem
import numpy as np 
# imagine a missile is launching to the north east with acceleration
# Resource: https://www.programiz.com/python-programming/matrix

# TODO: make a 2d numpy array X (the state matrix) to hold x, y, z, xv, yv, zv

# TODO: make a 2d numpy array A (the trasition matrix) hint: 6x6 matrix

# TODO: make a 2d numpy array B (the control input matrix) hint; 6x1  matrix

# TODO: make a 2d numpy array u (the control vector) hint: 3 accelerations since its 3D

# keep this the same since we just need to change the matrices to mess with the dimensions
for i in range(100):
    Bu = B.dot(u)
    X = A.dot(X) + Bu
    print("X-Position:", X[0][0], "X-Velocity:", X[3][0])
    print("Y-Position:", X[1][0], "Y-Velocity:", X[4][0])
    print("Z-Position:", X[2][0], "Z-Velocity:", X[5][0])
    print()