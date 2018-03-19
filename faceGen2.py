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
import numpy as np
import argparse
import imutils
import dlib
import cv2

ap = argparse.ArgumentParser()

#Path to Image we want to use to analyse (can use live feed too)
ap.add_argument("-i", "--image", required = True,
help = "path to input image")

args = vars(ap.parse_args())

#DLIB face detectore with facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("facerec.dat")
fa = FaceAligner(predictor, desiredFaceWidth=256)

#Load Input
al_image = cv2.imread(args["image"])
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