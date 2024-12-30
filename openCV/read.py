import cv2 as cv

img = cv.imread('photos/pic.jpeg') # Read an image



if img is None:
    print("Error: Unable to open image. Check the file path and integrity.")
else:
    # Display an image
    cv.imshow('Image', img)
    cv.waitKey(0) # Wait for a key press

    # Save an image
    cv.imwrite('photos/pic_copy.png', img)

    # Close all windows
    cv.destroyAllWindows()
    
    # Convert an image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)
    cv.waitKey(0)
    cv.destroyAllWindows()

