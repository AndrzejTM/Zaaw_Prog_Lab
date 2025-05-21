import cv2
import numpy as np

image = cv2.imread('wiewiorka.jpg')

burned_numpy = image.astype(int) + 150
burned_numpy = np.clip(burned_numpy % 256, 0, 255).astype(np.uint8)

burned_opencv = cv2.add(image, np.uint8([150]))

cv2.imshow('NumPy Przepalenie', burned_numpy)
cv2.imshow('OpenCV Przepalenie', burned_opencv)
cv2.waitKey(0)

cv2.imwrite('zad2_numpy_burned.jpg', burned_numpy)
cv2.imwrite('zad2_opencv_burned.jpg', burned_opencv)