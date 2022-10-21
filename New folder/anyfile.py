import cv2
import numpy as np
img = cv2.imread("poster.jpg")
rocket = img[120:360,400:500]
img[0:240,500:600]
text = "I Love Coding"
cv2.putText(img,text,(20,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255))
cv2.imshow("Display Window",img)
cv2.waitKey(0)