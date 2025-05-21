import cv2
import numpy as np

image = cv2.imread("wiewiorka.jpg")
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę pliku.")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])  
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red, upper_red)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

dark_background = np.zeros_like(image)

masked = cv2.bitwise_and(image, image, mask=mask)
result = cv2.add(masked, dark_background)

cv2.imshow("Original Image", image)
cv2.imshow("Color Mask", mask)
cv2.imshow("Extracted Color", result)
cv2.waitKey(0)
cv2.destroyAllWindows()