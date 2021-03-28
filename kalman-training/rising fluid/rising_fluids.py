# you will need to watch until video 9 for this problem
# this is the same as the temperature problem except it gets you used to using matrices
import np as np
import numpy as np
# make sure to install numpy throught terminal with the command "pip install numpy"

# Resource: https://www.programiz.com/python-programming/matrix

# TODO: Create an X Matrix using numpy

X=np.array([[1],
            [3]])
print(X)
# TODO: Create an A Matrix using numpy
t=1
A= np.array([[1,t],
             [0,1]])
print(A)
for i in range(100):
    # TODO: Calculate X(k) using A and X(k-1)
    X=A.dot(X)
    print("Y-Position:", X[0][0], "Y-Velocity:", X[1][0]) # uncomment this line and you can see the pattern of your Y-Position change
    print("good luck") # you can delete this line (just for code compilation)