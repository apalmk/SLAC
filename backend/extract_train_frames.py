import cv2
import math
#This project is created as a capstone implementation for my university
videoname = "ds1\\vdo\\Anjani_woglasses_tubelight.mp4"
__author__="Anjani Prasad"
imagesloc = "C:\\Users\\ANJANIPRASAD\\PycharmProjects\\Sin\\ds1\\Anjani4"
vdoobject = cv2.VideoCapture(videoname)
fr = vdoobject.get(5) #gets the frame rate of the video
print(fr)
success = 1
frameCount = vdoobject.get(cv2.CAP_PROP_FRAME_COUNT)
frc=math.floor(fr)
duration=math.floor(frameCount/fr)
print(duration)
x=1
while x<=duration and success:
    # vidObj object calls read
    # function extract frames
    frameId = vdoobject.get(1)
    success, image = vdoobject.read()

    if (frameId % frc == 0): #if fr is 24fps, 24rth, 48th, 72 etc will be extracted one by one
        filename = imagesloc + "/image_" + str(int(x)) + ".jpg";x=x+1
        cv2.imwrite(filename, image)
#

vdoobject.release()
print("Done!")