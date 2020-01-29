from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# print(lStart)
# print(lEnd)
# print(rStart)
# print(rEnd)
img=cv2.imread('E:\\projectImplementation\\projectFiles\\frames\\att0.jpg')
image = imutils.resize(img, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imgg=image.copy()
# detect faces in the grayscale image
rects = detector(gray, 1)
for rect in rects:
    shape = predictor(gray,rect)
    shape = face_utils.shape_to_np(shape)
    l=shape[lStart:lEnd]
    r=shape[rStart:rEnd]
    imgag=imgg[l[1][1]-40:l[4][1]+40,l[0][0]-20:l[3][0]+20]
    cv2.imshow("image",imgag)
    cv2.waitKey(0)
    imgag1=imgg[r[5][1]-50:r[2][1]+50,r[0][0]-20:r[3][0]+20]
    cv2.imshow("image",imgag1)
    cv2.waitKey(0)
    # print(l[0][0])
