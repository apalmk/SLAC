import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from model import create_model
import cv2
import numpy as np
import PIL.Image as Image
import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)


# anjani = np.load('anjani.npy')
aman = np.load('aman_final.npy')
# rapaka= np.load('rapaka.npy')
amany = np.load('aman_yawn.npy')
abhi= np.load('abhishek_final.npy')
# hemanth = np.load('hemanth.npy')
# subham = np.load('subham.npy')
# vivek = np.load('vivek.npy')

nn4_small2_pretrained = create_model()
nn4_small2_pretrained.load_weights('nn4.small2.v1.h5')

def load_image(path):
    img = cv2.imread(path, 1)
    im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return im

img=load_image('E:\\projectImplementation\\projectFiles\\frames\\face2_aligned\\frame153.jpg')

def find_id(img):
    img = (img / 255.).astype(np.float32)
    img=np.expand_dims(img, axis=0)
    embedded = nn4_small2_pretrained.predict(img)[0]
    distances = []
    # distances.append(np.linalg.norm(embedded - anjani))
    distances.append(np.linalg.norm(embedded - abhi))
    # distances.append(np.linalg.norm(embedded - subham))
    # distances.append(np.linalg.norm(embedded - rapaka))
    # distances.append(np.linalg.norm(embedded - hemanth))
    distances.append(np.linalg.norm(embedded - aman))
    distances.append(np.linalg.norm(embedded - amany))
    fin = min(distances)
    if (fin == distances[0]):
        return "Abhishek"
    if (fin == distances[1]):
        return "Aman"
    if (fin == distances[2]):
        return "amany"
# name=find_id(img)
# print(name)

