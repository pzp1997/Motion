import numpy as np
import cv2

# Constants
MIN_AREA = 1600
MORPH_SIZE = 20

# Globals
cam = cv2.VideoCapture(1)
frame = cam.read()[1]

while True:
    # Grab new frame
    prev_frame, frame = frame, cam.read()[1]

    # Calculate the difference between current frame and previous frame
    diff = cv2.absdiff(frame, prev_frame)

    # Create binary image of difference
    thresh = cv2.threshold(cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY),
                           1, 255, cv2.THRESH_BINARY)[1]
    
##    thresh = cv2.erode(thresh,
##                       cv2.getStructuringElement(cv2.MORPH_RECT,(20,20)))
##    thresh = cv2.dilate(thresh,
##                        cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))

    # "Open" threshold image to remove noise                     
    thresh = cv2.morphologyEx(thresh,
                              cv2.MORPH_OPEN,
                              cv2.getStructuringElement(
                                  cv2.MORPH_RECT,(MORPH_SIZE,MORPH_SIZE)))

    # Find the contours of the threshold image
    contours = cv2.findContours(thresh,
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[0]

    # Draw bounding boxes around the contours
    contour_count = 0
    for contour in contours:
        if cv2.contourArea(contour) > MIN_AREA:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
            contour_count += 1
    print contour_count

##    cv2.drawContours(frame, contours, -1, (255,0,0), 3)

    # Display image with contours and threshold image
    cv2.imshow('Foreground', thresh)
    cv2.imshow('Image', frame)

    # Wait 30ms. Also makes esc key exit program
    if cv2.waitKey(30) == 27:
        break

# Release resources and cleanup
cam.release()
cv2.destroyAllWindows()
