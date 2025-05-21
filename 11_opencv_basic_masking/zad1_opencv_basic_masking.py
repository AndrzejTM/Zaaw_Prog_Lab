import cv2
import numpy as np

image = cv2.imread("twarz.jfif")
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę pliku.")
    exit()

mask = np.zeros(image.shape[:2], dtype="uint8")
height, width = image.shape[:2]

face_top_left = (width//4, height//4)
face_bottom_right = (3*width//4, 3*height//4)
cv2.rectangle(mask, face_top_left, face_bottom_right, 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original Image", image)
cv2.imshow("Face Mask", mask)
cv2.imshow("Masked Face", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()