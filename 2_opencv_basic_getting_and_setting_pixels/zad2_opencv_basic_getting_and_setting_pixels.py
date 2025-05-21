import cv2
image = cv2.imread('wiewiorka.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Original", image)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))


height, width, _ = image.shape

image[height-1, width-1] = [0, 0, 255]
(b, g, r) = image[height-1, width-1]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.imshow('Obraz po zmianie', image)

cv2.waitKey(0)
cv2.destroyAllWindows()