# you will need to watch until video 15 for this problem
import numpy as np 
# imagine a missile is launching to the north east with acceleration
# Resource: https://www.programiz.com/python-programming/matrix

# x, y, xv, yv
X = np.array([  [10],
                [50],
                [1],
                [1] ])

t = 1
A = np.array([  [1, 0, t, 0],
                [0, 1, 0, t],
                [0, 0, 1, 0],
                [0, 0, 0, 1]  ])

g = -9.8
u = np.array([  [9],
                [3] ])

B = np.array([  [0.5 * t**2, 0],
                [0, 0.5 * t**2],
                [t, 0],
                [0, t]])



for i in range(100):
    Bu = B.dot(u)
    X = A.dot(X) + Bu
    print("X-Position:", X[0][0], "X-Velocity:", X[2][0])
    print("Y-Position:", X[1][0], "Y-Velocity:", X[3][0])
    print()






