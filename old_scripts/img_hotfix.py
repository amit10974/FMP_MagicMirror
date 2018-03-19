#Code by Reday Yahya
#23/02/2018
#Facial Landmark detection using OpenCV, DLIB with added help of imageutilities by pyimageresearch
#IMG hotfix, Fixes image input for accurate results

#Packages needed (IMUTILS by pyimageresearch to install = pip install imutils)
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import numpy as np
import argparse
import imutils
import dlib
import cv2

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
fa = FaceAligner(predictor, desiredFaceWidth=256)

#Load Input
al_image = cv2.imread(args["image"])
al_image = imutils.resize(al_image, width = 800)
al_gray = cv2.cvtColor(al_image, cv2.COLOR_BGR2GRAY)
al_rects = detector(al_gray, 2)

# loop over the face detections
for rect in al_rects:
	
	#Format Conversion DLIB and openCV
	(x, y, w, h) = rect_to_bb(rect)
	faceAligned = fa.align(al_image, al_gray, rect)
 
	# display the output image 
	cv2.imshow("Aligned", faceAligned)
	cv2.waitKey(0)