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

min_area = 500
max_area = 5000
filtered_cnts = []

for c in cnts:
    area = cv2.contourArea(c) * (ratio**2)
    if min_area <= area <= max_area:
        filtered_cnts.append(c)

output_before = image.copy()
output_after = image.copy()

for c in cnts:
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(output_before, [c], -1, (0, 0, 255), 2)

for c in filtered_cnts:
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(output_after, [c], -1, (0, 255, 0), 2)

info_before = f"Wszystkie kontury: {len(cnts)}"
info_after = f"Przefiltrowane kontury: {len(filtered_cnts)}"
cv2.putText(output_before, info_before, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.putText(output_after, info_after, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow("Before Filtering", output_before)
cv2.imshow("After Filtering", output_after)
cv2.imwrite('before_filtering.png', output_before)
cv2.imwrite('after_filtering.png', output_after)

cv2.waitKey(0)
cv2.destroyAllWindows()

areas = [cv2.contourArea(c) * (ratio**2) for c in cnts]
filtered_areas = [cv2.contourArea(c) * (ratio**2) for c in filtered_cnts]

print("\nAnaliza filtrowania:")
print(f"Liczba konturów przed filtrowaniem: {len(cnts)}")
print(f"Liczba konturów po filtrowaniu: {len(filtered_cnts)}")
print(f"Odrzucono {len(cnts)-len(filtered_cnts)} konturów")
print(f"Zakres obszarów przed filtrowaniem: {np.min(areas):.1f} - {np.max(areas):.1f} px²")
print(f"Zakres obszarów po filtrowaniu: {np.min(filtered_areas):.1f} - {np.max(filtered_areas):.1f} px²")