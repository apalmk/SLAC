import cv2
from model import create_model
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import time

# start=time.time()

# haar_face_cascade = cv2.CascadeClassifier('haar_profile_face.xml')
# # imagesloc = "E:\\projectImplementation\\projectFiles\\frames\\sidefaces\\"
# # lbp_face_cascade = cv2.CascadeClassifier('lbpcascade_profileface.xml')
#
# anjani1 = np.load('abhishek_sideface.npy')
# anjani2 = np.load('abhishek_sideface1.npy')
# aman1 = np.load('aman_sideface1.npy')
# aman2 = np.load('aman_sideface2.npy')

# def findy(img,anjani1,anjani2,aman1,aman2):
#     nn4_small2_pretrained = create_model()
#     nn4_small2_pretrained.load_weights('nn4.small2.v1.h5')
#     img = (img / 255.).astype(np.float32)
#     img = np.expand_dims(img, axis=0)
#     embedded = nn4_small2_pretrained.predict(img)[0]
#     distances = []
#     distances.append(np.linalg.norm(embedded - anjani1))
#     distances.append(np.linalg.norm(embedded - anjani2))
#     distances.append(np.linalg.norm(embedded - aman1))
#     distances.append(np.linalg.norm(embedded - aman2))
#     # distances.append(np.linalg.norm(embedded - aman3))
#     # distances.append(np.linalg.norm(embedded - aman4))
#
#
#     fin = min(distances)
#     if (fin == distances[0]):
#         return "Abhishek"
#     if (fin == distances[1]):
#         return "Abhishek"
#     if (fin == distances[2]):
#         return "Aman"
#     if (fin == distances[3]):
#         return "Aman"
#     # if (fin == distances[4]):
#         # return "Aman"
#     # if (fin == distances[5]):
#         # return "Aman"


def sideface(test,haar_face_cascade,anjani1,anjani2,aman1,aman2):
    # test = cv2.imread(loc)
    gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
    faces = haar_face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30)
    )

    f=len(faces)
    print(f," faces found")
    # x1=1

    # faces1 = lbp_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    # f1=len(faces1)
    # print(len(faces1))

    clone=test.copy()
    clone1=test.copy()

    if(f==2):
        facess=[]
        for (x, y, w, h) in faces:
            name=""
            crop_img1 = clone[y-20:y+h+20, x-40:x+w+40]
            crop_img1 = cv2.resize(crop_img1, (96, 96), interpolation=cv2.INTER_AREA)
            nn4_small2_pretrained = create_model()
            nn4_small2_pretrained.load_weights('nn4.small2.v1.h5')
            img = (crop_img1 / 255.).astype(np.float32)
            img = np.expand_dims(img, axis=0)
            embedded = nn4_small2_pretrained.predict(img)[0]
            distances = []
            distances.append(np.linalg.norm(embedded - anjani1))
            distances.append(np.linalg.norm(embedded - anjani2))
            distances.append(np.linalg.norm(embedded - aman1))
            distances.append(np.linalg.norm(embedded - aman2))

            fin = min(distances)
            if (fin == distances[0]):
                name="Abhishek"
            if (fin == distances[1]):
                name="Abhishek"
            if (fin == distances[2]):
                name="Aman"
            if (fin == distances[3]):
                name="Aman"
            facess.append(name)
        return facess

# elif(f1==1 and f==0):
#     for (x, y, w, h) in faces1:
#         cv2.rectangle(test, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         crop_img2 = clone1[y-20:y+h+20, x-40:x+w+40]
#         # print("not called")
#         # filename=imagesloc + "/sidefacell_aman1" + str(int(x1)) + "_frame1.jpg"
#         # cv2.imwrite(filename, crop_img)
#         crop_img2 = cv2.resize(crop_img2, (96, 96), interpolation=cv2.INTER_AREA)
#         name=findy(crop_img2)
#         print(name)
#
# elif(f>1 and f1==1):
#     # i=0
#     for (x, y, w, h) in faces:
#         cv2.rectangle(test, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         crop_img1 = clone[y-20:y+h+20, x-40:x+w+40]
#         # print("not called")
#         crop_img1 = cv2.resize(crop_img1, (96, 96), interpolation=cv2.INTER_AREA)
#         # cv2.imwrite("frames/sideface_"+str(i)+".jpg",crop_img1)
#         name = findy(crop_img1)
#         # i=i+1
#         print(name)
#
# if(f==1 and f1>1):
#     for (x, y, w, h) in faces:
#         cv2.rectangle(test, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         crop_img1 = clone[y-20:y+h+20, x-40:x+w+40]
#         # print("not called")
#         crop_img1 = cv2.resize(crop_img1, (96, 96), interpolation=cv2.INTER_AREA)
#         name = findy(crop_img1)
#         print(name)
#
# if(f==1 and f1==1):
#     for (x, y, w, h) in faces:
#         cv2.rectangle(test, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         crop_img1 = clone[y-10:y+h+10, x-20:x+w+20]
#         # print("not called")
#         crop_img1 = cv2.resize(crop_img1, (96, 96), interpolation=cv2.INTER_AREA)
#         name = findy(crop_img1)
#         print(name)
#
# if(f>1 and f1>1):
#     i=0
#     for (x, y, w, h) in faces:
#         cv2.rectangle(test, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         crop_img1 = clone[y-20:y+h+20, x-40:x+w+40]
#         # print("not called")
#         crop_img1 = cv2.resize(crop_img1, (96, 96), interpolation=cv2.INTER_AREA)
#         i=i+1
#         name = findy(crop_img1)
#         print(name)
#
# if(f==0 and f1==0):
#     #add return none statement here
#     print("none")

# i=52
# while i<=60:
#     name=sideface("E:\\projectImplementation\\projectFiles\\frames\\testcase2\\frame_"+str(i)+".jpg",haar_face_cascade,anjani1,anjani2,aman1,aman2)
#     print(name)
#     i=i+1
# end = time.time()
# print(end-start)
# cv2.imshow("Faces found", test)
# cv2.waitKey(0)