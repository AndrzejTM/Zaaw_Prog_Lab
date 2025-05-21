import cv2

image = cv2.imread("wiewiorka.jpg")

height, width = image.shape[:2]
resized = cv2.resize(image, (int(width * 0.5), int(height * 0.5)), interpolation=cv2.INTER_AREA)

cv2.imshow("Resized - 50%", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()