import cv2 as cv

webcam = cv.VideoCapture(0)

while True:
    missionAccomplished, img = webcam.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Mohammad Abu-Halaweh", gray)
    if cv.waitKey(20) & 0xFF == ord('x'):
        break