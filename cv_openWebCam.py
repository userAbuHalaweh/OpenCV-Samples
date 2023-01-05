import cv2 as cv

webcam = cv.VideoCapture(0)

while True:
    missionAccomplished, img = webcam.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    re_gray = cv.resize(gray, (800, 600))
    cv.putText(re_gray, "What's good, Mohammad?", (100, 400), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
    cv.imshow("Mohammad Abu-Halaweh", re_gray)
    if cv.waitKey(20) & 0xFF == ord('x'):
        break