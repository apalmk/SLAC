import cv2
from model import create_model
import numpy as np

# haar_face_cascade = cv2.CascadeClassifier('haar_profile_face.xml')
# imagesloc = "E:\\projectImplementation\\projectFiles\\frames\\sidefaces\\"
#
# test = cv2.imread('frames/sidefaces/62.jpg')
# if test is None:
#     print("None")
# gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
# faces = haar_face_cascade.detectMultiScale(
#     gray,
#     scaleFactor=1.1,
#     minNeighbors=3,
#     minSize=(30, 30)
# )
# f=len(faces)
# print(f," faces found")
# x1=1
#
# lbp_face_cascade = cv2.CascadeClassifier('lbpcascade_profileface.xml')
# faces1 = lbp_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
#
# f1=len(faces1)
# print(len(faces1))
#
# clone=test.copy()
# clone1=test.copy()
# clone2=test.copy()
# for (x, y, w, h) in faces:
#     cv2.rectangle(clone2, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     cv2.imshow("image",clone2)
#     cv2.waitKey(0)
#     crop_img1 = clone[y-10:y+h+10, x-10:x+w+10]
#     crop_img1 = cv2.resize(crop_img1, (96, 96), interpolation=cv2.INTER_AREA)
#     filename=imagesloc + "/sideface_anjani.jpg"
#     cv2.imwrite(filename, crop_img1)
#
# for (x, y, w, h) in faces1:
#     cv2.rectangle(test, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     cv2.imshow("image",test)
#     cv2.waitKey(0)
#     crop_img2 = clone1[y-20:y+h+20, x-40:x+w+40]
#     filename=imagesloc + "/sidefacel_anjani.jpg"
#     crop_img2 = cv2.resize(crop_img2, (96, 96), interpolation=cv2.INTER_AREA)
#     cv2.imwrite(filename, crop_img2)

img=cv2.imread("frames/sideface_0.jpg")
nn4_small2_pretrained = create_model()
nn4_small2_pretrained.load_weights('nn4.small2.v1.h5')
img = (img / 255.).astype(np.float32)
img = np.expand_dims(img, axis=0)
embedded = nn4_small2_pretrained.predict(img)[0]
np.save('aman_sideface2.npy', embedded)    # .npy extension is added if not given

# cv2.imshow("Faces found", test)
# cv2.waitKey(0)