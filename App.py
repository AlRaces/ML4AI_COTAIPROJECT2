import mss
import numpy as np
import cv2
import time
import keyboard
import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
path = './yolov7/best.pt'
model = torch.hub.load("WongKinYiu/yolov7","custom",f"{path}",trust_repo=True)

cap = cv2.VideoCapture(0)

while True:
    t = time.time()

    ret, frame = cap.read()
    img = cv2.resize(frame, (1280, 720))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = model(img)
    results.render()
    out = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow('s', out)

    print('fps: {}'.format(1 / (time.time() - t)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()