import cv2
import numpy as np

image = cv2.imread('pug-test.jpeg')

# apply morphology open to smooth the outline
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6,6))
morph = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# brighten dark regions
result = cv2.normalize(morph,None,20,255,cv2.NORM_MINMAX)

cv2.imshow("OPEN", morph)
cv2.imshow("RESULT", result)
cv2.waitKey(0)

#cv2.imwrite('pug-output-morph.jpg', result)

# colorReduce()
div = 24
quantized = result // div * div + div // 2

cv2.imwrite('pug-output-morph-{}.jpg'.format(div), quantized)
