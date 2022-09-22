import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# image = cv.imread('../Resources/Photos/cat_large.jpg')
# cv.imshow("cat",image)
blank[200:300,200:300] = 0,150,250

cv.imshow("",blank)

cv.rectangle(blank,(0,0),(250,250),(0,150,250),thickness=2)

cv.imshow("",blank)

cv.waitKey(0) 