import cv2
import cv2.face
import glob as gb
import random
import numpy as np

emojis = ["neutral", "anger", "disgust", "happy", "surprise"]
fisher_face = cv2.face.FisherFaceRecognizer_create()
data = {}


def getFiles(emotion):
    files = gb.glob("final_dataset\\%s\\*" % emotion)
    random.shuffle(files)
    training = files[:int(len(files) * 0.67)]
    prediction = files[-int(len(files) * 0.33):]
    return training, prediction


def makeTrainingAndValidationSet():
    training_data = []
    training_labels = []
    prediction_data = []
    prediction_labels = []
    for emotion in emojis:
        training, prediction = getFiles(emotion)

        for item in training:
            image = cv2.imread(item)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            training_data.append(gray)
            training_labels.append(emojis.index(emotion))

        for item in prediction:
            image = cv2.imread(item)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            prediction_data.append(gray)
            prediction_labels.append(emojis.index(emotion))
    return training_data, training_labels, prediction_data, prediction_labels


def runClassifier(num):
    training_data, training_labels, prediction_data, prediction_labels = makeTrainingAndValidationSet()

    print("training fisher face classifier using the training data")
    print("size of training set is:", len(training_labels), "images")
    fisher_face.train(training_data, np.asarray(training_labels))
    fisher_face.write('final_new_emotionn1_model_'+str(num)+'.xml')
    # fishface.save('fish_models/fish_model' + str(num) + '.xml')
    print("classification prediction")
    counter = 0
    right = 0
    wrong = 0
    for image in prediction_data:
        pred, conf = fisher_face.predict(image)
        if pred == prediction_labels[counter]:
            right += 1
            counter += 1
        else:
            wrong += 1
            counter += 1
    return ((100 * right) / (right + wrong))



metascore = []
for i in range(0, 10):
    right = runClassifier(i)
    print("got", right, "percent right!")
    metascore.append(right)
print("\n\nend score:", np.mean(metascore), "percent right!")