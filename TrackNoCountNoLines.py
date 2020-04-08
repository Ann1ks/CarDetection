import numpy as np
import cv2
import pandas as pd
from datetime import datetime
import time
from termcolor import colored

#VIDEO_URL = "http://217.21.34.252:31013/msh22-1/index.m3u8" #ЛЕНИНА
VIDEO_URL = "http://217.21.34.252:31013/mah21-1/index.m3u8" #МАХНОВИЧА
cap = cv2.VideoCapture(VIDEO_URL)
if (cap.isOpened() == False):
    print('!!! Unable to open URL')
    sys.exit(-1)

frames_count, fps, width, height = cap.get(cv2.CAP_PROP_FRAME_COUNT), cap.get(cv2.CAP_PROP_FPS), cap.get(
    cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

carsFlag = 0
carsTemp = 0
cars = 0
totalcars = 0

night = True
flag = 0
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5= 0
flag6 = 0
flag7= 0
flag8 = 0
flag9 = 0
flag10 = 0
flag11 = 0
flag12 = 0
flag13 = 0
flag14 = 0
flag15 = 0
flag16 = 0
flag17 = 0
flag18 = 0
flag19 = 0
flag20 = 0
flag21 = 0


millis = 0
millis_next = 0
temp = 0

millis1 = 0
millis_next1 = 0
temp1 = 0

millis2 = 0
millis_next2 = 0
temp2 = 0

millis3 = 0
millis_next3 = 0
temp3= 0

millis4 = 0
millis_next4 = 0
temp4 = 0

millis5 = 0
millis_next5 = 0
temp5 = 0

millis6 = 0
millis_next6 = 0
temp6= 0

millis7 = 0
millis_next7 = 0
temp7= 0

millis8 = 0
millis_next8 = 0
temp8 = 0

millis9 = 0
millis_next9 = 0
temp9 = 0

millis10 = 0
millis_next10 = 0
temp10 = 0

millis11 = 0
millis_next11 = 0
temp11 = 0

millis12 = 0
millis_next12 = 0
temp12 = 0

millis13 = 0
millis_next13 = 0
temp13 = 0

millis14 = 0
millis_next14 = 0
temp14 = 0

millis15 = 0
millis_next15 = 0
temp15 = 0

millis16 = 0
millis_next16 = 0
temp16 = 0

millis17 = 0
millis_next17 = 0
temp17 = 0

millis18 = 0
millis_next18 = 0
temp18 = 0

millis19 = 0
millis_next19 = 0
temp19 = 0

millis20 = 0
millis_next20 = 0
temp20 = 0

millis21 = 0
millis_next21 = 0
temp21 = 0

delay = 0

width = int(width)
height = int(height)
#print(frames_count, fps, width, height)

sub = cv2.createBackgroundSubtractorMOG2()  # create background subtractor
# information to start saving a video file
ret, frame = cap.read()  # import image
ratio = 0.5  # resize ratio
image = cv2.resize(frame, (0, 0), None, ratio, ratio)  # resize image
#width2, height2, channels = image.shape

lineypos0start = 580/2
lineypos0end = 610/2
linexpos0_start =  730/2
linexpos0_end = 780/2

lineypos1start = 612/2
lineypos1end = 676/2
linexpos1_start =  782/2
linexpos1_end = 910/2


lineypos2start = 760/2
lineypos2end = 800/2
linexpos2_start =  324/2
linexpos2_end = 380/2

lineypos3start = 802/2
lineypos3end = 836/2
linexpos3_start =  382/2
linexpos3_end = 438/2

lineypos4start = 444/2
lineypos4end = 490/2
linexpos4_start =  1200/2
linexpos4_end = 1254/2

lineypos5start = 422/2
lineypos5end = 446/2
linexpos5_start = 1256/2
linexpos5_end = 1284/2

lineypos6start = 390/2
lineypos6end = 424/2
linexpos6_start =  1286/2
linexpos6_end = 1320/2

lineypos7start = 366/2
lineypos7end = 392/2
linexpos7_start =  1322/2
linexpos7_end = 1356/2

lineypos8start = 846/2
lineypos8end = 900/2
linexpos8_start =  1256/2
linexpos8_end = 1360/2

lineypos9start = 800/2
lineypos9end = 848/2
linexpos9_start =  1362/2
linexpos9_end = 1430/2

lineypos10start = 756/2
lineypos10end = 802/2
linexpos10_start =  1432/2
linexpos10_end = 1500/2

lineypos11start = 308/2
lineypos11end = 324/2
linexpos11_start =  650/2
linexpos11_end = 685/2

lineypos12start = 284/2
lineypos12end = 306/2
linexpos12_start = 690/2
linexpos12_end = 734/2

lineypos13start = 256/2
lineypos13end = 280/2
linexpos13_start =  738/2
linexpos13_end = 788/2

lineypos14start = 234/2
lineypos14end = 250/2
linexpos14_start =  790/2
linexpos14_end = 834/2

lineypos15start = 208/2
lineypos15end = 224/2
linexpos15_start =  874/2
linexpos15_end = 914/2

lineypos16start = 184/2
lineypos16end = 202/2
linexpos16_start =  920/2
linexpos16_end = 960/2

lineypos17start = 166/2
lineypos17end = 180/2
linexpos17_start =  964/2
linexpos17_end = 1004/2

lineypos18start = 160/2
lineypos18end = 190/2
linexpos18_start =  1100/2
linexpos18_end = 115/2

lineypos19start = 192/2
lineypos19end = 216/2
linexpos19_start =  1162/2
linexpos19_end = 1196/2

lineypos20start = 190/2
lineypos20end = 210/2
linexpos20_start =  1300/2
linexpos20_end = 1330/2

lineypos21start = 190/2
lineypos21end = 210/2
linexpos21_start =  1390/2
linexpos21_end = 1420/2

offset = 0
while True:
    ret, frame = cap.read()  # import image
    now = datetime.today()
    hour = int(now.strftime("%H"))
    minutes = int(now.strftime("%M"))
    seconds = int(now.strftime("%S"))
    if not ret:  # if vid finish repeat
        continue
    if ret:  # if there is a frame continue with code
        if(20<hour<7):
            night = True
            delay = 90
            offset = 6
        else:
            night = False
            delay = 110

        #1 линия левее право
        cv2.line(frame, (730, 580), (780, 610), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (782, 612), (910, 675), (255, 127, 0), 3)  # Линия пересечения
        # 2 линия левее лево
        cv2.line(frame, (325, 760), (380, 800), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (382, 802), (438, 836), (255, 127, 0), 3)  # Линия пересечения
        # 3 линия право верх
        cv2.line(frame, (1200, 490), (1254, 444), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (1256, 446), (1284, 422), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (1286, 424), (1320, 390), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (1322, 392), (1356, 366), (255, 127, 0), 3)  # Линия пересечения
        # 4 линия право низ
        cv2.line(frame, (1255, 900), (1360, 846), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (1362, 848), (1430, 800), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (1432, 802), (1500, 756), (255, 127, 0), 3)  # Линия пересечения
        # 5 линия верх лево
        cv2.line(frame, (650, 325), (685, 308), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (690, 306), (734, 284), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (738, 280), (788, 256), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (790, 250), (834, 234), (255, 127, 0), 3)  # Линия пересечения
        #6 линия верх право
        cv2.line(frame, (874, 224), (914, 208), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (920, 202), (960, 184), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (964, 180), (1030, 164), (255, 127, 0), 3) # Линия пересечения
        #7 линия право левее
        cv2.line(frame, (1100, 160), (1150, 190), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (1162, 192), (1196, 216), (255, 127, 0), 3)  # Линия пересечения
        #8 линия право правее
        cv2.line(frame, (1300, 190), (1330, 210), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (1390, 190), (1420, 210), (255, 127, 0), 3)  # Линия пересечения

        image = cv2.resize(frame, (0, 0), None, ratio, ratio)  # resize image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # converts image to gray
        fgmask = sub.apply(gray)  # uses the background subtraction
        cv2.imshow("fgmask", fgmask)  # @
        #cv2.imshow("image", image)  # @
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # converts image to gray
        #cv2.imshow("gray", gray)  # @

        # applies different thresholds to fgmask to try and isolate cars
        # just have to keep playing around with settings until cars are easily identifiable
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # kernel to apply to the morphology
        closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
        #cv2.imshow("closing", closing)  # @
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
        #cv2.imshow("opening", opening)  # @
        dilation = cv2.dilate(opening, kernel)
        #cv2.imshow("dilation", dilation)  # @
        retvalbin, bins = cv2.threshold(dilation, 220, 255, cv2.THRESH_BINARY)  # removes the shadows
        #cv2.imshow("retvalbin", retvalbin)  # @
        # creates contours
        # cv2.imshow('bins',bins)
        contours, hierarchy = cv2.findContours(bins, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        minarea = 500
        # max area for contours, can be quite large for buses
        maxarea = 30000
        # vectors for the x and y locations of contour centroids in current frame
        cxx = np.zeros(len(contours))
        cyy = np.zeros(len(contours))

        for i in range(len(contours)):  # cycles through all contours in current frame
            if hierarchy[0, i, 3] == -1:  # using hierarchy to only count parent contours (contours not within others)
                area = cv2.contourArea(contours[i])  # area of contour
                if minarea < area < maxarea:  # area threshold for contour
                    # calculating centroids of contours
                    cnt = contours[i]
                    M = cv2.moments(cnt)

                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    x, y, w, h = cv2.boundingRect(cnt)
                    # creates a rectangle around contour
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # Prints centroid text in order to double check later on
                    cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, .3,
                                (0, 0, 255), 1)
                    cv2.drawMarker(image, (cx, cy), (0, 255, 255), cv2.MARKER_CROSS, markerSize=8, thickness=3,
                                   line_type=cv2.LINE_8)


                    if  (lineypos0start <= cy <= lineypos0end) and (linexpos0_start <= cx <=linexpos0_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag==0):
                            cars += 1
                            print(colored(str(cars) + " слева(правее[1])", 'green'))
                            millis = int(round(time.time() * 1000))
                            flag=1
                        if (flag == 1):
                            millis_next = int(round(time.time() * 1000))
                            temp = millis#1 пересечение
                            millis = millis_next # 2 пересечение
                        if(millis_next - temp > delay):
                         cars+=1
                         print(colored(str(cars) + " слева(правее[1])", 'green'))
                        #print(millis_next-temp)

                    if (lineypos1start <= cy <= lineypos1end) and (linexpos1_start <= cx <= linexpos1_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag1 == 0):
                            cars += 1
                            print(colored(str(cars) + " слева(правее[2])", 'green'))
                            millis1 = int(round(time.time() * 1000))
                            flag1 = 1
                        if (flag1 == 1):
                            millis_next1 = int(round(time.time() * 1000))
                            temp1 = millis1  # 1 пересечение
                            millis1 = millis_next1  # 2 пересечение
                        if (millis_next1 - temp1 > delay):
                            cars += 1
                            print(colored(str(cars) + " слева(правее[2])", 'green'))
                        #print(millis_next - temp)

                    if (lineypos2start <= cy <= lineypos2end) and (linexpos2_start <= cx <= linexpos2_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag2 == 0):
                            cars += 1
                            print(colored(str(cars) + " слева(левее[2])", 'green'))
                            millis2 = int(round(time.time() * 1000))
                            flag2 = 1
                        if (flag2 == 1):
                            millis_next2 = int(round(time.time() * 1000))
                            temp2 = millis2  # 1 пересечение
                            millis2 = millis_next2  # 2 пересечение
                        if (millis_next2 - temp2 > delay):
                            cars += 1
                            print(colored(str(cars) + " слева(левее[2])", 'green'))
                        #print(millis_next - temp)

                    if (lineypos3start <= cy <= lineypos3end) and (linexpos3_start <= cx <= linexpos3_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag3 == 0):
                            cars += 1
                            print(colored(str(cars) + " слева(левее[1])", 'green'))
                            millis3 = int(round(time.time() * 1000))
                            flag3 = 1
                        if (flag3 == 1):
                            millis_next3 = int(round(time.time() * 1000))
                            temp3 = millis3  # 1 пересечение
                            millis3 = millis_next3  # 2 пересечение
                        if (millis_next3 - temp3 > delay):
                            cars += 1
                            print(colored(str(cars) + " слева(левее[1])", 'green'))
                        #print(millis_next - temp)

                    if (lineypos4start <= cy <= lineypos4end) and (linexpos4_start <= cx <= linexpos4_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag4 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[1])", 'green'))
                            millis4 = int(round(time.time() * 1000))
                            flag4 = 1
                        if (flag4 == 1):
                            millis_next4 = int(round(time.time() * 1000))
                            temp4 = millis4  # 1 пересечение
                            millis4 = millis_next4  # 2 пересечение
                        if (millis_next4 - temp4 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[1])", 'green'))
                        #print(millis_next - temp)

                    if (lineypos5start <= cy <= lineypos5end) and (linexpos5_start <= cx <= linexpos5_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag5 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[2])", 'green'))
                            millis5 = int(round(time.time() * 1000))
                            flag5 = 1
                        if (flag5 == 1):
                            millis_next5 = int(round(time.time() * 1000))
                            temp5 = millis5  # 1 пересечение
                            millis5 = millis_next5  # 2 пересечение
                        if (millis_next5 - temp5 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[2])", 'green'))
                        #print(millis_next - temp)

                    if (lineypos6start <= cy <= lineypos6end) and (linexpos6_start <= cx <= linexpos6_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag6 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[3])", 'green'))
                            millis6 = int(round(time.time() * 1000))
                            flag6 = 1
                        if (flag6 == 1):
                            millis_next6 = int(round(time.time() * 1000))
                            temp6 = millis6  # 1 пересечение
                            millis6 = millis_next6  # 2 пересечение
                        if (millis_next6 - temp6 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[3])", 'green'))
                        #print(millis_next - temp)

                    if (lineypos7start <= cy <= lineypos7end) and (linexpos7_start <= cx <= linexpos7_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag7 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[4])", 'green'))
                            millis7 = int(round(time.time() * 1000))
                            flag7 = 1
                        if (flag7 == 1):
                            millis_next7= int(round(time.time() * 1000))
                            temp7 = millis7  # 1 пересечение
                            millis7 = millis_next7  # 2 пересечение
                        if (millis_next7 - temp7 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[4])", 'green'))
                        #print(millis_next - temp)

                    if (lineypos8start <= cy <= lineypos8end) and (linexpos8_start <= cx <= linexpos8_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag8 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(левее[3])", 'green'))
                            millis8 = int(round(time.time() * 1000))
                            flag8 = 1
                        if (flag8 == 1):
                            millis_next8 = int(round(time.time() * 1000))
                            temp8 = millis8  # 1 пересечение
                            millis8 = millis_next8  # 2 пересечение
                        if (millis_next8 - temp8 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(левее[3])", 'green'))
                        #print(millis_next - temp)

                    if (lineypos9start <= cy <= lineypos9end) and (linexpos9_start <= cx <= linexpos9_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag9 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(левее[2])", 'green'))
                            millis9 = int(round(time.time() * 1000))
                            flag9 = 1
                        if (flag9 == 1):
                            millis_next9 = int(round(time.time() * 1000))
                            temp9 = millis9  # 1 пересечение
                            millis9 = millis_next9  # 2 пересечение
                        if (millis_next9 - temp9 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(левее[2])", 'green'))
                        #print(millis_next - temp)

                    if (lineypos10start <= cy <= lineypos10end) and (linexpos10_start <= cx <= linexpos10_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag10 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(левее[1])", 'green'))
                            millis10 = int(round(time.time() * 1000))
                            flag10 = 1
                        if (flag10 == 1):
                            millis_next10 = int(round(time.time() * 1000))
                            temp10 = millis10  # 1 пересечение
                            millis10 = millis_next10  # 2 пересечение
                        if (millis_next10 - temp10 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(левее[1])", 'green'))
                        #print(millis_next - temp)

                    if ((lineypos11start - offset) <= cy <= (lineypos11end+ offset)) and (linexpos11_start <= cx <= linexpos11_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag11 == 0):
                            cars += 1
                            print(colored(str(cars) + " сверху(левее[4])", 'green'))
                            millis11 = int(round(time.time() * 1000))
                            flag11 = 1
                        if (flag11 == 1):
                            millis_next11 = int(round(time.time() * 1000))
                            temp11 = millis11  # 1 пересечение
                            millis11 = millis_next11  # 2 пересечение
                        if (millis_next11 - temp11 > delay):
                            cars += 1
                            print(colored(str(cars) + " сверху(левее[4])", 'green'))
                        # print(millis_next - temp)

                    if ((lineypos12start - offset) <= cy <= (lineypos12end+ offset)) and (linexpos12_start <= cx <= linexpos12_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag12 == 0):
                            cars += 1
                            print(colored(str(cars) + " сверху(левее[3])", 'green'))
                            millis12 = int(round(time.time() * 1000))
                            flag12 = 1
                        if (flag12 == 1):
                            millis_next12 = int(round(time.time() * 1000))
                            temp12 = millis12  # 1 пересечение
                            millis12 = millis_next12  # 2 пересечение
                        if (millis_next12 - temp12 > delay):
                            cars += 1
                            print(colored(str(cars) + " сверху(левее[3])", 'green'))
                        # print(millis_next - temp)

                    if ((lineypos13start - offset) <= cy <= (lineypos13end+ offset)) and (linexpos13_start <= cx <= linexpos13_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5,
                                       thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag13 == 0):
                            cars += 1
                            print(colored(str(cars) + " сверху(левее[2])", 'green'))
                            millis13 = int(round(time.time() * 1000))
                            flag13 = 1
                        if (flag13 == 1):
                            millis_next13 = int(round(time.time() * 1000))
                            temp13 = millis13  # 1 пересечение
                            millis13 = millis_next13  # 2 пересечение
                        if (millis_next13 - temp13 > delay):
                            cars += 1
                            print(colored(str(cars) + " сверху(левее[2])", 'green'))
                        # print(millis_next - temp)

                    if ((lineypos14start - offset) <= cy <= (lineypos14end+ offset)) and (linexpos14_start <= cx <= linexpos14_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5,
                                       thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag14 == 0):
                            cars += 1
                            print(colored(str(cars) + " сверху(левее[1])", 'green'))
                            millis14 = int(round(time.time() * 1000))
                            flag14 = 1
                        if (flag14 == 1):
                            millis_next14 = int(round(time.time() * 1000))
                            temp14 = millis14  # 1 пересечение
                            millis14 = millis_next14  # 2 пересечение
                        if (millis_next14 - temp14 > delay):
                            cars += 1
                            print(colored(str(cars) + " сверху(левее[1])", 'green'))
                        # print(millis_next - temp)

                    if ((lineypos15start - offset) <= cy <= (lineypos15end+ offset)) and (linexpos15_start <= cx <= linexpos15_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR,
                                       markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag15 == 0):
                            cars += 1
                            print(colored(str(cars) + " сверху(правее[1])", 'green'))
                            millis15 = int(round(time.time() * 1000))
                            flag15 = 1
                        if (flag15 == 1):
                            millis_next15 = int(round(time.time() * 1000))
                            temp15 = millis15  # 1 пересечение
                            millis15 = millis_next15  # 2 пересечение
                        if (millis_next15 - temp15 > delay):
                            cars += 1
                            print(colored(str(cars) + " сверху(правее[1])", 'green'))
                        # print(millis_next - temp)

                    if ((lineypos16start - offset) <= cy <= (lineypos16end+ offset)) and (linexpos16_start <= cx <= linexpos16_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR,
                                       markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag16 == 0):
                            cars += 1
                            print(colored(str(cars) + " сверху(правее[2])", 'green'))
                            millis16 = int(round(time.time() * 1000))
                            flag16 = 1
                        if (flag16 == 1):
                            millis_next16 = int(round(time.time() * 1000))
                            temp16 = millis16  # 1 пересечение
                            millis16 = millis_next16  # 2 пересечение
                        if (millis_next16 - temp16 > delay):
                            cars += 1
                            print(colored(str(cars) + " сверху(правее[2])", 'green'))
                        # print(millis_next - temp)

                    if ((lineypos17start - offset) <= cy <= (lineypos17end+ offset)) and (linexpos17_start <= cx <= linexpos17_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR,
                                       markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag17 == 0):
                            cars += 1
                            print(colored(str(cars) + " сверху(правее[3])", 'green'))
                            millis17 = int(round(time.time() * 1000))
                            flag17 = 1
                        if (flag17 == 1):
                            millis_next17 = int(round(time.time() * 1000))
                            temp17 = millis17  # 1 пересечение
                            millis17 = millis_next17  # 2 пересечение
                        if (millis_next17 - temp17 > delay):
                            cars += 1
                            print(colored(str(cars) + " сверху(правее[3])", 'green'))
                        # print(millis_next - temp)

                    if ((lineypos18start - offset) <= cy <= (lineypos18end+ offset)) and (linexpos18_start <= cx <= linexpos18_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR,
                                       markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag18 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(левее[2])", 'green'))
                            millis18 = int(round(time.time() * 1000))
                            flag18 = 1
                        if (flag18 == 1):
                            millis_next18 = int(round(time.time() * 1000))
                            temp18 = millis18  # 1 пересечение
                            millis18 = millis_next18  # 2 пересечение
                        if (millis_next18 - temp18 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(левее[2])", 'green'))
                        # print(millis_next - temp)

                    if ((lineypos19start - offset) <= cy <= (lineypos19end+ offset)) and (linexpos19_start <= cx <= linexpos19_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR,
                                       markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag19 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(левее[1])", 'green'))
                            millis19 = int(round(time.time() * 1000))
                            flag19 = 1
                        if (flag19 == 1):
                            millis_next19 = int(round(time.time() * 1000))
                            temp19 = millis19  # 1 пересечение
                            millis19 = millis_next19  # 2 пересечение
                        if (millis_next19 - temp19 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(левее[1])", 'green'))
                        # print(millis_next - temp)

                    if ((lineypos20start - offset) <= cy <= (lineypos20end+ offset)) and (linexpos20_start <= cx <= linexpos20_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR,
                                       markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag20 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[1])"),'green')
                            millis20 = int(round(time.time() * 1000))
                            flag20 = 1
                        if (flag20 == 1):
                            millis_next20 = int(round(time.time() * 1000))
                            temp20 = millis20  # 1 пересечение
                            millis20 = millis_next20  # 2 пересечение
                        if (millis_next20 - temp20 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[1])"),'green')
                        # print(millis_next - temp)

                    if ((lineypos21start - offset) <= cy <= (lineypos21end+ offset)) and (linexpos21_start <= cx <= linexpos21_end):  # filters out contours that are above line (y starts at top)
                        x, y, w, h = cv2.boundingRect(cnt)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)
                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR,
                                       markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        if (flag21 == 0):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[2])"), 'green')
                            millis21 = int(round(time.time() * 1000))
                            flag21 = 1
                        if (flag21 == 1):
                            millis_next21 = int(round(time.time() * 1000))
                            temp21 = millis21  # 1 пересечение
                            millis21 = millis_next21  # 2 пересечение
                        if (millis_next21 - temp21 > delay):
                            cars += 1
                            print(colored(str(cars) + " справа(правее[2])"), 'green')
                        # print(millis_next - temp)
    if(not carsFlag):
        carsTemp = cars
        carsFlag = 1
    if(carsFlag) and (cars!=carsTemp):
        totalcars = int(cars/2)
        if(totalcars):
            print(colored("Всего автомобилей: " + str(totalcars), 'blue'))
        carsFlag = 0

    cv2.imshow("countours", image)
    key = cv2.waitKey(20)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()