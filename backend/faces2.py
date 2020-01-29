import cv2

from faced.faced1.detector import FaceDetector
from faced.faced1.utils import annotate_image

face_detector = FaceDetector()

img = cv2.imread("E:\\projectImplementation\\projectFiles\\frames\\family5.jpg")
rgb_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)
# converts color order from bgr to rgb
imagesloc = "E:\\projectImplementation\\projectFiles\\frames"

bboxes,N = face_detector.predict(rgb_img, 0.2)

print(N)
bbboxes=[]
for i in range(N):
    bbboxes.append((bboxes[i][0],bboxes[i][1],bboxes[i][2],bboxes[i][3],bboxes[i][4]))
    # print(bbboxes[i][4])
# bboxes[]
#xc,yc,w,h,prob
x1=1
for j in range(N):
    xc=bbboxes[j][0]
    yc=bbboxes[j][1]
    w=bbboxes[j][2]
    h=bbboxes[j][3]
    crop_img = img[int(yc-(h/2)):int(yc+(h/2)), int(xc-(w/2)):int(xc + (w/2))]
    filename = imagesloc + "/face_" + str(int(x1)) + "_frame1.jpg"
    cv2.imwrite(filename, crop_img)
    x1 = x1 + 1
# Show the image
ann_img,center = annotate_image(img, bbboxes)
print(center)
cv2.imshow('image',ann_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

