import numpy as np
import os
import tensorflow as tf
from keras.models import Model, load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image


# Add our data-augmentation parameters to ImageDataGenerator
trdata = ImageDataGenerator(rescale = 1./255.,rotation_range = 40, width_shift_range = 0.2, height_shift_range = 0.2, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
traindata = trdata.flow_from_directory(directory=r"E:\SSD\Uni\Graduation Project\archive\Training",batch_size=20 ,class_mode = 'binary',target_size=(224,224))

# Note that the validation data should not be augmented!
tsdata = ImageDataGenerator(rescale = 1.0/255.)
testdata = tsdata.flow_from_directory(directory=r"E:\SSD\Uni\Graduation Project\archive\Testing", batch_size=20,class_mode = 'binary', target_size=(224,224))




#We will be using only the basic models, with changes made only to the final layer.
# This is because this is just a binary classification problem while these models are built to handle up to 1000 classes.
from keras.applications.vgg16 import VGG16

import efficientnet.tfkeras as efn

basemodel = efn.EfficientNetB7(input_shape = (224, 224, 3) ,weights='imagenet', include_top=False) # Leave out the last fully connected layer

basemodel.summary()


#Since we don’t have to train all the layers, we make them non_trainable:
from keras.layers import Dense, Dropout ,Flatten
for layers in (basemodel.layers):
    #print(layers)
    layers.trainable = False

#Compile and fit the model:
# Flatten the output layer to 1 dimension
x = Flatten()(basemodel.output)
# Add a fully connected layer with 512 hidden units and ReLU activation
#x = Dense(512, activation='relu') (vggmodel.layers[-2].output)

x = Dense(1024, activation="relu")(x)
x = Dropout(0.5)(x)
# Add a dropout rate of 0.5

# Add a final sigmoid layer with 1 node for classification output
x = Dense(1, activation='sigmoid')(x)

model = tf.keras.models.Model(basemodel.input, x)

model.compile(optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.0001,decay=1e-6), loss = 'binary_crossentropy',metrics = ['acc'])

# Save the best model during training
from keras.callbacks import ModelCheckpoint
filepath="cnn-parameters-improvement-{epoch:02d}-{val_acc:.2f}"
checkpoint = ModelCheckpoint(r"E:\SSD\Uni\Graduation Project\Brain-Tumor-Detection-master\Modelss/{}.model".format(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max'))

# Train the model
#model.fit(traindata,steps_per_epoch=2, epochs=10 ,validation_data=testdata, validation_steps=50, callbacks=[checkpoint])

# Load the best model
#model = load_model('vgg16_weights.h5')

#features method



