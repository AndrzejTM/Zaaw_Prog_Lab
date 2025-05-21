import cv2

image = cv2.imread("wiewiorka.jpg")

flipped_both = cv2.flip(image, -1)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Odbicie poziome i pionowe", flipped_both)
cv2.waitKey(0)
cv2.destroyAllWindows()