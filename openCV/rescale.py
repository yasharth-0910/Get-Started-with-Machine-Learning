import cv2 as cv

img = cv.imread('photos/pic.jpeg') # Read an image
cv.imshow('pic', img)
cv.waitKey(0)
cv.destroyAllWindows()

# Rescale an image
def rescale(img, scale=0.5):
    width = int(img.shape[1] * scale) # img.shape[1] is the width
    height = int(img.shape[0] * scale) # img.shape[0] is the height
    dimensions = (width, height) # (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA) # Resize the image to the specified dimensions using the specified interpolation method

rescaled_img = rescale(img)

cv.imshow('Rescaled Image', rescaled_img)
cv.waitKey(0)
cv.destroyAllWindows()



# Rescale a video

capture = cv.VideoCapture('videos/output.avi')

def rescale_video(video, scale=0.5):
    while True:
        isTrue, frame = video.read()
        if isTrue:
            frame_rescaled = rescale(frame, scale)
            cv.imshow('Rescaled Video', frame_rescaled)
            if cv.waitKey(20) & 0xFF == ord('d'):
                break
        else:
            break

    video.release()
    cv.destroyAllWindows()

rescale_video(capture)
