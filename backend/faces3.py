import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()
imagePath = "E:\\projectImplementation\\projectFiles\\frames\\testcase1\\frame_52.jpg"
image = cv2.imread(imagePath)
result = detector.detect_faces(image)
N=(len(result))
imgg=image.copy()
for i in range(N):
    bounding_box = result[i]['box']
    keypoints = result[i]['keypoints']
    cv2.rectangle(image,
              (bounding_box[0], bounding_box[1]),
              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              (0,155,255),
              6)

    cv2.circle(image,(keypoints['left_eye']), 3, (0,155,255), 2)
    cv2.circle(image,(keypoints['right_eye']), 3, (0,155,255), 2)
    cv2.circle(image,(keypoints['nose']), 3, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_left']), 3, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_right']), 3, (0,155,255), 2)
    imgag=imgg[bounding_box[1]:bounding_box[1] + bounding_box[3],bounding_box[0]:bounding_box[0]+bounding_box[2]]

cv2.imwrite("frames//family_drawn"+str(i)+".jpg", image)

cv2.imshow("image",image)
print(keypoints['right_eye'])
cv2.waitKey(0)
cv2.imwrite("family_drawn.jpg", image)

print(result)