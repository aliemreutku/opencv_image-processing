import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('boston', img)

# Translations
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    img_dimensions = (img.shape[1], img.shape[0])  # Değişken ismini değiştirdim
    return cv.warpAffine(img, transMat, img_dimensions)

# Translation
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rot_Mat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rot_Mat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)
#Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
#flip
flipped = cv.flip(img,1)
cv.imshow('Flipped',flipped)
#cropping
cropped = img[200:400,300:400]
cv.imshow('Cropped',cropped)





cv.waitKey(0)
