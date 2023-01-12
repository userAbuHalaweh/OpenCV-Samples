import cv2 as cv

webCam = cv.VideoCapture(0)

while True:
    missionAccomplished, you = webCam.read()
    resizedYou = cv.resize(you, (400, 400))
    blurYou = cv.GaussianBlur(resizedYou, (5, 5), 0)
    cv.circle(blurYou, (20, 20), 20, (255, 255, 255), thickness=2)
    cv.circle(blurYou, (20, 380), 20, (255, 255, 255), thickness=2)
    cv.circle(blurYou, (380, 20), 20, (255, 255, 255), thickness=2)
    cv.circle(blurYou, (380, 380), 20, (255, 255, 255), thickness=2)
    youAndCircles = cv.Canny(blurYou, 80, 80)
    cv.imshow("Edge Detection", youAndCircles)
    if cv.waitKey(1) & 0xFF == ord('x'):
        break