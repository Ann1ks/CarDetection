import cv2
import numpy as np
from time import sleep

largura_min = 40  # Largura minima do retangulo
altura_min = 40  # Altura minima do retangulo

offset = 6  # Erro permitido entre pixel

pos_linha = 550  # Posição da linha de contagem

delay = 60  # FPS do vídeo

detec = []
carros = 0


def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


cap = cv2.VideoCapture('cars.mp4')
subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame1 = cap.read()
    tempo = float(1 / delay)
    sleep(tempo)
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)

    contorno, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.line(frame1, (470, 150), (620, 150), (255, 127, 0), 3)  # Линия пересечения
    cv2.line(frame1, (750, 340), (1400, 340), (255, 127, 0), 3)  # Линия пересечения
    cv2.line(frame1, (410, 180), (410, 280), (255, 127, 0), 3)  # Линия пересечения

    for (i, c) in enumerate(contorno):
        (x, y, w, h) = cv2.boundingRect(c)
        validar_contorno = (w >= largura_min) and (h >= altura_min)
        if not validar_contorno:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 4, (0, 0, 255), -1)

        for (x, y) in detec:#детект автомобилей
            if y < (150 + offset ) and y > (150 - offset ):
                carros += 1
                cv2.line(frame1, (470, 150), (620, 150), (255, 127, 255), 3)
                detec.remove((x, y))
                print("Автомобилей обнаружено: " + str(carros))
        '''for (x, y) in detec:#детект автомобилей
            if y < (180 ) and y > (290 ):
                carros += 1
                cv2.line(frame1, (450, 180), (700, 150), (0, 127, 255), 3)
                detec.remove((x, y))
                print("Автомобилей обнаружено: " + str(carros))
        for (x, y) in detec:#детект автомобилей
            if y < (290 ) and y > (210 ):
                carros += 1
                cv2.line(frame1, (450, 180), (700, 150), (0, 127, 255), 3)
                detec.remove((x, y))
                print("Автомобилей обнаружено: " + str(carros))
        for (x, y) in detec:#детект автомобилей
            if y < (210 ) and y > (150 ):
                carros += 1
                cv2.line(frame1, (450, 180), (700, 150), (0, 127, 255), 3)
                detec.remove((x, y))
                print("Автомобилей обнаружено: " + str(carros))'''
    cv2.putText(frame1, "CARS: " + str(carros), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv2.imshow("Video Original", frame1)
    #cv2.imshow("Detectar", dilatada)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()