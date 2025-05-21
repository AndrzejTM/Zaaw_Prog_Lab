import cv2

image = cv2.imread("wiewiorka.jpg")
h, w = image.shape[:2]

right_half = image[:, w//2:]

flipped_right = cv2.flip(right_half, 1)

image[:, w//2:] = flipped_right

cv2.imshow("Oryginalny z odbitym prawym fragmentem", image)
cv2.waitKey(0)
cv2.destroyAllWindows()