
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

M = np.float32([
[1, 0, 100],
[0, 1, 50]
])

shifted2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("WarpAffine Shifted Up and Left", shifted2)

shifted = imutils.translate(image, 100, 50)
cv2.imshow("Imutils Translate Up and Left", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
