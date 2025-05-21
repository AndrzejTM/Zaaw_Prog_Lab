
import cv2
import numpy as np

image = cv2.imread('wiewiorka.jpg')

if image is None:
    print("Błąd: Nie udało się wczytać obrazu")
else:
    pixel_1 = image[50, 50]
    pixel_2 = image[200, 200]

    pixel_1 = np.clip(pixel_1, 0, 255)
    pixel_2 = np.clip(pixel_2, 0, 255)

    b1, g1, r1 = pixel_1
    b2, g2, r2 = pixel_2

    diff_b = abs(b1 - b2)
    diff_g = abs(g1 - g2)
    diff_r = abs(r1 - r2)

    print(f'Różnica w kanale B: {diff_b}')
    print(f'Różnica w kanale G: {diff_g}')
    print(f'Różnica w kanale R: {diff_r}')
