import cv2
import imutils

image = cv2.imread("wiewiorka.jpg")
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated_warp = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 60 Degrees (warpAffine)", rotated_warp)

rotated_imutils = imutils.rotate(image, 60)
cv2.imshow("Rotated by 60 Degrees (imutils.rotate)", rotated_imutils)

cv2.waitKey(0)
cv2.destroyAllWindows()