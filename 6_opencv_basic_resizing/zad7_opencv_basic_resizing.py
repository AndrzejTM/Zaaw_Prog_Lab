import cv2

image = cv2.imread("wiewiorka.jpg")

resized_area = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)

resized_linear = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Resized - INTER_AREA", resized_area)
cv2.imshow("Resized - INTER_LINEAR", resized_linear)
cv2.waitKey(0)
cv2.destroyAllWindows()