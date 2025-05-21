import cv2
import imutils

image = cv2.imread("wiewiorka.jpg")

resized = imutils.resize(image, width=800)

cv2.imwrite("resized_output.jpg", resized)

cv2.imshow("Resized - Width 800", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()