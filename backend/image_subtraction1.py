import cv2
import os
import numpy as np

def frsub():
    dir="E:\\projectImplementation\\projectFiles\\frames\\testcase2"
    j=1
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            im1 = cv2.imread(dir + '/frame_'+str(j)+'.jpg')
            im2= cv2.imread(dir+'/frame_'+str(j+1)+'.jpg')
            if im1.shape==im2.shape:
                diff=cv2.subtract(im1,im2)
                b,g,r=cv2.split(diff)
                if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
                    j=j+1
                    continue
                else:
                    print('Starting from the frame '+str(j)+' as the consecutive frames are different')
                    return j
                    break
frsub()