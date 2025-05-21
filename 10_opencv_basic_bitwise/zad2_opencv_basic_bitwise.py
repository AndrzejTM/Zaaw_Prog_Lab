import numpy as np
import cv2

def create_similar_images():
    img1 = np.zeros((300, 300), dtype="uint8")
    cv2.rectangle(img1, (50, 50), (250, 250), 255, -1)

    img2 = img1.copy()
    cv2.rectangle(img2, (100, 100), (150, 150), 0, -1)

    return img1, img2

image1, image2 = create_similar_images()

cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)

diff = cv2.bitwise_xor(image1, image2)

_, diff_thresh = cv2.threshold(diff, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("XOR Difference", diff)
cv2.imshow("XOR Difference with Threshold", diff_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

