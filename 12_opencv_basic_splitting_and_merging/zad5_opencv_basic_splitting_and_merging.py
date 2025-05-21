import cv2
import numpy as np

image = cv2.imread('wiewiorka.jpg')
if image is None:
    print("Błąd: Nie można wczytać obrazu.")
    exit()

(B, G, R) = cv2.split(image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170, 120, 70])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

mask = cv2.bitwise_or(mask1, mask2)

R_enhanced = cv2.add(R, 50, mask=mask)
R_final = cv2.add(R, cv2.multiply(R_enhanced, mask//255))
merged_masked = cv2.merge([B, G, R_final])

cv2.imshow("Original", image)
cv2.imshow("Mask", mask)
cv2.imshow("Selective Red Enhancement", merged_masked)
cv2.waitKey(0)

cv2.imwrite("red_mask.jpg", mask)
cv2.imwrite("selective_enhancement.jpg", merged_masked)

cv2.destroyAllWindows()