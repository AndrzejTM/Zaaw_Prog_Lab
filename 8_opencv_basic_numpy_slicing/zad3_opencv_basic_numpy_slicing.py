import cv2

image = cv2.imread('wiewiorka.jpg')
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

width = image.shape[1]
right_half = image[:, width//2:]

cv2.imshow('Prawa połowa obrazu', right_half)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('prawa_polowa.jpg', right_half)