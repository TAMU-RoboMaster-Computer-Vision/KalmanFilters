# you will need to watch until video 15 for this problem
import numpy as np 
# imagine a missile is launching to the north east with acceleration
# Resource: https://www.programiz.com/python-programming/matrix

# TODO: make a 2d numpy array X (the state matrix) to hold x, y, xv, yv

# TODO: make a 2d numpy array A (the trasition matrix) hint: 4x4 matrix

# TODO: make a 2d numpy array B (the control input matrix) hint; 4x1  matrix

# TODO: make a 2d numpy array u (the control vector) hint: 2 accelerations since its 2D

# keep this the same since we just need to change the matrices to mess with the dimensions
for i in range(100):
    Bu = B.dot(u)
    X = A.dot(X) + Bu
    print("X-Position:", X[0][0], "X-Velocity:", X[2][0])
    print("Y-Position:", X[1][0], "Y-Velocity:", X[3][0])
    print()