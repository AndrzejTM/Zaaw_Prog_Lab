import cv2

image = cv2.imread('wiewiorka.jpg')
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

height = image.shape[0]
lower_half = image[height//2:, :]

cv2.imshow('Dolna połowa obrazu', lower_half)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('dolna_polowa.jpg', lower_half)