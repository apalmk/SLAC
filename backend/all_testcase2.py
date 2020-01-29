from random import shuffle
from glob import glob
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import PIL.Image as Image
import numpy as np
from keras.models import load_model
import time
from face_recognition1 import find_id
from model import create_model
import os
from image_subtraction import frsub
from side_face_distraction import sideface
from EmotionDetection import find_emo
from eye_detect_recog_final import eye_ext
from face_recognition1 import find_id

start=time.time()
from align import AlignDlib


alignment = AlignDlib('models/landmarks.dat')
haar_face_cascade = cv2.CascadeClassifier('haar_profile_face.xml')
eye_cascade_left= cv2.CascadeClassifier("E:\\projectImplementation\\projectFiles\\left_eye_haar.xml")
trainedModel = load_model('my-model1-20190419-230910.h5')

abhishek1 = np.load('abhishek_sideface.npy')
abhishek2 = np.load('abhishek_sideface1.npy')
aman1 = np.load('aman_sideface1.npy')
aman2 = np.load('aman_sideface2.npy')

def load_image(path):
    img = cv2.imread(path, 1)
    im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return im

i=frsub()
i=i+3
aman_att=[]
abhishek_att=[]
abhi_emotion=np.ones(i-1).astype(int)*(-1)
aman_emotion=np.ones(i-1).astype(int)*(-1)
aman_emotion=list(aman_emotion)
abhi_emotion=list(abhi_emotion)
aman_att=list(np.zeros(i-1).astype(int))
abhi_att=list(np.zeros(i-1).astype(int))
li=[52,53,54,55,56,57,58,59,60]
side_face_aman=[]
side_face_abhi=[]

while i<= 112:
    file="E:\\projectImplementation\\projectFiles\\frames\\testcase2\\frame_"+str(i)+".jpg"
    img=load_image(file)
    imgg=cv2.imread(file)
    print(file)
    abhi_flag = 0
    aman_flag = 0
    aman_emo_flag = -1
    abhi_emo_flag = -1
    if i in li:
        name=sideface(imgg,haar_face_cascade,abhishek1,abhishek2,aman1,aman2)
        if "Abhishek" in name:
            abhi_flag=1
            side_face_abhi.append(i)
            abhi_emo_flag=0
        if "Aman" in name:
            aman_flag=1
            side_face_aman.append(i)
            aman_emo_flag=0


    else:
        bb = alignment.getAllFaceBoundingBoxes(img)
        N = len(bb)
        for j in range(N):
            img1 = imgg[bb[j].top():bb[j].bottom(), bb[j].left():bb[j].right()]
            # img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
            print("face ",j)

            im_aligned = alignment.align(96, img, bb[j], landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)
            im_aligned = cv2.cvtColor(im_aligned, cv2.COLOR_RGB2BGR)
            name = find_id(im_aligned)
            if name == "Abhishek":
                abhi_flag = 1
                abhi_emo_flag = find_emo(img1)
                if abhi_emo_flag == 0:
                    es1 = eye_ext(img1, trainedModel, eye_cascade_left)
                    if es1 == 'closed':
                        abhi_flag = 0
                print(name)

            elif name == "Aman":
                if aman_flag == 1:
                    break

                aman_flag = 1
                print(name)
                aman_emo_flag = find_emo(img1)
                if aman_emo_flag == 0:
                    es2 = eye_ext(img1, trainedModel, eye_cascade_left)
                    if es2 == 'closed':
                        aman_flag = 0

    if abhi_flag == 1 and aman_flag == 0:
        abhi_att.append(1)
        aman_att.append(0)
        abhi_emotion.append(abhi_emo_flag)
        aman_emotion.append(-1)
    if aman_flag == 1 and abhi_flag == 0:
        abhi_att.append(0)
        aman_emotion.append(aman_emo_flag)
        aman_att.append(1)
        abhi_emotion.append(-1)
    if aman_flag == 0 and abhi_flag == 0:
        aman_att.append(0)
        abhi_att.append(0)
        abhi_emotion.append(-1)
        aman_emotion.append(-1)
    if abhi_flag == 1 and aman_flag == 1:
        abhi_att.append(1)
        aman_att.append(1)
        abhi_emotion.append(abhi_emo_flag)
        aman_emotion.append(aman_emo_flag)

    i = i + 1

np.save('abhishek_attendance_tc2.npy',abhi_att)
np.save('aman_attendance_tc2.npy',aman_att)
np.save('aman_sideface_tc2.npy',side_face_aman)
np.save('abhishek_sideface_tc2.npy',side_face_abhi)
np.save('aman_emotion_tc2',aman_emotion)
np.save('abhishek_emotion_tc2',abhi_emotion)
end=time.time()
# print(side_face_abhi)
# print(side_face_aman)
print("time taken in seconds",end-start)