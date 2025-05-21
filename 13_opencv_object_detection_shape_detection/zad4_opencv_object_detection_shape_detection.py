import cv2
import imutils
import os
import numpy as np

if not os.path.exists('kostki'):
    os.makedirs('kostki')

image = cv2.imread('kostka.jpg')
resized = imutils.resize(image, width=300)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
ratio = image.shape[0] / float(resized.shape[0])

output = image.copy()

for i, c in enumerate(cnts):
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")

    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    cv2.putText(output, str(i + 1), (cX - 10, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    x, y, w, h = cv2.boundingRect(c)
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)
    segmented = cv2.bitwise_and(image, image, mask=mask)
    roi = segmented[y:y + h, x:x + w]

    cv2.imwrite(f'kostki/kostka_{i + 1:02d}.png', roi)

    cv2.drawContours(output, [c], -1, (0, 255, 0), 2)
    cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 1)

cv2.imwrite('numbered_bricks.png', output)
cv2.imshow("Numbered Bricks", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"\nZapisano {len(cnts)} kostek do folderu 'kostki'")