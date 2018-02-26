#Code by Reday Yahya
#02/02/2018
#Facial Landmark detection using OpenCV, DLIB with added help of imageutilities by pyimageresearch

#Packages needed (IMUTILS by pyimageresearch to install = pip install imutils)
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

#Cunstructing the argument parser for CL
ap = argparse.ArgumentParser()

#DLIB's trained facial Landmark detector
ap.add_argument("-p", "--shape-predictor", required = True,
    help = "path to Facial landmark predictor")

#Path to Image we want to use to analyse (can use live feed too)
ap.add_argument("-i", "--image", required = True,
    help = "path to input image")

args = vars(ap.parse_args())

#DLIB face detectore with facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

#Detect face with openCV
image = cv2.imread(args["image"])
image = imutils.resize(image, width = 500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rects = detector(gray, 1)

#Getting the right region for the face
for (i, rect) in enumerate(rects):
	shape = predictor(gray, rect)
	shape = face_utils.shape_to_np(shape)
	
    #Converting DLIB's rectange to OpenCV style
	(x, y, w, h) = face_utils.rect_to_bb(rect)
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #Looping over the coordinates for the facial landmarks and display them on image
	for (x, y) in shape:
		cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

	np.savetxt("output"), shape)

#Output
cv2.imshow("Output", image)
cv2.waitKey(0)