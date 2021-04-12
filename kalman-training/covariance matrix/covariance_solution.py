import numpy as np 
# watch video 21, 22, and 23 for this

# first column is math, second column in physics, third column is  (grades for different students)
A = np.array(  [[90, 80, 40],
                [90, 60, 80],
                [60, 50, 70],
                [30, 40, 70],
                [30, 20, 90]])

# shows the average and total scores for information (matrices not used in calculations)
total_scores = np.array([300,250,350])
average_scores = np.array([60, 50, 70])

# create a 5x5 matrix of 1s to calculate totals for columns later
ones = np.ones((5,5))

# this is the equation to find the deviation matrix
a = ones.dot(A)
a = a*(1/5)
a = A - a
print(a)
# this is the covariance matrix
c = a.transpose().dot(a)
print(c)