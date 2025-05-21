import cv2
import numpy as np

image = cv2.imread('wiewiorka.jpg')
if image is None:
    print("Błąd: Nie można wczytać obrazu.")
    exit()

(B, G, R) = cv2.split(image)

R_enhanced = cv2.add(R, 50)
merged_enhanced_red = cv2.merge([B, G, R_enhanced])

G_enhanced = cv2.add(G, 50)
merged_enhanced_green = cv2.merge([B, G_enhanced, R])

B_enhanced = cv2.add(B, 50)
merged_enhanced_blue = cv2.merge([B_enhanced, G, R])

cv2.imshow("Enhanced Red Channel", merged_enhanced_red)
cv2.imshow("Enhanced Green Channel", merged_enhanced_green)
cv2.imshow("Enhanced Blue Channel", merged_enhanced_blue)
cv2.waitKey(0)

cv2.imwrite("enhanced_red.jpg", merged_enhanced_red)
cv2.imwrite("enhanced_green.jpg", merged_enhanced_green)
cv2.imwrite("enhanced_blue.jpg", merged_enhanced_blue)

cv2.destroyAllWindows()