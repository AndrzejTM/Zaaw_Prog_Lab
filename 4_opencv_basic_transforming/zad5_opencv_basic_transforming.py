
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

x = int(input("podaj przesunięcie dla x"))
y = int(input("podaj przesunięcie dla y"))

M = np.float32([
[1, 0, x],
[0, 1, y]
])

shifted2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("WarpAffine Shifted Up and Left", shifted2)

shifted = imutils.translate(image, x, y)
cv2.imshow("Imutils Translate Up and Left", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
