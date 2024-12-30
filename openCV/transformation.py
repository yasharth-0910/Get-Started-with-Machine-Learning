import cv2 as cv
import numpy as np

#translation

img = cv.imread('photos/pic.jpeg') 
cv.imshow('pic', img)
cv.waitKey(0)
cv.destroyAllWindows()

def translate(img, x, y): #x is the number of pixels to move in the x direction and y is the number of pixels to move in the y direction
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # Translation matrix for moving the image in the x and y directions
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100) # Move the image 100 pixels to the right and 100 pixels down  
cv.imshow('Translated Image', translated)
cv.waitKey(0)
cv.destroyAllWindows()

#rotation

def rotate(img, angle, rotPoint=None): #angle is the angle of rotation in degrees and rotPoint is the point around which the image is rotated
    (height, width) = img.shape[:2] # Get the height and width of the image 
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # Rotation matrix for rotating the image by the specified angle around the specified pointd
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45) # Rotate the image by 45 degrees
cv.imshow('Rotated Image', rotated)
cv.waitKey(0)
cv.destroyAllWindows()

#flip

def flip(img, flipCode): #flipCode is the code that specifies the direction in which the image is flipped
    return cv.flip(img, flipCode)

flipped = flip(img, 0) # Flip the image horizontally , 0 is the flip code for horizontal flip and 1 is the flip code for vertical flip and -1 is the flip code for both horizontal and vertical flip 
cv.imshow('Flipped Image', flipped)
cv.waitKey(0)
cv.destroyAllWindows()


