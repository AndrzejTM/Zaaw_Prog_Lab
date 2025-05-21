
import cv2
import imutils
import numpy as np

# a. Wczytanie zrzutu ekranu i wyodrębnienie szablonu
screenshot = cv2.imread('screenshot.png')
template = cv2.imread('kosz_template.jpg')

# Konwersja do skali szarości
screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# c. Wykonanie dopasowania
result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
locations = np.where(result >= threshold)

# d. Zaznaczenie wyników
detected = screenshot.copy()
for pt in zip(*locations[::-1]):
    cv2.rectangle(detected, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

cv2.imshow('Detected Icons', detected)
cv2.waitKey(0)
cv2.destroyAllWindows()