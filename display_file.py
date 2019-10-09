import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import pandas as pd
import numpy as np
#
agest_cascade=cv2.CascadeClassifier("aGest.xml")
fist_cascade=cv2.CascadeClassifier("palm_v4.xml")
# v_cascade=cv2.CascadeClassifier("cascade.xml")
# model=tf.keras.models.load_model("final_model.h5")
# fist=cv2.CascadeClassifier("fist.xml")
# palm=cv2.CascadeClassifier("palm.xml")
# lpalm=cv2.CascadeClassifier("right.xml")
plam_cascade=cv2.CascadeClassifier("right.xml")
# model=tf.keras.models.load"_model("sign_lang_")
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    agest=agest_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for (x,y,w,h) in agest:

        # print(x,y,w,h)
        roi_gray=gray[y:y+h,x:x+w]
        f=frame[y:y+h,x:x+w]
        # print(np.argmax(model.predict(cv2.resize(f,(64,64),interpolation=cv2.INTER_AREA).reshape(1,64,64,3))))

        # img_item="image.png"
        # cv2.imwrite(img_item,roi_gray)
        color=(255,0,0)
        stroke=2
        en_x=x+w
        en_y=y+h
        cv2.rectangle(frame,(x,y),(en_x,en_y),color,stroke)

    fist = fist_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in fist:
        # print(x,y,w,h)
        roi_gray = gray[y:y + h, x:x + w]
        f = frame[y:y + h, x:x + w]
        # print(np.argmax(model.predict(cv2.resize(f,(64,64),interpolation=cv2.INTER_AREA).reshape(1,64,64,3))))

        # img_item="image.png"
        # cv2.imwrite(img_item,roi_gray)
        color = (255, 0, 0)
        stroke = 2
        en_x = x + w
        en_y = y + h
        cv2.rectangle(frame, (x, y), (en_x, en_y), color, stroke)
    r=plam_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for (x,y,w,h) in r:
        roi_gray = gray[y:y + h, x:x + w]
        f = frame[y:y + h, x:x + w]
        # print(np.argmax(model.predict(cv2.resize(f,(64,64),interpolation=cv2.INTER_AREA).reshape(1,64,64,3))))

        # img_item="image.png"
        # cv2.imwrite(img_item,roi_gray)
        color = (255, 0, 0)
        stroke = 2
        en_x = x + w
        en_y = y + h
        cv2.rectangle(frame, (x, y), (en_x, en_y), color, stroke)

    cv2.imshow('frame',frame)
    if(cv2.waitKey(20)&0xFF==ord("q")):
        break
cap.release()
cap.destroyAllWindows()
