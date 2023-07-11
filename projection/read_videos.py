import cv2
import numpy as np
# import time
import convolve

# time.sleep(300)
cap = cv2.VideoCapture(4,)
cap.set(3, 640)
cap.set(4, 480)
print(cap.isOpened())
#show image


while(cap.isOpened()):
    ret = cap.read()
    frame : np.ndarray[np.ndarray[np.ndarray[int]]] = ret[1]
    # print(type(frame[0][0][0]))
    cv2.imshow('frame', frame)
    #get contour : convolve with [[1 1 1][1 -8 1][1 1 1]]
    frame_conv = convolve.convolve_3d(np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]), frame)
    cv2.imshow('frame_conv', frame_conv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
