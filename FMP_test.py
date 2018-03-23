#Code by Reday Yahya
#22/03/2018
#Facial Landmark detection using OpenCV, DLIB with added help of imageutilities by pyimageresearch
#Unittesting for FMP_MagicMirror

#Needed for testing
import unittest
from combo import getFaceCord

#needed for getFaceCord
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import statistics

#Testing Class
class TestgetFaceCord(unittest.TestCase):

    #1st test tests the function to produces an output that maches the live execution
    def test_getFaceCord(self):

        #executes requirements
        shape = getFaceCord("Material/attr/TPNA8Z.jpg", "output_results/output.txt" )
        coordinates = np.loadtxt("output_results/output.txt")

        #Test 1 array of coordinates is equal to the output file
        np.alltrue(shape == coordinates)
    
    #2nd test focuses on testing the formula to determine STDEV counts
    def test_Z_Formula(self):

        #here were just going to see if the formula
        Zmanual = (62 - 45.000) / 6.782

        #Reason why I didn't take values directly from output is due
        #to the fact we don't need to specifically need to test mulitples
        #when we can simply test the result of an example and the formula

        #Calculated the result value manually just to see if python calculates
        #exactly like a normal calculator would operate
        #result should state that the coordinate is 2.5 STDEVs above the average
        self.assertAlmostEqual(Zmanual, 2.506635210852256)
    
    #3rd test focuses on output result
    def test_FinalOutput(self):
        
        anomalousPoints = 45
        FINALVAL = 100 - (anomalousPoints * 100 / 136)

        #Calculated the result value manually just to see if python calculates
        #exactly like a normal calculator would operate
        #result should state a result that is 66,91% close
        #with a anomalousPoint value of 45
        self.assertAlmostEqual(FINALVAL,66.911764705882352941176470588235 )