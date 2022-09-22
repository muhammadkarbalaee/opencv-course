import cv2 as cv

image = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow("cat",image)
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("yes",gray)

# bluring
# blur = cv.GaussianBlur(image,(3,3))
cv.waitKey(0) 