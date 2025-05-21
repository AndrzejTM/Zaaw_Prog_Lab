import cv2
image = cv2.imread('wiewiorka.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Original", image)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))