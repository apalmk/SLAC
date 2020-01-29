import cv2
import math
#This project is created as a capstone implementation for my university
videoname = "E://projectImplementation//projectFiles//frames//FYP//test_case2_patch.MOV"
__author__="Anjani Prasad"
imagesloc = "E://projectImplementation//projectFiles//frames//testcase2_patch//"
vdoobject = cv2.VideoCapture(videoname)
fr = vdoobject.get(5) #gets the frame rate of the video
print(fr)
success = 1
frameCount = vdoobject.get(cv2.CAP_PROP_FRAME_COUNT)
print(frameCount)
frc=math.floor(fr)
print(frc)
duration=math.floor(frameCount/fr)
print(duration)
x=0
y=0
while x<=duration and success:
    # vidObj object calls read
    # function extract frames
    frameId = vdoobject.get(1)
    success, image = vdoobject.read()
    # print(success)
    y=y+1
    if (frameId % frc == 0): #if fr is 24fps, 24rth, 48th, 72 etc will be extracted
        filename = imagesloc + "image_" + str(int(x)) + ".jpg"
        cv2.imwrite(filename, image)
        x = x + 1
print("last frame processed",frameId)
print(x)
print(y)
vdoobject.release()
print("Done!")