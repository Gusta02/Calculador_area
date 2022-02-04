from sqlite3 import paramstyle
import cv2
from detector_objetos import *
import numpy as np 


# Load aruco detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)


img = cv2.imread('phone_aruco_marker.jpg')

corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

int_corners = np.int0(corners)
print(int_corners)

cv2.polylines(img, int_corners, True, (0, 255, 0), 5)


# Aruco Perimeter
aruco_perimeter = cv2.arcLength(corners, True)
print(aruco_perimeter)


# carrega detector de objetos
detector = HomogeneousBgDetector()

contours = detector.detect_objects(img)

# Draw objects boundaries
for cnt in contours:

    # # Draw polygon 
    # cv2.polylines(img, [cnt], True, (255, 0, 0), 2)

    # get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect


    # Dispaly retangular
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {}".format(round(w, 1)), (int(x - 100), int(y - 30)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, "Height {}".format(round(h, 1)), (int(x - 100), int(y + 30)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)





#load Image
cv2.imshow("Image", img)
cv2.waitKey(0)