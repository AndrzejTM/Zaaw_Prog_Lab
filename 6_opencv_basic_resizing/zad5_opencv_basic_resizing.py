import cv2
import imutils

image = cv2.imread("wiewiorka.jpg")

resized = imutils.resize(image, width=500)

cv2.imshow("Resized - Width 500", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()