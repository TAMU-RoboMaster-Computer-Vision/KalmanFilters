# you will need to watch until video 9 for this problem
# this is the same as the temperature problem except it gets you used to using matrices
import numpy as np # make sure to install numpy throught terminal with the command "pip install numpy"

X = np.array([  [1],
                [1] ])

t = 1
A = np.array([  [1, t],
                [0, 1]  ])

for i in range(100):
    X = A.dot(X)
    print("Y-Position:", X[0][0], "Y-Velocity:", X[1][0])
