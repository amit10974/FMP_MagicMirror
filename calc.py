#Code by Reday Yahya
#14/03/2018
#Facial Landmark detection using OpenCV, DLIB with added help of imageutilities by pyimageresearch
#Document for Statistical Analysis and Data Gathering
#Test Calculation file

import os
import statistics
import numpy as np

#X Data
average_mean_x = []
average_sd_x = []
average_vari_x = []

#Y Data
average_mean_y = []
average_sd_y = []
average_vari_y = []

#shape coordinates
shape = []
X_CORD = []
Y_CORD = []

#Calculation output
x_diff = []
y_diff = []

#Load for X
average_mean_x = np.loadtxt("output_results/MEAN_X.txt")
average_sd_x = np.loadtxt("output_results/STDEV_X.txt")
average_vari_x = np.loadtxt("output_results/VARI_X.txt")

#Load for Y
average_mean_y = np.loadtxt("output_results/MEAN_Y.txt")
average_sd_y = np.loadtxt("output_results/STDEV_Y.txt")
average_vari_y = np.loadtxt("output_results/VARI_Y.txt")

#Load shape
shape = np.loadtxt("output_results/output.txt")

for (x, y) in shape:
    X_CORD.append(x)
    Y_CORD.append(y)

#Difference in Deviation against val
#Formula Z = (cordvalue - MEAN) / STDEV 
# for x in X_CORD:
#     for m in average_mean_x:
#         for sd in average_sd_x:
#             z = (x - m) / sd
#             x_diff.append(z)

pos = 0
reps = len(X_CORD)

while pos < reps:
    z = (X_CORD[pos] - average_mean_x[pos]) / average_sd_x[pos]
    pos = pos + 1
    x_diff.append(z)

pos = 0

while pos < reps:
    z = (Y_CORD[pos] - average_mean_y[pos]) / average_sd_y[pos]
    pos = pos + 1
    y_diff.append(z)

np.savetxt("output_results/Measure_X.txt", x_diff, fmt='%1.3f', delimiter='\t')
np.savetxt("output_results/Measure_Y.txt", y_diff, fmt='%1.3f', delimiter='\t')

#Output
print("")
print("STDEV for X coordinates")
print(average_sd_x)

print(" ")
print("Mean for X coordinates")
print(average_mean_x)

print(" ")
print("variance for X coordinates")
print(average_vari_x)

print(" ")
print("STDEV for Y coordinates")
print(average_sd_y)

print(" ")
print("Mean for Y coordinates")
print(average_mean_y)

print(" ")
print("variance for Y coordinates")
print(average_vari_y)

print(" ")
print("Coordinate Array")
print(shape)

print(" ")
print("X Array")
print(X_CORD)

print(" ")
print("Y Array")
print(Y_CORD)

print(" ")
print("difference Array X")
print(x_diff)

print(" ")
print("difference Array Y")
print(y_diff)
