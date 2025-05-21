import cv2

image = cv2.imread('wiewiorka.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imwrite('wiewiorka_gray.jpg', image)

print("Obraz zapisany jako nowy plik.")