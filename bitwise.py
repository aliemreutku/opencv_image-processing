#BITWISE OPERATIONS
import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle =  cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#bitwise AND ---> Aslında yaptığı işlev iki görüntüyü
# bilreştiricek bir nevi ortak kümenin görüntüsü gibi.
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise_and',bitwise_and)

#bitwise OR --->Bu operatörün yaptığıda birleşim kümesini almak gibi.
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR',bitwise_or)

#bitwise XOR ----> Bu operatörde KESİŞMEYEN noktaları bulur.
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR',bitwise_xor)

#bitwise NOT --->Bu da görseldeki olmayan noktaları gösterir(BİR NEVİ TERS RENK..)
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('NOT',bitwise_not)


cv.waitKey(0)