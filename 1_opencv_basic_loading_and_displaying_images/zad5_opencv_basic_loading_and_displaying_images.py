import cv2

image1 = cv2.imread('wiewiorka.jpg')
image2 = cv2.imread('wiewiorka_gray.jpg')

cv2.imshow('Obraz 1', image1)
cv2.imshow('Obraz 2', image2)

cv2.waitKey(0)

cv2.destroyAllWindows()