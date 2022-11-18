import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

capture = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300


labels = ['F']

counter = 0
for label in labels:
    print(f"Taking data for label {label}")
    folder = f"Data/{label}"
    check = True
    while check:
        try:
            success, img = capture.read()
            hands, img = detector.findHands(img)

            if hands:
                hand = hands[0]
                x, y, w, h = hand['bbox']

                imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
                # crop the image
                imgCrop = img[y - offset:y + h +
                              offset, x - offset:x + w + offset]

                imgCropShape = imgCrop.shape

                aspectRatio = h/w

                if aspectRatio > 1:
                    const = imgSize/h
                    wCal = math.ceil(const*w)
                    imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                    imgResizeShape = imgResize.shape
                    wGap = math.ceil((imgSize - wCal)/2)
                    imgWhite[:, wGap:wCal+wGap] = imgResize
                else:
                    const = imgSize/w
                    hCal = math.ceil(const*w)
                    imgResize = cv2.resize(imgCrop, (hCal, imgSize))
                    imgResizeShape = imgResize.shape
                    hGap = math.ceil((imgSize - hCal)/2)
                    imgWhite[hGap:hCal+hGap, :] = imgResize

                cv2.imshow('ImageCrop', imgCrop)
                cv2.imshow('ImageWhite', imgWhite)

            cv2.imshow('Image', img)
            key = cv2.waitKey(1)
        except Exception as e:
            print(e)

        if key == ord("s"):
            counter += 1
            cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
            print(counter)

        if counter >= 300:
            counter = 0
            check = False
