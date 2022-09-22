import cv2 as cv

# image = cv.imread('../Resources/Photos/cat_large.jpg')
# cv.imshow("cat",image)

capture = cv.VideoCapture("../Resources/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("yes",frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()