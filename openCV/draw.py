import cv2 as cv
import numpy as np

#painting img of a certain color

canvas = np.zeros((512, 512, 3), np.uint8) # Create a black canvas of size 512x512 pixels   
cv.imshow('Canvas', canvas) # Display the canvas
cv.imwrite('photos/black_canvas.png', canvas) # Save the canvas as a png file


# Paint the canvas a certain color
canvas[:] = 255, 0, 0 # Blue color
cv.imshow('Blue Canvas', canvas)
cv.imwrite('photos/blue_canvas.png', canvas)

cv.waitKey(0) & 0xFF == ord('d')
cv.destroyAllWindows() # Close all windows

# Ask the user which color they want to paint the canvas
ask_input = input("Enter which color you want to paint the canvas: ")

if ask_input == 'red':
    canvas[:] = 0, 0, 255 # Red color
    cv.imshow('Red Canvas', canvas)
    cv.imwrite('photos/red_canvas.png', canvas)
    cv.waitKey(0) & 0xFF == ord('d')
    cv.destroyAllWindows() # Close all windows

elif ask_input == 'green':
    canvas[:] = 0, 255, 0
    cv.imshow('Green Canvas', canvas)
    cv.imwrite('photos/green_canvas.png', canvas)
    cv.waitKey(0) & 0xFF == ord('d')
    cv.destroyAllWindows()

elif ask_input == 'yellow':
    canvas[:] = 0, 255, 255
    cv.imshow('Yellow Canvas', canvas)
    cv.imwrite('photos/yellow_canvas.png', canvas)
    cv.waitKey(0) & 0xFF == ord('d')
    cv.destroyAllWindows()

elif ask_input == 'purple':
    canvas[:] = 255, 0, 255
    cv.imshow('Purple Canvas', canvas)
    cv.imwrite('photos/purple_canvas.png', canvas)
    cv.waitKey(0) & 0xFF == ord('d')
    cv.destroyAllWindows()

elif ask_input == 'orange':
    canvas[:] = 0, 165, 255
    cv.imshow('Orange Canvas', canvas)
    cv.imwrite('photos/orange_canvas.png', canvas)
    cv.waitKey(0) & 0xFF == ord('d')
    cv.destroyAllWindows()

elif ask_input == 'pink':
    canvas[:] = 147, 20, 255
    cv.imshow('Pink Canvas', canvas)
    cv.imwrite('photos/pink_canvas.png', canvas)
    cv.waitKey(0) & 0xFF == ord('d')
    cv.destroyAllWindows()

else:
    print("Invalid color. Please enter a valid color.")
    cv.destroyAllWindows()

#enough of painting, let's draw some shapes

canvas2 = np.zeros((512, 512, 3), np.uint8) # Create a black canvas of size 512x512 pixels

#rectangle

cv.rectangle(canvas2, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED) # Draw a filled rectangle on the canvas with the specified color and thickness
cv.imshow('Rectangle', canvas2)
cv.imwrite('photos/rectangle.png', canvas2)

#circle
cv.circle(canvas2, (400, 50), 30, (255, 0, 0), thickness=cv.FILLED) # Draw a filled circle on the canvas with the specified color and thickness
cv.imshow('Circle', canvas2)
cv.imwrite('photos/circle.png', canvas2)

#line
cv.line(canvas2, (0, 0), (512, 512), (255, 255, 0), thickness=3) # Draw a line on the canvas with the specified color and thickness
cv.imshow('Line', canvas2)
cv.imwrite('photos/line.png', canvas2)

cv.putText(canvas2, 'Hello, OpenCV!', (10, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), thickness=2) # Write text on the canvas with the specified color and thickness
cv.imshow('Text', canvas2)
cv.imwrite('photos/text.png', canvas2)
