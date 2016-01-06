import numpy as np
import cv2
from ObjectIdAssignment import find_ids_of_objects

# Constants
MIN_AREA = 1600
#MAX_AREA = 3600
MORPH_SIZE = 30

# Globals
cam = cv2.VideoCapture(1)
frame = cam.read()[1]
centroids = []


def calc_centroid(contour):
    """Returns a tuple representing the centroid of ``contour``"""
    moments = cv2.moments(contour)
    cx = int(moments['m10'] / moments['m00'])
    cy = int(moments['m01'] / moments['m00'])
    return cx, cy

while True:
    # Grab new frame
    prev_frame, frame = frame, cam.read()[1]

    frame = cv2.GaussianBlur(frame, (5,5), 0)

    # Calculate the difference between current frame and previous frame
    diff = cv2.absdiff(frame, prev_frame)

    # Create binary image of difference
    thresh = cv2.threshold(cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY),
                           1, 255, cv2.THRESH_BINARY)[1]

    # "Open" threshold image to remove noise                     
    thresh = cv2.morphologyEx(thresh,
                              cv2.MORPH_OPEN,
                              cv2.getStructuringElement(
                                  cv2.MORPH_RECT,(MORPH_SIZE,MORPH_SIZE)))

    # Find the contours of the threshold image
    contours = cv2.findContours(thresh,
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[0]
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > MIN_AREA]
    
    centroids, predicts = map(calc_centroid, contours), centroids
    
    ordered_objs = find_ids_of_objects(centroids, predicts)
    
    #cv2.drawContours(frame, contours, -1, (0,0,255), thickness=2)
    
    for i, pos in enumerate(ordered_objs, start=1):
        cv2.putText(frame, str(i), pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), thickness=2)
        
    
    # Draw bounding boxes around the contours
##    for contour in contours:
##        if cv2.contourArea(contour) > MIN_AREA:
##            centroids.append(calc_centroid(contour))
##            x, y, w, h = cv2.boundingRect(contour)
##            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)


    # Display image with contours and threshold image
    cv2.imshow('Foreground', thresh)
    cv2.imshow('Image', frame)

    # Wait 30ms. Also makes esc key exit program
    if cv2.waitKey(30) == 27:
        break

# Release resources and cleanup
cam.release()
cv2.destroyAllWindows()
