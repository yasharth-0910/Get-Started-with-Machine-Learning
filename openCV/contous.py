import cv2 as cv
import numpy as np

img = cv.imread('photos/pic.jpeg')
cv.imshow('pic', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # Find the contours in the image using the Canny edge detection image 
# cv.RETR_LIST retrieves all of the contours and does not create any parent-child relationship between them
# cv.CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments and leaves only their end points
print(f'{len(contours)} contour(s) found!')

cv.drawContours(img, contours, -1, (0, 0, 255), 1) # Draw the contours on the image
cv.imshow('Contours', img)

#background removal from the image
img2 = cv.imread('photos/pic.jpeg')

blank = np.zeros(img2.shape[:2], dtype='uint8')  # Create a blank mask
cv.drawContours(blank, contours, -1, 255, thickness=cv.FILLED)  # Fill contours to create mask
masked = cv.bitwise_and(img2, img2, mask=blank)  # Apply mask to remove background
cv.imshow('Masked Image', masked)


#thresholding
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # Apply thresholding to the grayscale image to get a binary image here 125 is the threshold value and 255 is the maximum value meaning that if the pixel value is greater than 10 then it is set to 255 else it is set to 0
cv.imshow('Thresholded Image', thresh)

print('Thresholded Image:', ret)


cv.waitKey(0)


