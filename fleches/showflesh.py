import cv2
import os

print(os.listdir("fleches"))

# open arrows.png

pic = cv2.imread("fleches/flech.png")

#draw the image

cv2.imshow("pic", pic)
cv2.waitKey(0)
input()

