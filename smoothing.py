import cv2 as cv
#BLURRING

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

# Averaging --> Bu yöntem piksel yoğunluklarının ortalamasını alıp ona göre blurlaştırır.
avarage = cv.blur(img,(7,7))
cv.imshow('Avarage Blur',avarage)

#Gaussian Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur',gauss)

# Median Blur
median = cv.medianBlur(img,3)
cv.imshow('Median',median)

#Bilateral
bilateral = cv.bilateralFilter(img,10,15,15)
cv.imshow('Bilatral',bilateral)




cv.waitKey(0)

