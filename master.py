#Code by Reday Yahya
#23/02/2018
#Facial Landmark detection using OpenCV, DLIB with added help of imageutilities by pyimageresearch
#Master File

#usage python faceGen2.py --image Material/user/

#Packages needed (IMUTILS by pyimageresearch to install = pip install imutils)
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
from imutils import face_utils
from picamera import PiCamera
from time import sleep
import os
import statistics
import numpy as np
import imutils
import dlib
import cv2

#This bit is to take Images and to set Image
camera = PiCamera()
camera.start_preview()
sleep(10) #timer for how long until image is taken
camera.capture('/Material/user/image.jpg')
camera.stop_preview()
source_image = "/Material/user/image.jpg"

#DLIB face detectore with facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("facerec.dat")
fa = FaceAligner(predictor, desiredFaceWidth=256)

#Load Input
al_image = cv2.imread(source_image)
al_image = imutils.resize(al_image, width = 800)
al_gray = cv2.cvtColor(al_image, cv2.COLOR_BGR2GRAY)
al_rects = detector(al_gray, 2)

# loop over the face detections
for rect in al_rects:
	
	#Format Conversion DLIB and openCV, store new image in faceAligned
	(x, y, w, h) = rect_to_bb(rect)
	faceAligned = fa.align(al_image, al_gray, rect)
 

#now that we have the fixed image, lets get our facial landmarks
image = faceAligned
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rects = detector(gray, 1)

#Getting the right region for the face
for (i, rect) in enumerate(rects):
	shape = predictor(gray, rect)
	shape = face_utils.shape_to_np(shape)

    #Looping over the coordinates for the facial landmarks and display them on image
	for (x, y) in shape:
		cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

#Output
np.savetxt("output_results/output.txt", shape, fmt='%10.f', delimiter='\t')
y = np.loadtxt("output_results/output.txt")
print(y)

#Standard Deviation Test

cv2.imshow("Output", image)

cv2.waitKey(0)

#How many standard deviations from the mean counts as anomalous
numStanDeviations = 1.6

#X Data
average_mean_x = []
average_sd_x = []
average_vari_x = []

#Y Data
average_mean_y = []
average_sd_y = []
average_vari_y = []

#shape coordinates
# shape = []
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
# shape = np.loadtxt("output_results/output.txt")

for (x, y) in shape:
    X_CORD.append(x)
    Y_CORD.append(y)

#Var for loop
pos = 0
reps = len(X_CORD)
anomalousPoints = 0

#looping through for difference X
while pos < reps:
	z = 0
	if (average_sd_x[pos] == 0):
		x_diff.append(z)
		pos = pos + 1
	else:
		z = (X_CORD[pos] - average_mean_x[pos]) / average_sd_x[pos]
		pos = pos + 1
		x_diff.append(z)

	#Calculated number of SDs from mean
	#Make this greater than zero
	if (z < 0):
		z = z* -1	
		
	#Is this value more than our threshold in terms of SDs
	#print("Z: " + str(z) + " num SDs " + str(numStanDeviations))
	if (z > numStanDeviations):
		anomalousPoints = anomalousPoints + 1
		# cordIndex = X_CORD.index(X_CORD[pos]) - 1
		# print ("Location of coordinate " + str(cordIndex)  + " Coordinate: " + str(X_CORD[pos]))

#reseting loop counter
pos = 0

#looping through for difference X
while pos < reps:
	z = 0
	if (average_sd_y[pos] == 0):
		y_diff.append(z)
		pos = pos + 1
	else:
		z = (Y_CORD[pos] - average_mean_y[pos]) / average_sd_y[pos]
		pos = pos + 1
		y_diff.append(z)
	
	#Calculated number of SDs from mean
	#Make this greater than zero
	if (z < 0):
		z = z* -1	
		
	#Is this value more than our threshold in terms of SDs
	if (z > numStanDeviations):
		anomalousPoints = anomalousPoints + 1
		# cordIndex = Y_CORD.index(Y_CORD[pos])
		# print ("Location of coordinate " + str(cordIndex)  + " Coordinate: " + str(Y_CORD[pos]))
			
#Output anomalous point count	
print("Anomalous point count: " + str(anomalousPoints))	

#Calculation for difference procentage

FINALVAL = 100 - (anomalousPoints * 100 / 136)
print()
print()
print()
print("Hmmmm I shall see....")
print(".....You are only " + str(FINALVAL) + " % close to the fairest in the land")
print()
print()
print()

# np.savetxt("output_results/Measure_X.txt", x_diff, fmt='%1.3f', delimiter='\t')
# np.savetxt("output_results/Measure_Y.txt", y_diff, fmt='%1.3f', delimiter='\t')

#Output
# print("")
# print("STDEV for X coordinates")
# print(average_sd_x)

# print(" ")
# print("Mean for X coordinates")
# print(average_mean_x)

# print(" ")
# print("variance for X coordinates")
# print(average_vari_x)

# print(" ")
# print("STDEV for Y coordinates")
# print(average_sd_y)

# print(" ")
# print("Mean for Y coordinates")
# print(average_mean_y)

# print(" ")
# print("variance for Y coordinates")
# print(average_vari_y)

# print(" ")
# print("Coordinate Array")
# print(shape)

# print(" ")
# print("X Array")
# print(X_CORD)

# print(" ")
# print("Y Array")
# print(Y_CORD)

# print(" ")
# print("difference Array X")
# print(x_diff)

# print(" ")
# print("difference Array Y")
# print(y_diff)
