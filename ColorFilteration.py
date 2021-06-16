#Color Filteration using OpenCV and Python Libraries
import cv2
import numpy as np

device = cv2.VideoCapture(0)
while True:
    ret, frame = device.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # hsv values for red 160 t0 179
    # hsv values for blue is 110 to 170
    #the hsv values of color changes according To color band
    lower_range = np.array([160,50,50])
    upper_range = np.array([180,255,255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    #color filtering with bitwise operator
    result1 = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("show",mask)
    cv2.imshow("result", result1)
    cv2.imshow("show1", frame)

    if cv2.waitKey(1) == 15:
        break

device.release()
#following Line would exit the application after pressing enter.
cv2.destroyAllWindows()
