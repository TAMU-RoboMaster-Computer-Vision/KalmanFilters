import random

# these are the initial values from the videos
true_temp = 72.0
estimate = 68.0
estimate_E = 2.0
measurement_E = 4.0
kalman_gain = 0.0

# this fills the 
temperatures = [75, 71, 70, 74]
for i in range(100):
    temperatures.append(random.randint(68,76))
    print(temperatures)

# modify this for loop to fit in the kalman equations to approximate the temperature
for i in temperatures:
    print("hello") # delete this line and add your calculations
    # print("estimate:", estimate, "error in estimate:", estimate_E, "kalman gain:", kalman_gain) # 