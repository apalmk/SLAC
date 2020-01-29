from keras.models import Sequential
from keras.layers import Conv2D
from datetime import datetime
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

cls = Sequential()
cls.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
cls.add(MaxPooling2D(pool_size = (2, 2)))
cls.add(Conv2D(32, (3, 3), activation = 'relu'))
cls.add(MaxPooling2D(pool_size = (2, 2)))
cls.add(Conv2D(32, (3, 3), activation = 'relu'))
cls.add(MaxPooling2D(pool_size = (2, 2)))
cls.add(Conv2D(32, (3, 3), activation = 'relu'))
cls.add(MaxPooling2D(pool_size = (2, 2)))
cls.add(Flatten())
cls.add(Dense(units = 256, activation = 'relu'))
cls.add(Dense(units = 1, activation = 'sigmoid'))
cls.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


from keras.preprocessing.image import ImageDataGenerator
training_data = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)
testing_data = ImageDataGenerator(rescale = 1./255)

trainSet = training_data.flow_from_directory('ds1/train_set',
target_size = (64, 64),
batch_size = 15,
class_mode = 'binary')

testingSet = testing_data.flow_from_directory('ds1/testing_set',
target_size = (64, 64),
batch_size = 15,
class_mode = 'binary')

cls.fit_generator(trainSet,
steps_per_epoch = 20,
epochs = 30,
validation_data = testingSet,
validation_steps = 15)

s= str(datetime.now().strftime("%Y%m%d-%H%M%S"))
cls.save('my-model1-%s.h5'%s)

