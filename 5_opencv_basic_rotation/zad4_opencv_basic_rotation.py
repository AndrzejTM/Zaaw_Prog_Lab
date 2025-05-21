import cv2

image = cv2.imread("wiewiorka.jpg")
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

try:
    angle = float(input("Podaj kąt obrotu (w stopniach): "))
except ValueError:
    print("Nieprawidłowy kąt. Użyj liczby.")
    exit()

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow(f"Rotated by {angle} Degrees", rotated)

# Oczekiwanie na klawisz i zamknięcie okien
cv2.waitKey(0)
cv2.destroyAllWindows()