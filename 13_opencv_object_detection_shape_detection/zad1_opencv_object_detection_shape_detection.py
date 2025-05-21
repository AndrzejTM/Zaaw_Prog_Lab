import cv2
import imutils
import numpy as np

image = cv2.imread('kostka.jpg')
resized = imutils.resize(image, width=300)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

for thresh_val in [100, 140, 180]:
    _, thresh = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)

    cv2.imshow(f'Threshold {thresh_val}', thresh)
    print(f"Progowanie {thresh_val}:")
    print(f"Liczba białych pikseli: {np.sum(thresh == 255)}")
    print(f"Liczba czarnych pikseli: {np.sum(thresh == 0)}")

    cv2.imwrite(f'thresh_{thresh_val}.png', thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

best_thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('best_threshold.png', best_thresh)