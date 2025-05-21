import cv2

image = cv2.imread('wiewiorka.jpg')
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

cropped = image[0:300, 0:300]

cv2.imshow('Przycięty obraz', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cropped_image.jpg', cropped)
print("Przycięty obraz został zapisany jako 'cropped_image.jpg'")