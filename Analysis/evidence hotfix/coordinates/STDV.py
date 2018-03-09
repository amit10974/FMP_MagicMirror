#Code by Reday Yahya
#06/03/2018
#Facial Landmark detection using OpenCV, DLIB with added help of imageutilities by pyimageresearch
#Standard Deviation Calculation

#Standard Deviation Test Bit
#Calculates Right Jawline for 3 woman

import statistics

#Data for 3 woman
Jaw_Line1_X = [40, 44, 54]
Jaw_Line1_Y = [81, 83, 93]
Jaw_Line2_X = [43, 44, 54]
Jaw_Line2_Y = [103, 106, 134]
Jaw_Line3_X = [47, 51, 58]
Jaw_Line3_Y = [125, 127, 135]
Jaw_Line4_X = [51, 54, 62]
Jaw_Line4_Y = [147, 149, 155]
Jaw_Line5_X = [60, 59, 70]
Jaw_Line5_Y = [168, 170, 173]
 

VARIA_Jaw_Line1_X =statistics.variance(Jaw_Line1_X)
MEAN_Jaw_Line1_X =statistics.mean(Jaw_Line1_X)
STDEV_Jaw_Line1_X = statistics.stdev(Jaw_Line1_X)
print(STDEV_Jaw_Line1_X)
print(MEAN_Jaw_Line1_X)
print(VARIA_Jaw_Line1_X)

# #Calculate Means
# Jaw_Line1_X_Mean = (40 + 44 + 54)/3
# Jaw_Line1_Y_Mean = (81 + 83 + 93)/3

# #Sample Variance
# Jaw_Line1_X_Sample_Variance = 4

# for i in range(len(Jaw_Line1_X)):
#     sample_temp1 = (Jaw_Line1_X[i] - Jaw_Line1_X_Mean) * 2
#     Jaw_Line1_X_Sample_Variance = sample_temp1 + Jaw_Line1_X_Sample_Variance

# print(Jaw_Line1_X_Sample_Variance)