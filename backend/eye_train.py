from keras.models import Sequential
from keras.layers import Conv2D
from datetime import datetime
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import cv2
import numpy as np
import os

dirs = ['dataset/openLeftEyes', 'dataset/openRightEyes']
dirs2 = ['dataset/closedLeftEyes', 'dataset/closedRightEyes']

def generate_dataset():
    dataset = np.ndarray([1265 * 2, 24, 24, 1], dtype='float32')
    i = 0
    for dir in dirs:
        for filename in os.listdir(dir):
            if filename.endswith('.jpg'):
                im = cv2.imread(dir + '/' + filename)
                im = np.dot(np.array(im, dtype='float32'), [[0.2989], [0.5870], [0.1140]]) / 255
                dataset[i, :, :, :] = im[:, :, :]
                i += 1
    labels = np.ones([len(dataset), 1], dtype=int)
    return dataset, labels


def generate_dataset_closed():
    dataset = np.ndarray([1192 * 2, 24, 24, 1], dtype='float32')
    i = 0
    for dir in dirs2:
        for filename in os.listdir(dir):
            if filename.endswith('.jpg'):
                im = cv2.imread(dir + '/' + filename)
                im = np.dot(np.array(im, dtype='float32'), [[0.2989], [0.5870], [0.1140]]) / 255
                dataset[i, :, :, :] = im[:, :, :]
                i += 1
    labels = np.zeros([len(dataset), 1], dtype=int)
    return dataset, labels


dataset_open, labels_open = generate_dataset()
dataset_closed, labels_closed = generate_dataset_closed()
print("done")

split = int(len(dataset_closed) * 0.8)
train_dataset_closed = dataset_closed[:split]
train_labels_closed = labels_closed[:split]
test_dataset_closed = dataset_closed[split:]
test_labels_closed = labels_closed[split:]

split = int(len(dataset_open) * 0.8)
train_dataset_open = dataset_open[:split]
train_labels_open = labels_open[:split]
test_dataset_open = dataset_open[split:]
test_labels_open = labels_open[split:]

train_dataset=train_dataset_open
train_dataset= np.concatenate([train_dataset,train_dataset_closed])
train_labels=train_labels_open
train_labels=np.concatenate([train_labels,train_labels_closed])

test_dataset=test_dataset_open
test_dataset=np.concatenate([test_dataset,test_dataset_closed])
test_labels=test_labels_open
test_labels=np.concatenate([test_labels,test_labels_closed])

batch_size = 30
epochs = 50

X_train = train_dataset
X_train = X_train.reshape((X_train.shape[0], X_train.shape[3]) + X_train.shape[1:3])
print(X_train.shape)
Y_train = train_labels

X_test = test_dataset
X_test = X_test.reshape((X_test.shape[0], X_test.shape[3]) + X_test.shape[1:3])
Y_test = test_labels
print(X_train.shape)
tot,img_channels, img_rows, img_cols = X_train.shape

model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same',
                        input_shape=(img_channels, img_rows, img_cols),activation='relu',data_format='channels_first'))
model.add(Conv2D(24, (3, 3),activation='relu',data_format='channels_first'))
model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same', activation='relu',data_format='channels_first'))
model.add(Conv2D(64, (3, 3),activation='relu',data_format='channels_first'))
model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(units = 512, activation = 'relu'))
model.add(Dense(units = 1, activation = 'sigmoid'))
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(X_test, Y_test))
s= str(datetime.now().strftime("%Y%m%d-%H%M%S"))
model.save('my-model1-%s.h5'%s)
score = model.evaluate(X_test, Y_test)
print(score)