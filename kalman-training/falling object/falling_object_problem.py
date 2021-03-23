# you will need to watch until video 11 for this problem
# this is the same as the temperature problem except it gets you used to using matrices
import numpy as np # make sure to install numpy throught terminal with the command "pip install numpy"

# Resource: https://www.programiz.com/python-programming/matrix

X = np.array([  [500],
                [0] ])

t = 1
A = np.array([  [1, t],
                [0, 1]  ])

g = -9.8
# TODO: Create a u Matrix using numpy

# TODO: Create a B Matrix using numpy


for i in range(100):
    # TODO: Calculate X(k) using A and X(k-1)

    # TODO: Calculate the X(k) by adding Bu

    #print("Y-Position:", X[0][0], "Y-Velocity:", X[1][0]) # uncomment this line and you can see the pattern of your Y-Position and Y-Velocity change
    print("good luck") # you can delete this line (just for code compilation) 


