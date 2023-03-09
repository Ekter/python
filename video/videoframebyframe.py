"""module to decode images of a video"""
# importing the necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
# from math import abs


# Creating a VideoCapture object to read the video
cap = cv2.VideoCapture('../../../Pictures/temp_fishe/new/vid3.mp4')
SHOW = True
print(cap)
i=1
# for _ in range(1520):         # for vid1
#     i+=1
#     cap.read()
# Loop until the end of the video
list_deltas = []
list_diffs = []
list_last_pos = []
list_last_pos_shell = [0]
list_diffs_shell = []
for i in tqdm(range(0,201)):                    # range(1520,2016) for vid1     range(0,483) for vid2
    # Capture frame-by-frame
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (540, 380), fx=0, fy=0,
                    #    interpolation=cv2.INTER_CUBIC)

    # Display the resulting frame

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # find the colors within the boundaries
    mask2 = cv2.inRange(rgb, np.array([100, 0 , 0]), np.array([255, 90, 90]))
    ret,thresh = cv2.threshold(mask2,127,255,0)
    contours, _ = cv2.findContours(thresh, 1, 2)
    # print(contours[0])
    # print(f"len contours: {len(contours)}")
    # print(f"type of contours[0]: {type(contours[0])}")
    list_contours = []
    list_contours2 = []
    # a=1
    for cnt in contours:
        # print(cv2.arcLength(cnt,True))
        # print("a wild contour appeared!")
        area = cv2.contourArea(cnt)
        if area > 100:
            list_contours.append(cnt)
        # print(area)
        # if int(cv2.arcLength(cnt,True)) in range(180,210) and int(area) in range(1000, 1500):
        if area>1300:
            # cv2.drawContours(frame, [cnt], 0, (0, 255-50*a, 0), 3)
            list_contours2.append(cnt)
            # a+=1
            # print(f"passed : {area}+ arclength : {cv2.arcLength(cnt,True)}")
        # elif area > 100:
            # cv2.drawContours(frame, [cnt], 0, (255, 0, 0), 3)
            # print(f"failed : {area}+ arclength : {cv2.arcLength(cnt,True)}")

    p1=min(list_contours, key=lambda x : x[0][0][1])
    p2=min(list_contours2, key=lambda x : x[0][0][1])
    lowest_p1 = max(p1, key=lambda x : x[0][1]+x[0][0])
    highest_p2 = min(p2, key=lambda x : x[0][1]+x[0][0])
    # print(highest_p2)
    # plt.plot(np.array(lowest_p1[0])-np.array(highest_p2[0]))
    # plt.show()
    # plt.pause(0.05)
    list_deltas.append(((np.array(lowest_p1[0])-np.array(highest_p2[0]))+47+75))
    list_last_pos_shell.append(lowest_p1[0][0])
    list_diffs_shell.append(list_last_pos_shell[-1]-list_last_pos_shell[-2])

    cv2.drawContours(frame, [p1], 0, (0, 0, 255), 3)
    cv2.drawContours(frame, [p2], 0, (255, 0, 0), 3)
    frame = cv2.circle(frame, (lowest_p1[0][0], lowest_p1[0][1]), 5, (0, 255, 0), -1)
    frame = cv2.circle(frame, (highest_p2[0][0], highest_p2[0][1]), 5, (0, 255, 0), -1)

    mask3 = cv2.inRange(rgb,np.array([150, 150, 150]),np.array([255, 255, 255]))
    if SHOW:
        cv2.imshow('Thresh', mask3)

    contours2, _ = cv2.findContours(mask3, 1, 2)
    listcontours3 = []
    for cnt in contours2:
        area = cv2.contourArea(cnt)
        if area > 20 and area < 200:
            if cnt[0][0][1] in range(37,200):
                cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 3)
                listcontours3.append(cnt)
    tmplist = []
    for cnt in listcontours3:
        # list_diffs.append(list_last_pos)
        tmplist.append(cnt[0][0])
        frame = cv2.circle(frame, (cnt[0][0][0], cnt[0][0][1]), 5, (0, 255, 255), -1)
    list_last_pos.append(np.array(tmplist,dtype=object))
    # # for cnt in contours:

    # try:
    #     area = cv2.contourArea(cnt)
    #     if area > 100:
    #         cv2.drawContours(mask2, [cnt], 0, (0, 255, 0), 3)
    # except Exception:
    #     print("AssertionError")
    #     continue
    if SHOW:
        cv2.imshow('Frame', frame)

    # cv2.imshow('Thresh', mask2)
    # define q as the exit button
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    # print("img shown"+str(i))
    i+=1
# print(list_deltas)
# print(list_last_pos)
# input()
# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv2.destroyAllWindows()
plt.plot([x[1] for x in list_deltas])
lx=[]
ly=[]
lsi=[]
lsii=[]
lsiii=[]
lsii2 = []

print(len(list_last_pos))
for index,j in tqdm(enumerate(list_last_pos)):
    # si=0
    # lsii.append(sum([x[0] for x in lsi-j])/len(lsi)-list_diffs_shell[index])
    lsi = [x[0] for x in lsi]
    lsi.sort()
    lsi = np.array(lsi)
    j2 = [x[0] for x in j]
    j2.sort()
    j2 = np.array(j2)
    print("-----")
    print(lsi)
    print("---")
    print(j2)
    print("------------------")
    tmp_list = []
    for k1 in lsi:
        for k2 in j2:
            if abs(k1-k2)<20:
                tmp_list.append(k1-k2)
    lsii.append(((sum(tmp_list)/len(tmp_list)) if len(tmp_list)!=0 else 0))
    lsii2.append(((sum(tmp_list)/len(tmp_list)) if len(tmp_list)!=0 else 0)+list_diffs_shell[index])

    print(lsii[-1])
    print("----------------------------------------")


    lsiii.append(index)
    for i in j2:
        # si+=i[0]
        lx.append(index)
        ly.append(i)
    lsi = j[:]
# print(lsiii)
data_to_smooth = np.array(lsii2)
for i in range(len(data_to_smooth)):
    if abs(data_to_smooth[i])>37:
        data_to_smooth[i]=0

SMOOTH_SIZE=15
l2=[]
for i in range(len(data_to_smooth)):
    l2.append(sum(data_to_smooth[max(0,i-SMOOTH_SIZE):min(i+SMOOTH_SIZE,len(
        data_to_smooth))])/2/SMOOTH_SIZE)
print(len(l2))
celerite=(np.array(l2)/21.2*30+12)/100
#1cm=21.2px
#1s=30 frame

l_deltas=[x[1] for x in list_deltas]
l3=[]
for i in range(len(l_deltas)):
    l3.append(sum(l_deltas[max(0,i-SMOOTH_SIZE):min(i+SMOOTH_SIZE,len(
        l_deltas))])/min(2*SMOOTH_SIZE,SMOOTH_SIZE+i ,SMOOTH_SIZE-i+len(l_deltas)))
print(len(l3))
longueur = np.array(l3)/21.2



# plt.plot(lx,ly,marker = "o", linestyle = " ")
plt.plot(lsiii,data_to_smooth,"green")
plt.plot(lsiii,l2,"red")
plt.plot(list_diffs_shell,"purple")
plt.plot(l3,"black")
plt.plot(lsii,"pink")
plt.show()
plt.close()
plt.plot(celerite,"red")
plt.plot(longueur,"green")
plt.show()
print(len(l2))
print(len(list_deltas))

print("done")
# input()
