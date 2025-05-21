import cv2

image = cv2.imread("wiewiorka.jpg")

flipped_h = cv2.flip(image, 1)
flipped_v = cv2.flip(image, 0)
flipped_hv = cv2.flip(image, -1)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Odbicie poziome (1)", flipped_h)
cv2.imshow("Odbicie pionowe (0)", flipped_v)
cv2.imshow("Odbicie poziome i pionowe (-1)", flipped_hv)

cv2.waitKey(0)
cv2.destroyAllWindows()