import cv2
import cv2.face
# import glob as gb
# import random
# import numpy as np
# import time
# start=time.time()

def find_emo(img):
    fisher_face = cv2.face.FisherFaceRecognizer_create()
    fisher_face.read('final_new_emotionn1_model_1.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fin = cv2.resize(gray, (350, 350))
    # cv2.imwrite("E:\\projectImplementation\\projectFiles\\frames\\try1.jpg",fin)
    pred,conf=(fisher_face.predict(fin))
    return pred

# i=61
# while i<=107:
#     img = cv2.imread("E:\\projectImplementation\\projectFiles\\frames\\nface1\\frame"+str(i)+".jpg",cv2.IMREAD_GRAYSCALE)
#     print("frame",i)
#     print(find_emo(img))
#     i=i+1

# end=time.time()
# print(end-start)