#COLOR CHANNELS
import cv2 as cv
import numpy as np


img = cv.imread('Photos/park.jpg')
cv.imshow('Boston',img)


b,g,r = cv.split(img) #bu fonksiyon ayrı ayrı renk kanalları döner.
#BUNLAR PİKSEL YOĞUNLUKLARINI GRİ TONLAMAYLA GÖSTEREN GÖSTERİMLER.
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge ile bu ayırdığımız renk kanallarını birleştirebiliriz:
merged = cv.merge([b,g,r])
cv.imshow('Merged Image',merged)

blank = np.zeros(img.shape[:2],dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow()



cv.waitKey(0)