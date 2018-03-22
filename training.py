#Code by Reday Yahya
#09/03/2018
#Facial Landmark detection using OpenCV, DLIB with added help of imageutilities by pyimageresearch
#Document for Statistical Analysis and Data Gathering
#Using Standard Deviation and Variance

#Packages
from combo import getFaceCord
import os
import statistics
import numpy as np

#Source Location
source_img = os.listdir("Material/attr/")
source_path = "Material/attr/"
ctr = "0"

#Collective Array of Coordinates from all Images distrubuted
train_array = []

#Loops through Images in Analysis Material Folder for attractive Females and passes it trhough getFaceCord()
for x in source_img:
    print(x)
    train_array.append(getFaceCord(source_path + x, "output_results/output.txt"))

#Taking gathered Coordinates and sorting them for Statistical Analysis Calculation
x_arr = []
y_arr = []
sub_length = len(train_array[0])

for i in range(sub_length):
    tmp_x = []
    tmp_y = []
    for array in train_array:
        tmp_x.append(array[i][0])
        tmp_y.append(array[i][1])
    x_arr.append(tmp_x)
    y_arr.append(tmp_y)
    
#Debug Output of Sorted Coordinate array. Sorted for the facial Landmarks Markup 68 locations
print("")
print("X Array")
print(x_arr)
print("")
print("Y Array")
print(y_arr)


#Collection of Learned Data
average_mean_x = []
average_mean_y = []
average_sd_x = []
average_sd_y = []
average_vari_x = []
average_vari_y = []

#Looping through Values for Calculations
for x in x_arr:
	average_sd_x.append(statistics.stdev(x))
	average_mean_x.append(statistics.mean(x))
	average_vari_x.append(statistics.variance(x))

#Looping through Values for Calculations
for x in y_arr:
	average_sd_y.append(statistics.stdev(x))
	average_mean_y.append(statistics.mean(x))
	average_vari_y.append(statistics.variance(x))

#Output Documents X
np.savetxt("output_results/STDEV_X.txt", average_sd_x, fmt='%1.3f', delimiter='\t')
np.savetxt("output_results/MEAN_X.txt", average_mean_x, fmt='%1.3f', delimiter='\t')
np.savetxt("output_results/VARI_X.txt", average_vari_x, fmt='%1.3f', delimiter='\t')

#Output Documents Y
np.savetxt("output_results/STDEV_Y.txt", average_sd_y, fmt='%1.3f', delimiter='\t')
np.savetxt("output_results/MEAN_Y.txt", average_mean_y, fmt='%1.3f', delimiter='\t')
np.savetxt("output_results/VARI_Y.txt", average_vari_y, fmt='%1.3f', delimiter='\t')


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