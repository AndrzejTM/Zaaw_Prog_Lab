import cv2

image = cv2.imread("wiewiorka.jpg")

resized = cv2.resize(image, (200, 300), interpolation=cv2.INTER_AREA)

cv2.imshow("Resized - 200x300", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()