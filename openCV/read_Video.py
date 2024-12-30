import cv2 as cv
import os

# Create videos directory if it doesn't exist
os.makedirs('videos', exist_ok=True)

# Read a video
capture = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('videos/output.avi', fourcc, 20.0, 
                     (int(capture.get(3)), int(capture.get(4))))

while True:
    isTrue, frame = capture.read()
    if isTrue:
        out.write(frame)
        cv.imshow('Video', frame)

    # Break the loop if 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
out.release()
cv.destroyAllWindows()
