import cv2
import numpy as np
import imutils
image = cv2.imread("wiewiorka.jpg")
cv2.imshow("Oryginal", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#M = np.float32([
#[1, 0, 3000],
#[0, 1, 3000]
#])

shifted = imutils.translate(image, 100, 50)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()