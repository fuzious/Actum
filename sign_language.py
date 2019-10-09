import tensorflow as tf
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# reading the data from the library
train=pd.read_csv("sign_mnist_train.csv")
test=pd.read_csv("sign_mnist_test.csv")
# deciding the labels
label_train=train["label"].to_numpy()
train.drop(columns=["label"],inplace=True)
label_test=test["label"].to_numpy()
test.drop(columns=["label"],inplace=True)

print(train.head())

# showing images
# just a test to see if the images are really showing
# image=train.iloc[:1].to_numpy().reshape(28,28)
# plt.imshow(image)
# plt.show()

# processing all the data present in the train here
counter=1
train_images=[]
for i in range(len(train["pixel1"])):
    train_images.append(train.iloc[counter-1:counter].to_numpy().reshape(28,28,1))
    counter+=1
test_images=[]
counter=1
for i in range(len(test["pixel1"])):
    test_images.append(test.iloc[counter-1:counter].to_numpy().reshape(28,28,1))
    counter+=1
train_images=np.array(train_images)
test_images=np.array(test_images)

# defining the coustom model;
label_train=tf.keras.utils.to_categorical(label_train,25)
label_test=tf.keras.utils.to_categorical(label_test,25)
train_images=train_images/255.0
test_images=test_images/255.0

model=tf.keras.Sequential([
    tf.keras.layers.Conv2D(filters=32,kernel_size=(5,5),input_shape=(28,28,1),activation="relu"),
    tf.keras.layers.Conv2D(filters=32,kernel_size=(5,5),activation="relu"),
    tf.keras.layers.MaxPool2D(pool_size=(2,2)),
    # tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Conv2D(filters=64,kernel_size=(3,3),activation="relu"),
    tf.keras.layers.Conv2D(filters=64,kernel_size=(3,3),activation="relu"),
    tf.keras.layers.MaxPool2D(pool_size=(2,2)),
    # tf.keras.layers.Conv2D(filters=6,kernel_size=(2,2),strides=2,activation="relu"),
    # tf.keras.layers.MaxPool2D(),


    # tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), strides=2, activation="relu"),
    # tf.keras.layers.MaxPool2D(),

    # tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3),strides=2,activation="relu"),
    # tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512,activation="relu"),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dense(64,activation="relu"),
    tf.keras.layers.Dense(25,activation="softmax"),


])

model.compile(loss="categorical_crossentropy",metrics=["accuracy"],optimizer="rmsprop")
model.fit(train_images,label_train,epochs=5,batch_size=2)

model.save("sign_lang_model.h5")
print("saved to disk")