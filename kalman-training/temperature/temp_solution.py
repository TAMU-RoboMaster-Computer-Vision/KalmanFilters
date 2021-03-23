import random


true_temp = 72.0
estimate = 68.0
estimate_E = 2.0
measurement_E = 4.0

temperatures = [75, 71, 70, 74]

for i in range(100):
    temperatures.append(random.randint(68,76))

print(temperatures)

for i in temperatures:
    kalman_gain = estimate_E / (estimate_E + measurement_E)
    estimate = estimate + kalman_gain * (i-estimate)
    estimate_E = (1-kalman_gain) * (estimate_E)
    print("estimate:", estimate, "error in estimate:", estimate_E, "kalman gain:", kalman_gain)