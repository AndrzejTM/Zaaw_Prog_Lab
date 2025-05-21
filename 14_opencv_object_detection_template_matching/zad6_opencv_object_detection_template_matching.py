import cv2
import imutils
import numpy as np
# a. Wczytanie obrazu z wieloma podobnymi obiektami
image = cv2.imread('lego_blocks.jpg')
template = cv2.imread('lego_template.jpg')

# Konwersja do skali szarości
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# c. Wykonanie dopasowania z wyższym progiem
result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
threshold = 0.9  # Wyższy próg dla mniejszej liczby fałszywych trafień
locations = np.where(result >= threshold)

# d. Zaznaczenie wyników i analiza
detected = image.copy()
for pt in zip(*locations[::-1]):
    cv2.rectangle(detected, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

print(f"Liczba wykrytych obiektów: {len(locations[0])}")
cv2.imshow('Detected Objects', detected)
cv2.waitKey(0)
cv2.destroyAllWindows()