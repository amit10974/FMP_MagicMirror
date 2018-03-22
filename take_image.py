from picamera import PiCamera
from time import sleep

camera = PiCamera()

def takeIMG():
    camera.resolution = (1080, 1920)
    camera.start_preview()
    camera.hflip = True
    camera.vflip = True
    sleep(10)
    camera.capture('Material/user/user.jpg')
    camera.stop_preview()
	
