import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


image = cv.imread('../Resources/Photos/cat.jpg')
 
resized = rescaleFrame(image,0.5)

cv.imshow("",resized)

cv.waitKey(0)