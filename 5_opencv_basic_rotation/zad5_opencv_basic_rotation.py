import cv2
import imutils

image = cv2.imread("wiewiorka.jpg")
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees (imutils.rotate)", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()