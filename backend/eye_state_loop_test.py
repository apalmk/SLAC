from keras.preprocessing import image
from keras import backend as K
from keras.models import load_model
import numpy as np
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

start=time.time()

trainedModel = load_model('my-model1-20190419-230910.h5')
# my-model1-20190419-230910.h5
def eye_state_predict(path,trainedModel):
    final_data = np.ndarray([1, 24, 24, 1], dtype='float32')
    testingImage = image.load_img(path, target_size=(24, 24))
    testingImage = np.dot(np.array(testingImage, dtype='float32'), [[0.2989], [0.5870], [0.1140]]) / 255
    final_data[0, :, :, :] = testingImage[:, :, :]
    final_data= final_data.reshape((final_data.shape[0], final_data.shape[3]) + final_data.shape[1:3])
    # print(final_data.shape)

    result = trainedModel.predict(final_data)
    # print(result[0][0])
    # K.clear_session()
    if result[0][0]>0.5:
        prediction = 'open'
    else:
        prediction = 'closed'

    return prediction


i=107
while i<=107:
    path = "E:\\projectImplementation\\projectFiles\\frames\\nface2_eye\\eye_frame"+str(i)+".jpg"
    state=eye_state_predict(path,trainedModel)
    print(i,state)
    i=i+1

end= time.time()
print(end-start)
