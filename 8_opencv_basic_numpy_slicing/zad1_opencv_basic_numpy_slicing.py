import cv2

image = cv2.imread('wiewiorka.jpg')
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

roi = image[0:100, 0:100]

cv2.imshow('Lewy górny róg 100x100', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('roi_lewy_gorny.jpg', roi)