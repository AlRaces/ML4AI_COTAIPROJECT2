import cv2
import os
import time
import uuid

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'
labels = ["Hello", "Thanks", "Yes", "No", "ILoveYou"]
num_imgs = 15

for label in labels:
    os.mkdir('Tensorflow\workspace\images\collectedimages\\' + str(label))
    cap = cv2.VideoCapture(0)
    print(f'Collecting images for {label}') 
    time.sleep(5)
    for imgnum in range(num_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    cap.release()
