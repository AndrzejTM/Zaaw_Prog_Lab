import cv2
import numpy as np

image = cv2.imread('wiewiorka.jpg')

darker_numpy = image.astype(int) - 80
darker_numpy = np.clip(darker_numpy, 0, 255).astype(np.uint8)

darker_opencv = cv2.subtract(image, np.uint8([80]))

cv2.imshow('NumPy Ciemniej', darker_numpy)
cv2.imshow('OpenCV Ciemniej', darker_opencv)
cv2.waitKey(0)

cv2.imwrite('zad3_numpy_darker.jpg', darker_numpy)
cv2.imwrite('zad3_opencv_darker.jpg', darker_opencv)