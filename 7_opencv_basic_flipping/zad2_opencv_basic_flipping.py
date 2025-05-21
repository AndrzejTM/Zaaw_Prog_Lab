import cv2

image = cv2.imread("wiewiorka.jpg")

flipped_vertical = cv2.flip(image, 0)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Odbicie pionowe", flipped_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()