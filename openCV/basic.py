import cv2 as cv
import numpy as np

white_canvas = np.zeros((512, 512, 3), np.uint8) # Create a white canvas of size 512x512 pixels
white_canvas[:] = 255, 255, 255 # White color
cv.imshow('White Canvas', white_canvas)

cv.waitKey(0) & 0xFF == ord('d')
cv.destroyAllWindows() # Close all windows

gray = cv.cvtColor(white_canvas, cv.COLOR_BGR2GRAY) # Convert the white canvas to grayscale
cv.imshow('Gray Canvas', gray)
cv.waitKey(0) & 0xFF == ord('d')
cv.destroyAllWindows()

#blur the image
img = cv.imread('photos/pic.jpeg')
blur = cv.GaussianBlur( img , (7, 7), cv.BORDER_DEFAULT) # Apply Gaussian blur to the white canvas, with a kernel size of 7x7 which is the standard deviation in the x and y directions
cv.imshow('Blur Canvas', blur)
cv.waitKey(0) & 0xFF == ord('d')

#Edge Cascade
canny = cv.Canny(img, 125, 175) # Apply Canny edge detection to the white canvas
cv.imshow('Canny Canvas', canny)
cv.waitKey(0) & 0xFF == ord('d')
cv.destroyAllWindows()

#Dilate the image
dilated = cv.dilate(canny, (7, 7), iterations=3) # Apply dilation to the white canvas, iterations is the number of times the dilation is applied more the iterations more the dilation
cv.imshow('Dilated Canvas', dilated)
cv.waitKey(0) & 0xFF == ord('d')
cv.destroyAllWindows()

#Erode the image
eroded = cv.erode(dilated, (7, 7), iterations=3) # Apply erosion to the white canvas, iterations is the number of times the erosion is applied more the iterations more the erosion
cv.imshow('Eroded Canvas', eroded)
cv.waitKey(0) & 0xFF == ord('d')
cv.destroyAllWindows()

#Resize the image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # Resize the white canvas to 500x500 pixels
cv.imshow('Resized Canvas', resized)
cv.waitKey(0) & 0xFF == ord('d')
cv.destroyAllWindows()

#Crop the image
cropped = img[50:200, 200:400] # Crop the white canvas from (50, 200) to (200, 400)
cv.imshow('Cropped Canvas', cropped)
cv.waitKey(0) & 0xFF == ord('d')
cv.destroyAllWindows()

#Rotate the image
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45) # Rotate the white canvas by 45 degrees
cv.imshow('Rotated Canvas', rotated)
cv.waitKey(0) & 0xFF == ord('d')
cv.destroyAllWindows()

