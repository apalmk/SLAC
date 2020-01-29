# import cv2
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# import PIL.Image as Image
# import numpy as np
# from model import create_model
# from keras import backend as K
# import tensorflow as tf
# from align import AlignDlib
# from keras import backend as K
#
# # %matplotlib inline
#
# def load_image(path):
#     img = cv2.imread(path, 1)
#     im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     return im

def findd():
    import cv2
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    import PIL.Image as Image
    import numpy as np
    from model import create_model
    from keras import backend as K
    import tensorflow as tf
    from align import AlignDlib
    from keras import backend as K

    tf.keras.backend.clear_session()
    K.clear_session()

    alignment = AlignDlib('models/landmarks.dat')

    # img= load_image('E:\\projectImplementation\\projectFiles\\imageee.png')
    img=cv2.imread('E:\\projectImplementation\\projectFiles\\imageee.png',1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    bb = alignment.getLargestFaceBoundingBox(img)

    im_aligned = alignment.align(96, img, bb, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)

    anjani = np.load('anjani.npy')
    aman = np.load('aman.npy')
    rapaka= np.load('rapaka.npy')
    akc = np.load('akc.npy')
    abhi= np.load('abhishek.npy')
    hemanth = np.load('hemanth.npy')
    subham = np.load('subham.npy')
    vivek = np.load('vivek.npy')
    nn4_small2_pretrained = create_model()
    nn4_small2_pretrained.load_weights('nn4.small2.v1.h5')
    im_aligned = (im_aligned / 255.).astype(np.float32)
    im_aligned=np.expand_dims(im_aligned, axis=0)
    embedded = nn4_small2_pretrained.predict(im_aligned)[0]
# print(embedded)
#     tf.keras.backend.clear_session()
    # K.clear_session()
    distances=[]
    distances.append(np.linalg.norm(embedded-anjani))
    distances.append(np.linalg.norm(embedded-abhi))
    distances.append(np.linalg.norm(embedded-subham))
    distances.append(np.linalg.norm(embedded-rapaka))
    distances.append(np.linalg.norm(embedded-hemanth))
    distances.append(np.linalg.norm(embedded-aman))
    distances.append(np.linalg.norm(embedded-akc))
    fin=min(distances)
    if  (fin==distances[0]):
        return "Anjani"
    if (fin == distances[1]):
        return "Abhishek"
    if (fin == distances[2]):
        return "Subham"
    if (fin == distances[3]):
        return "Rapaka"
    if (fin == distances[4]):
        return "Hemanth"
    if (fin == distances[5]):
        return "Aman"
    if (fin == distances[6]):
        return "Akshay"
