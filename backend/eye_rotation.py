#check which values are bigger of x1 and x2 and of y1 and y2
import cv2
import math
import numpy as np
eye_cascade = cv2.CascadeClassifier("E:\\projectImplementation\\projectFiles\\eye.xml")
imagesloc = "E:\\projectImplementation\\projectFiles\\frames"

imagePath = "E:\\projectImplementation\\projectFiles\\frames\\face_2_frame1.jpg"
# cascPath = "C:\\Users\\ANJANIPRASAD\\PycharmProjects\\Sin\\haarcascade_face_detect.xml"
eye_cascade_right= cv2.CascadeClassifier("E:\\projectImplementation\\projectFiles\\right_eye_haar.xml")
eye_cascade_left= cv2.CascadeClassifier("E:\\projectImplementation\\projectFiles\\left_eye_haar.xml")
eye_cascade_tree= cv2.CascadeClassifier("E:\\projectImplementation\\projectFiles\\haarcascade_eye_tree_glasses.xml")

image = cv2.imread(imagePath)
image1 = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# (thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

eyes = eye_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=10)
print("found {0} eyes".format(len(eyes)))
eyes2= eye_cascade_left.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=10)
print("found {0} eyes".format(len(eyes2)))
eyes3= eye_cascade_right.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=10)
print("found {0} eyes".format(len(eyes3)))
eyes4= eye_cascade_tree.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
print("found {0} eyes".format(len(eyes4)))

pos=[]
x1=1
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    x=ex+(ew/2)
    y=ey+(eh/2)
    # x=ex
    # y=ey
    pos.append((x,y))
    crop_eye=image1[ey:ey+eh, ex:ex+ew]
    filename = imagesloc + "/eye_image_" + str(int(x1)) + "_face1.jpg"
    cv2.imwrite(filename, crop_eye)
    x1=x1+1
    # break
    #     for (ex,ey,ew,eh) in eyes:
    #         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #
    # cv2.imshow('img',img)

cv2.imwrite(imagesloc+"/facee.jpg", image)
cv2.imshow('img',image)
cv2.waitKey(0)


print(pos)
#execute only if the no of eyes found are 2
# Head only had 180 degress of freedom of motion the left eye's x co-ordinate will always be lower than the right eye
if(len(eyes)==2):
    if((pos[0][0]<pos[1][0])):
        leftx=pos[1][0]
        rightx=pos[0][0]
        lefty=pos[1][1]
        righty=pos[0][1]
        deg = math.atan((lefty - righty) / (leftx - rightx))
        deg=deg*180/math.pi
        print("the angle is ", deg)

    else:
        leftx=pos[0][0]
        rightx=pos[1][0]
        lefty=pos[0][1]
        righty=pos[1][1]
        deg = math.atan((lefty - righty) / (leftx - rightx))
        deg=deg*180/math.pi
        print("the angle is ", deg)


else:
    print("It's not a proper face or single face is not detected")

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

angle1=deg
img1=rotateImage(image1,angle1)
cv2.imshow('image',img1)
filename = imagesloc + "/image_output_frame1.jpg"
cv2.imwrite(filename,img1)
k = cv2.waitKey(0)
