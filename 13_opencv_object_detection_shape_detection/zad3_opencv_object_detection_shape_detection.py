import cv2
import imutils
import numpy as np

image = cv2.imread('kostka.jpg')

widths = [200, 250, 300, 350, 400]

for width in widths:
    resized = imutils.resize(image, width=width)
    ratio = image.shape[0] / float(resized.shape[0])

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    output = image.copy()
    for c in cnts:
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(output, [c], -1, (0, 255, 0), 2)

    info = f"Width: {width}px, Contours: {len(cnts)}, Ratio: {ratio:.2f}"
    cv2.putText(output, info, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow(f"Width {width}", output)
    cv2.imwrite(f'resolution_{width}.png', output)

    areas = [cv2.contourArea(c) * (ratio ** 2) for c in cnts]
    print(f"\nAnaliza dla szerokości {width}px:")
    print(f"Liczba konturów: {len(cnts)}")
    print(f"Średni obszar: {np.mean(areas):.1f} px²")
    print(f"Min obszar: {np.min(areas):.1f} px²")
    print(f"Max obszar: {np.max(areas):.1f} px²")

    cv2.waitKey(0)
    cv2.destroyAllWindows()