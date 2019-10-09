import cv2
import tensorflow as tf
import copy
import time
from tensorflow.keras.preprocessing.image import img_to_array
import pandas as pd
import numpy as np

# agest_cascade=cv2.CascadeClassifier("cascade.xml")
model=tf.keras.models.load_model("sign_lang_model.h5")
# net=cv2.dnn.readNetFromTensorflow("final_model.h5")
# model=tf.keras.models.load_model("sign_lang_")
counter=0
cap=cv2.VideoCapture("1.mp4")
lis=[]
while(True):
    try:
        ret,frame=cap.read()
        # cv2.imshow("runner",frame)
        # # framer=copy.deepcopy(frame)
        # clr = (255, 0, 0)
        # str=2
        cv2.rectangle(frame, (50, 50), (300, 300), (0, 255, 0), 0)
        framer=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # # blob = cv2.dnn.blobFromImage(frame, 1, (64, 64), (104, 117, 123))
        # # print(blob.shape)
        # # cv2.imshow("blob",blob)
        # # print(model.predict(blob.resize(1,150,150,1)))
        #
        # # print(np.argmax(preds))
        # # end = time.time()
        roi_gray=framer[50:300,50:300]

        # # s=x
        cv2.imshow("frame2",cv2.resize(roi_gray,(28,28),interpolation=cv2.INTER_AREA))
        #     # print(model.predict(cv2.resize(roi_gray,(64,64),interpolation=cv2.INTER_AREA).resize(1,64,64,3)))
        # cv2.imshow('frame', frame)
        runner=cv2.resize(roi_gray,(28,28),interpolation=cv2.INTER_AREA)
        # cv2.imshow("processed_frame",runner)
        # # runner=runner/255
        # # print(runner)
        s=np.argmax(model.predict(np.reshape(runner,(1,28,28,1))))
        # print(s)
        lis.append(s)

        # #
        # if(s==0):
        #     print("Hi")
        #
        # elif(s==5):
        #     print("fine")
        # time.sleep(0.04)
        # # elif(s==14):
        # #     print("how")
        # # time.sleep(0.004)
        # agest=agest_cascade.detectMultiScale(,scaleFactor=1.5,minNeighbors=5)

        # for (x,y,w,h) in agest:
        #
        #     # print(x,y,w,h)
        #     roi_gray=gray[y:y+h,x:x+w]
        #     f=frame[y:y+h,x:x+w]
        #     print(np.argmax(model.predict(cv2.resize(f,(64,64),interpolation=cv2.INTER_AREA).reshape(1,64,64,3))))
        #
        #     # img_item="image.png"
        #     # cv2.imwrite(img_item,roi_gray)
        #     color=(255,0,0)
        #     stroke=2
        #     en_x=x+w
        #     en_y=y+h
        #     cv2.rectangle(frame,(x,y),(en_x,en_y),color,stroke)
        # print(s)
        cv2.imshow('frame',runner)
        counter+=1
        if(counter==500):
            l=np.bincount(lis).argmax()
            writer=open("hello_world.txt","a")
            writer.write(str(l)+" ")
            break
    except:
        print("the code ended")
        # print(np.bincount(lis).argmax())
        l = np.bincount(lis).argmax()
        writer = open("hello_world.txt", "w+")
        writer.write(str(l)+" ")
        break
    if(cv2.waitKey(20)&0xFF==ord("q")):
        break
counter+=1

cap.release()
# cap.destroyAllWindows()
