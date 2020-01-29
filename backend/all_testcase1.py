from random import shuffle
from glob import glob
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import PIL.Image as Image
import numpy as np
from EmotionDetection import find_emo
import time
from keras.models import load_model
from face_recognition1 import find_id
from eye_detect_recog_final import eye_ext
from model import create_model
import os

start=time.time()
from align import AlignDlib

def sortKeyFunc(s):
    return int(os.path.basename(s)[6:-4])

files = sorted(glob(r"E:\projectImplementation\projectFiles\frames\testcase1\*.jpg"))
files.sort(key=sortKeyFunc)
# print(os.path.basename(files[1])[6:-4])
alignment = AlignDlib('models/landmarks.dat')
eye_cascade_left= cv2.CascadeClassifier("E:\\projectImplementation\\projectFiles\\left_eye_haar.xml")
trainedModel = load_model('my-model1-20190419-230910.h5')

def load_image(path):
    img = cv2.imread(path, 1)
    im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return im

i=1
abhi_att=[]
aman_att=[]
anomaly=[]
abhi_emotion=[]
aman_emotion=[]
for file in files:
    img=load_image(file)
    imgg=cv2.imread(file)
    print(file)
    abhi_flag = 0
    aman_flag = 0
    aman_emo_flag=-1
    abhi_emo_flag=-1
    y_flag=0
    bb = alignment.getAllFaceBoundingBoxes(img)
    N = len(bb)
    for j in range(N):
        if N>=3:
            abhi_flag=1
            aman_flag=1
            anomaly.append(i)
            aman_emo_flag=0
            abhi_emo_flag=0
            break
        else:
            img1 = imgg[bb[j].top():bb[j].bottom(), bb[j].left():bb[j].right()]
            # img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
            print("face ",j)
            # cv2.imwrite('E:\\projectImplementation\\projectFiles\\frames\\face' + str(j+1) +'\\frame'+ str(i)+'.jpg', img1)
            im_aligned = alignment.align(96, img, bb[j], landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)
            # im_aligned = cv2.cvtColor(im_aligned, cv2.COLOR_RGB2BGR)
            name=find_id(im_aligned)
            if name=="Abhishek":
                abhi_flag=1
                abhi_emo_flag= find_emo(img1)
                if abhi_emo_flag==0:
                    es1=eye_ext(img1,trainedModel,eye_cascade_left)
                    if es1=='closed':
                        abhi_flag=0
                print(name)

            elif name=="amany":
                aman_flag=1
                y_flag=1
                print(name)
                aman_emotion.append(5)

            elif name=="Aman":
                if aman_flag==1:
                    break

                aman_flag=1
                print(name)
                aman_emo_flag=find_emo(img1)
                if aman_emo_flag==0:
                    es2=eye_ext(img1,trainedModel,eye_cascade_left)
                    if es2=='closed':
                        aman_flag=0

    if abhi_flag==1 and aman_flag==0:
        abhi_att.append(1)
        aman_att.append(0)
        abhi_emotion.append(abhi_emo_flag)
        aman_emotion.append(-1)
    if aman_flag==1 and abhi_flag==0:
        abhi_att.append(0)
        if(y_flag!=1):
            aman_emotion.append(aman_emo_flag)
        aman_att.append(1)
        abhi_emotion.append(-1)
    if aman_flag==0 and abhi_flag==0:
        aman_att.append(0)
        abhi_att.append(0)
        abhi_emotion.append(-1)
        aman_emotion.append(-1)
    if abhi_flag==1 and aman_flag==1:
        abhi_att.append(1)
        aman_att.append(1)
        abhi_emotion.append(abhi_emo_flag)
        if y_flag!=1:
            aman_emotion.append(aman_emo_flag)


    i=i+1

np.save('new_abhishek_attendance_tc1.npy',abhi_att)
np.save('new_aman_attendance_tc1.npy',aman_att)
np.save('new_anomaly_presence_tc1.npy',anomaly)
np.save('new_aman_emotion_tc1',aman_emotion)
np.save('new_abhishek_emotion_tc1',abhi_emotion)
print('anomaly present at',anomaly)

end=time.time()
print("time taken in seconds",end-start)