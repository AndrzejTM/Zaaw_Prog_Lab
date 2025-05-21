import cv2
import imutils
import numpy as np

image = cv2.imread('kostka.jpg')
resized = imutils.resize(image, width=300)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
ratio = image.shape[0] / float(resized.shape[0])

output = image.copy()
dimensions = []

for i, c in enumerate(cnts):
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")

    x, y, w, h = cv2.boundingRect(c)
    dimensions.append((w, h))

    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    dim_text = f"{w}x{h}"
    cv2.putText(output, dim_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    dimensions[-1] = dimensions[-1] + (area, perimeter)

cv2.imwrite('brick_dimensions.png', output)
cv2.imshow("Brick Dimensions", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

widths = [d[0] for d in dimensions]
heights = [d[1] for d in dimensions]
areas = [d[2] for d in dimensions]
perimeters = [d[3] for d in dimensions]

print("\nStatystyki wymiarów kostek:")
print(f"Średnia szerokość: {np.mean(widths):.1f} ± {np.std(widths):.1f} px")
print(f"Średnia wysokość: {np.mean(heights):.1f} ± {np.std(heights):.1f} px")
print(f"Średni obszar: {np.mean(areas):.1f} ± {np.std(areas):.1f} px²")
print(f"Średni obwód: {np.mean(perimeters):.1f} ± {np.std(perimeters):.1f} px")
print(f"Min wymiary: {np.min(widths)}x{np.min(heights)} px")
print(f"Max wymiary: {np.max(widths)}x{np.max(heights)} px")