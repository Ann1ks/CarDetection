import numpy as np
import cv2
import pandas as pd
from datetime import datetime, date, time

#VIDEO_URL = "http://217.21.34.252:31013/msh22-1/index.m3u8" #ЛЕНИНА
VIDEO_URL = "http://217.21.34.252:31013/mah21-1/index.m3u8" #МАХНОВИЧА
cap = cv2.VideoCapture(VIDEO_URL)
if (cap.isOpened() == False):
    print('!!! Unable to open URL')
    sys.exit(-1)

frames_count, fps, width, height = cap.get(cv2.CAP_PROP_FRAME_COUNT), cap.get(cv2.CAP_PROP_FPS), cap.get(
    cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

cars = 0
counter = 0
night = True

width = int(width)
height = int(height)
print(frames_count, fps, width, height)

sub = cv2.createBackgroundSubtractorMOG2()  # create background subtractor
# information to start saving a video file
ret, frame = cap.read()  # import image
ratio = 0.5  # resize ratio
image = cv2.resize(frame, (0, 0), None, ratio, ratio)  # resize image
width2, height2, channels = image.shape

lineypos1 = height - 725
linexpos1_start = 580/2
linexpos1_end = 740/2

lineypos2 = height - 825 + 150
linexpos2_start = int(285/2)
linexpos2_end =int(460/2)

lineypos3 = height - 725
linexpos3_start = 750
linexpos3_end =1000

lineypos4 = 450
linexpos4_start =int(1255/2)
linexpos4_end =int(1655/2)

lineypos5 = 105
linexpos5_start =int(575/2)
linexpos5_end =int(820/2)

lineypos6 = 74
linexpos6_start =int(810/2)
linexpos6_end =int(980/2)

while True:
    ret, frame = cap.read()  # import image
    now = datetime.today()
    hour = int(now.strftime("%H"))
    offset = 0
    if not ret:  # if vid finish repeat
        continue
    if ret:  # if there is a frame continue with code
        if(20<hour<7):
            night = True
            offset = 2  # погрешность
        else:
            night = False
            offset = 0
        #cv2.line(frame, (0, height - 425), (width,height - 425), (255, 0, 0), 5)#линия рисуется немного не в том месте(поправлено, уже в том), причина хуй знает
        cv2.line(frame, (580, 725), (740, 725), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (285, 825), (460, 825), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (1520, 725), (1880, 725), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (1255, 900), (1655, 900), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (575, 215), (820, 215), (255, 127, 0), 3)  # Линия пересечения
        cv2.line(frame, (810, 150), (980, 150), (255, 127, 0), 3)  # Линия пересечения

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
        maxarea = 50000
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

                    if  ((lineypos1 - offset) <= cy <= (lineypos1 + offset)) and (linexpos1_start <= cx <=linexpos1_end):  # filters out contours that are above line (y starts at top)
                    #Сделать проверку на соседние пиксели, всё будет заебок если поставить правильные условия
                        # gets bounding points of contour to create rectangle
                        # x,y is top left corner and w,h is width and height
                        x, y, w, h = cv2.boundingRect(cnt)

                        # creates a rectangle around contour
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # Prints centroid text in order to double check later on
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)

                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        cars+=1
                        print(str(cars))

                    if  ((lineypos2 - offset) <= cy <= (lineypos2 + offset)) and (linexpos2_start <= cx <=linexpos2_end):  # filters out contours that are above line (y starts at top)
                    #Сделать проверку на соседние пиксели, всё будет заебок если поставить правильные условия
                        # gets bounding points of contour to create rectangle
                        # x,y is top left corner and w,h is width and height
                        x, y, w, h = cv2.boundingRect(cnt)

                        # creates a rectangle around contour
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # Prints centroid text in order to double check later on
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)

                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        cars+=1
                        print(str(cars))

                    if  ((lineypos3 - offset) <= cy <= (lineypos3 + offset)) and (linexpos3_start <= cx <=linexpos3_end):  # filters out contours that are above line (y starts at top)
                    #Сделать проверку на соседние пиксели, всё будет заебок если поставить правильные условия
                        # gets bounding points of contour to create rectangle
                        # x,y is top left corner and w,h is width and height
                        x, y, w, h = cv2.boundingRect(cnt)

                        # creates a rectangle around contour
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # Prints centroid text in order to double check later on
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)

                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        counter+=1#перед закатом увеличивать погрешность, эту хуйню оставить(наверное)
                        if(night):
                            cars+=1
                            print(str(cars))
                        else:
                            if counter == 3:
                                cars += 1
                                print(str(cars))
                                counter = 0


                    if ((lineypos4 - offset) <= cy <= (lineypos4 + offset)) and (linexpos4_start <= cx <= linexpos4_end):  # filters out contours that are above line (y starts at top)
                        # Сделать проверку на соседние пиксели, всё будет заебок если поставить правильные условия
                        # gets bounding points of contour to create rectangle
                        # x,y is top left corner and w,h is width and height
                        x, y, w, h = cv2.boundingRect(cnt)

                        # creates a rectangle around contour
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # Prints centroid text in order to double check later on
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)

                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        cars += 1
                        print(str(cars))

                    if ((lineypos5 - offset) <= cy <= (lineypos5 + offset)) and (linexpos5_start <= cx <= linexpos5_end):  # filters out contours that are above line (y starts at top)
                        # Сделать проверку на соседние пиксели, всё будет заебок если поставить правильные условия
                        # gets bounding points of contour to create rectangle
                        # x,y is top left corner and w,h is width and height
                        x, y, w, h = cv2.boundingRect(cnt)

                        # creates a rectangle around contour
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # Prints centroid text in order to double check later on
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)

                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        cars += 1
                        print(str(cars))

                    if ((lineypos6 - offset) <= cy <= (lineypos6 + offset)) and (linexpos6_start <= cx <= linexpos6_end):  # filters out contours that are above line (y starts at top)
                        # Сделать проверку на соседние пиксели, всё будет заебок если поставить правильные условия
                        # gets bounding points of contour to create rectangle
                        # x,y is top left corner and w,h is width and height
                        x, y, w, h = cv2.boundingRect(cnt)

                        # creates a rectangle around contour
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # Prints centroid text in order to double check later on
                        cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    .3, (0, 0, 255), 1)

                        cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize=5, thickness=1,
                                       line_type=cv2.LINE_AA)
                        cars += 1
                        print(str(cars))

    cv2.imshow("countours", image)
    key = cv2.waitKey(20)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()