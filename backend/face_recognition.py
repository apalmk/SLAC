import numpy as np
from keras.preprocessing import image
from keras import backend as K
from keras.models import load_model

def pred(img):
    trainedModel = load_model('my-model1-20190303-011934.h5')
    testingImage = image.load_img(img, target_size = (64, 64))
    testing_image = image.img_to_array(testingImage)
    # print(testing_image.shape)
    testing_image = np.expand_dims(testing_image, axis = 0)
    testing_image=testing_image*1./255
    result = trainedModel.predict(testing_image)
    K.clear_session()
    print(result)
    if result[0][0] > 0.5:
        prediction = 'Anjani'
    else:
        prediction = 'Aman'
    return prediction
    # print('The image is '+prediction)

name=pred('frames/Anjani.jpg')
print(name)