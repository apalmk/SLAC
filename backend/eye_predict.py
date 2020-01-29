from keras.models import Sequential
from keras.layers import Conv2D
from datetime import datetime
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import numpy as np
from keras.preprocessing import image
from keras import backend as K
from keras.models import load_model
import cv2
from PIL import Image
import numpy as np
import os

trainedModel = load_model('my-model1-20190302-042735.h5')
final_data = np.ndarray([1, 24, 24, 1], dtype='float32')
testingImage = image.load_img('frames/nface1_eye/eye_frame77.jpg', target_size=(24, 24))
# print(type(testingImage.))
testingImage = np.dot(np.array(testingImage, dtype='float32'), [[0.2989], [0.5870], [0.1140]]) / 255
print(testingImage.shape)
final_data[0, :, :, :] = testingImage[:, :, :]
# finalized_data=np.rollaxis(final_data, 3, 1)
# imaged_data = np.moveaxis(imaged_data, -1, 0)
final_data= final_data.reshape((final_data.shape[0], final_data.shape[3]) + final_data.shape[1:3])

print(final_data.shape)

result = trainedModel.predict(final_data)
print(result[0][0])
K.clear_session()
if result[0][0]>0.5:
    prediction = 'open'
else:
    prediction = 'closed'

print(prediction)
# print(trainedModel.predict(final_data, verbose=1, steps=None))