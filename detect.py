import os

import numpy as np
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications.efficientnet import preprocess_input

best_model = load_model(filepath=r'E:\SSD\Uni\Graduation Project\cnn-parameters-improvement-05-0.97.model')
print(best_model.metrics_names)


# best_model.metrics_names
#model_final.save_weights("vgg16_1.h5")


import pandas as pd
df=pd.read_csv(r"E:\SSD\Uni\Graduation Project\submission.csv")

path=r"E:\SSD\Uni\Graduation Project\Brain Dataset\Test\no\No20.jpg"
img = image.load_img(os.path.join(path),target_size=(224,224))
#crop_brain_contour(img)
img = np.asarray(img)
img = np.expand_dims(img, axis=0)
img=preprocess_input(img)
output = best_model.predict(img)
print(output.shape)
print(output)
if output[0][0] > output[0][1]:
    print("no")
elif output [0][1] > output[0][0]:
    print("yes")









