import cv2
import numpy as np

image = cv2.imread("twarz.jfif")
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę pliku.")
    exit()

mask = np.ones(image.shape[:2], dtype="uint8") * 255  # Biała maska (pokazuje wszystko)
height, width = image.shape[:2]

left_eye_top_left = (width//3, height//3)
left_eye_bottom_right = (width//2, height//2)
right_eye_top_left = (width//2, height//3)
right_eye_bottom_right = (2*width//3, height//2)

cv2.rectangle(mask, left_eye_top_left, left_eye_bottom_right, 0, -1)
cv2.rectangle(mask, right_eye_top_left, right_eye_bottom_right, 0, -1)

masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original Image", image)
cv2.imshow("Eye Covering Mask", mask)
cv2.imshow("Masked Eyes", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()