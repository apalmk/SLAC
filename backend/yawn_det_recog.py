import cv2
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# import PIL.Image as Image
import numpy as np
from model import create_model
import time
# from keras import backend as K
# import tensorflow as tf
# from align import AlignDlib
# from keras import backend as K

start=time.time()
def load_image(path):
    img = cv2.imread(path, 1)
    im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return im

def find_yawn(im_aligned):
    # alignment = AlignDlib('models/landmarks.dat')

    # img= load_image('E:\\projectImplementation\\projectFiles\\frames\\face2\\frame52.jpg')

    # bb = alignment.getLargestFaceBoundingBox(img)

    # im_aligned = alignment.align(96, img, bb, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)

    aman = np.load('aman_final.npy')
    # abhi= np.load('abhishek_final.npy')
    aman_yawn=np.load('aman_yawn.npy')
    nn4_small2_pretrained = create_model()
    nn4_small2_pretrained.load_weights('nn4.small2.v1.h5')
    im_aligned = (im_aligned / 255.).astype(np.float32)
    im_aligned=np.expand_dims(im_aligned, axis=0)
    embedded = nn4_small2_pretrained.predict(im_aligned)[0]
# print(embedded)
#     tf.keras.backend.clear_session()
#     K.clear_session()
    distances=[]
    # distances.append(np.linalg.norm(embedded-abhi))
    distances.append(np.linalg.norm(embedded-aman))
    distances.append(np.linalg.norm(embedded-aman_yawn))
    # print(distances)
    fin=min(distances)
    # if (fin == distances[0]):
    #     return "Abhishek"
    if (fin == distances[0]):
        return "no"
    if(fin==distances[1]):
        return "yes"

# imgg=load_image("E:\\projectImplementation\\projectFiles\\frames\\face1_aligned\\frame51.jpg")
# value=find_yawn(imgg)
# print(value)
# end=time.time()
# print(end-start)