from model import create_model
import cv2
import numpy as np
import PIL.Image as Image

nn4_small2_pretrained = create_model()
nn4_small2_pretrained.load_weights('nn4.small2.v1.h5')

def load_image(path):
    img = cv2.imread(path, 1)
    im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return im

img=load_image('E:\\projectImplementation\\projectFiles\\frames\\abhishek\\ab.jpg')
# ?img = np.around(np.transpose(img, (0,1,2))/255.0, decimals=12)
# cv2.imshow('image',img)
# cv2.waitKey(0)
img = (img / 255.).astype(np.float32)
# print(img.shape)
img=np.expand_dims(img, axis=0)
# print(img)
# print(img.shape)
embedded = nn4_small2_pretrained.predict(img)[0]
np.save('abhishek1.npy', embedded)    # .npy extension is added if not given
print(embedded)
# print(euclidean_distance)
# ?x_train = np.array([img])
# print(x_train)
# ?embedding = nn4_small2_pretrained.predict_on_batch(x_train)
# print(embedding)
# print(embedded)

# cv2.imwrite('E:\\projectImplementation\\projectFiles\\frames\\tthu.jpg',img)
