import handy
import cv2
import tensorflow as tf
import numpy as np
model=tf.keras.models.load_model("../sign_lang_model.h5")

# getting video feed from webcam
hist = handy.capture_histogram(source=0)
cap = cv2.VideoCapture(0)


# capture the hand histogram by placing your hand in the box shown and
# press 'A' to confirm
# source is set to inbuilt webcam by default. Pass source=1 to use an
# external camera.

counter=0
lis=[]
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # to block a faces in the video stream, set block=True.
    # if you just want to detect the faces, set block=False
    # if you do not want to do anything with faces, remove this line
    handy.detect_face(frame, block=True)

    # detect the hand
    hand = handy.detect_hand(frame, hist)

    # to get the outline of the hand
    # min area of the hand to be detected = 10000 by default
    custom_outline = hand.draw_outline(
        min_area=10000, color=(0, 255, 255), thickness=2)

    # to get a quick outline of the hand
    quick_outline = hand.outline
    # print(quick_outline.shape)
    cv2.imshow("just this",quick_outline)
    # draw fingertips on the outline of the hand, with radius 5 and color red,
    # filled in.
    for fingertip in hand.fingertips:
        cv2.circle(quick_outline, fingertip, 5, (0, 0, 255), -1)

    # to get the centre of mass of the hand
    com = hand.get_center_of_mass()
    if com:
        cv2.circle(quick_outline, com, 10, (255, 0, 0), -1)



    # display the unprocessed, segmented hand
    cv2.imshow("Handy", hand.masked)
    cv2.rectangle(quick_outline, (50, 50), (300, 300), (0, 255, 0), 0)
    framer=hand.masked[50:300,50:300]
    # fr=cv2.cvtColor(framer,cv2.COLOR_RGB2HLS)
    r,g,b=cv2.split(framer)
    framer=cv2.cvtColor(framer,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("may work",framer)
    # cv2.imshow("processed",cv2.resize(r, (28, 28), interpolation=cv2.INTER_AREA))
    # cv2.imshow("processed",cv2.resize(g, (28, 28), interpolation=cv2.INTER_AREA))
    # cv2.imshow("processed",cv2.resize(b, (28, 28), interpolation=cv2.INTER_AREA))

    print(np.argmax(model.predict((cv2.resize(framer,(28, 28), interpolation=cv2.INTER_AREA)).reshape(1,28,28,1))))
    # print(np.argmax(model.predict((cv2.resize(g, (28, 28), interpolation=cv2.INTER_AREA)).reshape(1, 28, 28, 1))))
    # print(np.argmax(model.predict((cv2.resize(b, (28, 28), interpolation=cv2.INTER_AREA)).reshape(1, 28, 28, 1))))
    # print(framer.shape)
    # print(framer.shape)
    cv2.imshow("Handy", quick_outline)
    # display the binary version of the hand
    # cv2.imshow("Handy", hand.binary)

    k = cv2.waitKey(5)

    # Press 'q' to exit
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
