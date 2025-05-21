import cv2

image = cv2.imread("wiewiorka.jpg")

height, width = image.shape[:2]
resized = cv2.resize(image, (int(width * 2), int(height * 2)), interpolation=cv2.INTER_LINEAR)

cv2.imshow("Resized - 2x", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()