import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/pic.jpeg')

blank = np.zeros(img.shape[:2], dtype='uint8') 

cv.imshow('blank', blank)


#we will split the image into its BGR components

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape) #prints the shape of the image in the form of (height, width, number of channels)
print(b.shape)  #prints the shape of the blue channel in the form of (height, width)
print(g.shape)  #prints the shape of the green channel in the form of (height, width)
print(r.shape)  #prints the shape of the red channel in the form of (height, width)

#merge the BGR components back together

merged = cv.merge([b, g, r])

cv.imshow('Merged Image', merged)

cv.waitKey(0)