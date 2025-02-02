import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston',img)
# plt.imshow(img)
# plt.show()


# BGR to GrayScaale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to L*A*B
lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)

#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

# HSV to BGR
hsvtobgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR',hsvtobgr)





# plt.imshow(rgb)
# plt.show()


cv.waitKey(0)
