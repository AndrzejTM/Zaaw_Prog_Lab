import cv2
import imutils

image = cv2.imread("wiewiorka.jpg")

resized = imutils.resize(image, height=400)

cv2.imshow("Resized - Height 400", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()