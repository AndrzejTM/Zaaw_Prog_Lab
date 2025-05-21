import cv2
import imutils

image = cv2.imread("wiewiorka.jpg")
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated Without Cropping (imutils.rotate_bound)", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()