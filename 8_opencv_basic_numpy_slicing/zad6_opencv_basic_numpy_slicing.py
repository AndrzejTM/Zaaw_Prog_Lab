import cv2

image = cv2.imread('wiewiorka.jpg')
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

modified_image = image.copy()

fragment = modified_image[50:150, 50:150]

modified_image[200:300, 200:300] = fragment

cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Obraz z wklejonym fragmentem', modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('modified_image.jpg', modified_image)