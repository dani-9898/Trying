import numpy as np
import cv2
img = np.zeros([512,512,0], np.uint8)



img=cv2.line(img,(0,0), (255,255), (102,44,102), 5)
img=cv2.arrowedLine(img,(0,255), (255,255), (102,44,102), 5)
img=cv2.rectangle(img,(384,0), (510,128), (102,102,102), -3)

font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'OPENCV', (10, 500), font, 4, (255,255,255), 10, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()