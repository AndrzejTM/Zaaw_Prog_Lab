import cv2
import numpy as np

image = cv2.imread('wiewiorka.jpg')

added_numpy = image.astype(int) + 50
added_numpy = np.clip(added_numpy, 0, 255).astype(np.uint8)

added_opencv = cv2.add(image, np.uint8([50]))

cv2.imshow('Oryginał', image)
cv2.imshow('NumPy (+50) - Zawijanie', added_numpy)
cv2.imshow('OpenCV (+50) - Obcinanie', added_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('zad1_numpy.jpg', added_numpy)
cv2.imwrite('zad1_opencv.jpg', added_opencv)