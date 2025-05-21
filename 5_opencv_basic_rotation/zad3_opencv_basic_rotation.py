import cv2

image = cv2.imread("wiewiorka.jpg")
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
(h, w) = image.shape[:2]
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 30 Degrees around (0,0)", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()