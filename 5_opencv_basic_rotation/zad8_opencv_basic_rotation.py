import cv2

image = cv2.imread("wiewiorka.jpg")
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

rotated = image.copy()
for _ in range(3):
    M = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
    rotated = cv2.warpAffine(rotated, M, (w, h))
cv2.imshow("Sequential Rotation (3x30 Degrees)", rotated)

M = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)
rotated_single = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Single Rotation (90 Degrees)", rotated_single)

cv2.waitKey(0)
cv2.destroyAllWindows()