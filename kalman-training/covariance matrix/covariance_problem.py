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

# create a 5x5 matrix of 1s to calculate totals for columns later (hint: numpy has a function for this)

# calculate the deviation matrix using numpy functions and the equation from video 23
# the final result should be :
# [[ 30.  30. -30.]
#  [ 30.  10.  10.]
#  [  0.   0.   0.]
#  [-30. -10.   0.]
#  [-30. -30.  20.]]

# calculate the covariance matrix 
# the final results should be : 
# [[ 3600.  2400. -1200.]
#  [ 2400.  2000. -1400.]
#  [-1200. -1400.  1400.]]