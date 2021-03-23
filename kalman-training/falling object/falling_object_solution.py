# you will need to watch until video 11 for this problem
# this is the same as the temperature problem except it gets you used to using matrices
import numpy as np # make sure to install numpy throught terminal with the command "pip install numpy"

X = np.array([  [500],
                [0] ])

t = 1
A = np.array([  [1, t],
                [0, 1]  ])
g = -9.8
u = np.array([g])

B = np.array([  [.5 * (t**2)],
                [t]])


for i in range(10):
    Bu = B * u
    X = A.dot(X) + Bu
    print("Y-Position:", X[0][0], "Y-Velocity:", X[1][0])
