import cv2
import imutils
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
#print(os.listdir(r"D:\2NAAAAA\gradution project\New folder (2)\brain_tumor_dataset"))


os.listdir("../")


import keras
from keras.models import Model, load_model
from keras.layers import Dense ,Flatten
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image


#os.listdir(r"D:\2NAAAAA\gradution project\New folder (2)\brain_tumor_dataset\training_set")

# trdata = ImageDataGenerator()
# traindata = trdata.flow_from_directory(directory=r"E:\SSD\Uni\Graduation Project\archive\Training",target_size=(224,224))
#
# tsdata = ImageDataGenerator()
# testdata = tsdata.flow_from_directory(directory=r"E:\SSD\Uni\Graduation Project\archive\Testing", target_size=(224,224))
#


from keras.applications.vgg16 import VGG16

vggmodel = VGG16(weights='imagenet', include_top=True)

#vggmodel.summary()



for layers in (vggmodel.layers)[:19]:
    print(layers)
    layers.trainable = False



X= vggmodel.layers[-2].output


predictions = Dense(2, activation="softmax")(X)


model_final = Model(inputs = vggmodel.input, outputs = predictions)


import tensorflow as tf

model_final.compile(loss = "categorical_crossentropy", optimizer =tf.keras.optimizers.SGD(learning_rate=0.0001, momentum=0.9, decay=1e-6), metrics=["acc"])


#model_final.summary()



from keras.callbacks import ModelCheckpoint

#os.listdir("../")

filepath="cnn-parameters-improvement-{epoch:02d}-{val_acc:.2f}"
#save the model with the best validation (development) accuracy till now
checkpoint = ModelCheckpoint(r"E:\SSD\Uni\Graduation Project\Brain-Tumor-Detection-master\Modelss/{}.model".format(filepath, monitor='val_acc', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1))


#checkpoint = ModelCheckpoint("vgg16_1.h5", monitor='val_acc', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
#early = EarlyStopping(monitor='val_acc', min_delta=0, patience=40, verbose=1, mode='auto')

#model_final.fit(generator=traindata, steps_per_epoch= 2, epochs=15, validation_data= testdata, validation_steps=1, callbacks=[checkpoint])

import pyrebase
import urllib.request

firebaseConfig = {
  'apiKey': "AIzaSyCjI1nJ3C-BphF73hGzi1mNYuVNcD_RoyI",
  'authDomain': "cnn-model-2bdfe.firebaseapp.com",
  'databaseURL': "https://cnn-model-2bdfe-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "cnn-model-2bdfe",
  'storageBucket': "cnn-model-2bdfe.appspot.com",
  'messagingSenderId': "196800182225",
  'appId': "1:196800182225:web:02c926eba0853aab7152f0",
  'measurementId': "G-FK5Q7JJRMN"
};


firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
auth=firebase.auth()
storage=firebase.storage()
path='model.json'
print(storage.child(path).get_url(None))
url=storage.child(path).get_url(None)
f=urllib.request.urlopen(url).read()
print(f)









#best_model = load_model(filepath=r'E:\SSD\Uni\Graduation Project\cnn-parameters-improvement-05-0.97.model')
best_model = load_model(filepath='model.json')
# best_model.metrics_names
#model_final.save_weights("vgg16_1.h5")

# from keras.applications.efficientnet import preprocess_input
# import pandas as pd
# df=pd.read_csv(r"E:\SSD\Uni\Graduation Project\submission.csv")
#
#
# print(df["label"][0])
# pd.options.mode.chained_assignment = None  # default='warn'
#
# for e,i in enumerate(os.listdir(r"E:\SSD\Uni\Graduation Project\Brain Dataset\Test\yes")):
#     print(i)
#     output=[]
#     img = image.load_img(os.path.join(r"E:\SSD\Uni\Graduation Project\Brain Dataset\Test\yes",i),target_size=(224,224))
#     img = np.asarray(img)
#     img = np.expand_dims(img, axis=0)
#     img=preprocess_input(img)
#     output = best_model.predict(img)
#     if output[0][0] > output[0][1]:
# #         print("cat")
#         df["id"][e]=i
#         df["label"][e]="-----------> NO"
#     else:
# #         print('dog')
#         df["id"][e]=i
#         df["label"][e]="-----------> YES"
# df
# df.to_csv("submission.csv",index=False)







# img = image.load_img(os.path.join(r"E:\SSD\Uni\Graduation Project\Brain Dataset\Test\no\nooo.jpg"),target_size=(224,224))
# #crop_brain_contour(img)
# img = np.asarray(img)
# img = np.expand_dims(img, axis=0)
# output = best_model.predict(img)
# if output[0][0] > output[0][1]:
#  print("no")
# elif output [0][1] > output[0][0]:
#  print('yes')
# else:
#  print('Unknown')