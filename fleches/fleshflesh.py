import cv2
import os
import numpy as np

print(os.listdir("fleches"))

# open arrows.png

def sign(x:float) -> int:
    return 0 if x==0 else (-1 if x<0 else 1)
pic = cv2.imread("fleches/arrows2.png")

#draw the image

cv2.imshow("pic", pic)
# input()
# convert to grayscale

gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

# threshold the image

ret, thresh = cv2.threshold(gray, 127, 255, 0)

# find contours in the thresholded image

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# loop over the contours

for c in contours:
    #get the area
    area = cv2.contourArea(c)
    print(area)

    if area>10:
        [[vx],[vy],[x0],[y0]] = cv2.fitLine(c,cv2.DIST_L2,0,0.01,0.01)    #!??? the syntax sucks
        v0 = np.array([x0,y0])   # v0 is the center of the contour

        # plot the line
        x1, y1 = x0 + 100*vx, y0 + 100*vy
        v1 = np.array([x1,y1])
        x2, y2 = x0 + 100*vy, y0 - 100*vx   #orthonormal to v1
        v2 = np.array([x2,y2])
        s=0
        for v in c: #v[0] is every point of the contour, don't ask why
            s1 = v1.dot(v[0]-v0)        # scalar product between the line of our arrow and the vector of the point to indicate the direction
            s2 = abs(v2.dot(v[0]-v0))        # scalar product between v2 and our point to get the y distance in the other reper
            s+=s1*s2                    # sign depends on the side, force depends on the y and x distance 
        s=-sign(s)                       # -> sum should be positive if the arrow is in the right direction, else negative
        cv2.circle(pic,(int(x0 + 100*vx*s), int(y0 + 100*vy*s)),10,(0,255,255),5)
        cv2.line(pic, (int(x0),int(y0)), (int(x1),int(y1)), (0,0,255), 2)
        cv2.line(pic, (int(x0),int(y0)), (int(x2),int(y2)), (0,0,127), 2)


        cv2.drawContours(pic, [c], -1, (0,255,0), 2)
        cv2.imshow("pic", pic)
cv2.waitKey(0)

input()
