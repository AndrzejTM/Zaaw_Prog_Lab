import cv2
import numpy as np

image = cv2.imread('wiewiorka.jpg')

b, g, r = cv2.split(image)

r_filtered = cv2.add(r, np.uint8([30]))
g_filtered = cv2.subtract(g, np.uint8([20]))
b_filtered = cv2.add(b, np.uint8([10]))

filtered_image = cv2.merge([b_filtered, g_filtered, r_filtered])

cv2.imshow('Oryginał', image)
cv2.imshow('Filtr Instagram', filtered_image)
cv2.waitKey(0)

cv2.imwrite('zad4_instagram_filter.jpg', filtered_image)