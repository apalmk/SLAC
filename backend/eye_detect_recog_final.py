import cv2
import math
import numpy as np
import time
from keras.models import load_model


# start=time.time()

# imagesloc = "E:\\projectImplementation\\projectFiles\\frames\\nface2_eye"
# eye_cascade = cv2.CascadeClassifier("E:\\projectImplementation\\projectFiles\\eye.xml")
# eye_cascade_right= cv2.CascadeClassifier("E:\\projectImplementation\\projectFiles\\right_eye_haar.xml")
eye_cascade_left= cv2.CascadeClassifier("E:\\projectImplementation\\projectFiles\\left_eye_haar.xml")
# eye_cascade_tree= cv2.CascadeClassifier("E:\\projectImplementation\\projectFiles\\haarcascade_eye_tree_glasses.xml")
trainedModel = load_model('my-model1-20190419-230910.h5')

def eye_ext(image1,trainedModel,eye_cascade_left):

    # image = cv2.imread(imagePath)
    # image1 = cv2.imread(imagePath)
    # image1= cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    # print(imagePath)
    # eyes = eye_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=10)
    # print("found {0} eyes".format(len(eyes)))
    eyes2= eye_cascade_left.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=10)
    # print("found {0} eyes".format(len(eyes2)))
    # eyes3= eye_cascade_right.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=10)
    # print("found {0} eyes".format(len(eyes3)))
    # eyes4= eye_cascade_tree.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
    # print("found {0} eyes".format(len(eyes4)))

    for (ex,ey,ew,eh) in eyes2:
        crop_eye=image1[ey:ey+eh, ex:ex+ew]
        final_data = np.ndarray([1, 24, 24, 1], dtype='float32')
        # testingImage = image.load_img(path, target_size=(24, 24))
        testingImage=cv2.resize(crop_eye,(24,24))
        testingImage = np.dot(np.array(testingImage, dtype='float32'), [[0.2989], [0.5870], [0.1140]]) / 255
        # print(testingImage.shape)
        final_data[0, :, :, :] = testingImage[:, :, :]
        final_data = final_data.reshape((final_data.shape[0], final_data.shape[3]) + final_data.shape[1:3])
        # print(final_data.shape)

        result = trainedModel.predict(final_data)
        # print(result[0][0])
        # K.clear_session()
        if result[0][0] > 0.5:
            prediction = 'open'
        else:
            prediction = 'closed'

        return prediction

        #write recognition here and return the state
        # filename = imagesloc + "/eye_frame"+str(i)+".jpg"
        # cv2.imwrite(filename, crop_eye)
        break


# i=61
# while i<=69:
#     imagePath = "E:\\projectImplementation\\projectFiles\\frames\\nface2\\frame"+str(i)+".jpg"
#     pred=eye_ext(imagePath,trainedModel,eye_cascade_left)
#     print(i,pred)
#     i=i+1
#
# end= time.time()
# print(end-start)