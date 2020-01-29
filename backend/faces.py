import cv2
import sys


imagePath = "C:\\Users\\ANJANIPRASAD\\PycharmProjects\\Sin\\frames\\family2.jpg"
cascPath = "C:\\Users\\ANJANIPRASAD\\PycharmProjects\\Sin\\haarcascade_face_detect.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imagesloc = "C:\\Users\\ANJANIPRASAD\\PycharmProjects\\Sin\\frames"

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))
centers_list=[]
# Draw a rectangle around the faces
x1=1
for (x, y, w, h) in faces:
    # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    centers_list.append((x+(w/2),y+(h/2)))
    # clone=image.copy()
    crop_img = image[y:y+h, x:x+w]
    filename=imagesloc + "/image_" + str(int(x1)) + "_frame1.jpg"
    cv2.imwrite(filename, crop_img)
    x1=x1+1
# cv2.imshow("Faces found", image)
print(centers_list)
# cv2.waitKey(0)