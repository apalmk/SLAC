import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import PIL.Image as Image

from align import AlignDlib
# Put the detections in an array then at last you do the computation 3 consecutive absences etc.
# %matplotlib inline

def load_image(path):
    img = cv2.imread(path, 1)
    im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return im

alignment = AlignDlib('models/landmarks.dat')

img= load_image('E:\\projectImplementation\\projectFiles\\frames\\family5.jpg')
imgg=img.copy()
# cv2.imshow('image',img)
# cv2.waitKey(0)
# Detect face and return bounding box
# bb = alignment.getLargestFaceBoundingBox(img)
# bb=[]
bb = alignment.getAllFaceBoundingBoxes(img)
# n=bb.length
# print(len(bb))
N=len(bb)
bbox=[]
print(N)
for i in range(N):
# Transform image using specified face landmark indices and crop image to 96x96
#     bbox[0].append(bb[i].left())
#     bbox[1]=bb[i].top()
#     bbox[2]=bb[i].right()
#     bbox[3]=bb[i].bottom()
#     img1=img[bbox[1]:bbox[1]+bbox[3],bbox[0]:bbox[0]+bbox[2]]

    img1=imgg[bb[i].top():bb[i].bottom(),bb[i].left():bb[i].right()]
    img1=cv2.cvtColor(img1,cv2.COLOR_RGB2BGR)
    cv2.imwrite('E:\\projectImplementation\\projectFiles\\frames\\att' + str(i) + '.jpg', img1)
    im_aligned = alignment.align(96, img, bb[i], landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)
    im_aligned = cv2.cvtColor(im_aligned, cv2.COLOR_RGB2BGR)
    cv2.imwrite('E:\\projectImplementation\\projectFiles\\frames\\tt'+str(i)+'.jpg',im_aligned)

# # Show original image
# plt.subplot(131)
# plt.imshow(img)
#
# # Show original image with bounding box
# plt.subplot(132)
# plt.imshow(img)
# plt.gca().add_patch(patches.Rectangle((bb.left(), bb.top()), bb.width(), bb.height(), fill=False, color='red'))
#
# # Show aligned image
# plt.subplot(133)
# plt.imshow(jc_aligned);