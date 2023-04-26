import cv2 
import numpy as np

image = cv2.imread("burgerking.png")
hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

colors= {

    "kirmizi":([0,50,50],[10,255,255]),
    "yesil":([36,25,25],[70,255,255]),
    "mavi":([90,50,50],[130,255,255])
    }

for color_name , (lower_color,upper_color) in colors.items():
    mask=cv2.inRange(hsv_image,np.array(lower_color),np.array(upper_color))
    result=cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow(color_name +"Renk tespiti",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
