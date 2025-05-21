import cv2
import numpy as np

# a. Wczytanie obrazu butelki i szablonu logo
image = cv2.imread('butelka_z_logo.JPG')
template = cv2.imread('coca_cola_logo.JPG')

# b. Konwersja do skali szarości i wykonanie template matching
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
(min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(result)

# c. Zaznaczenie wykrytego logo ramką
(start_x, start_y) = max_loc
end_x = start_x + template.shape[1]
end_y = start_y + template.shape[0]
cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

# d. Wyświetlenie wyników
print(f"Współrzędne wykrytego logo: ({start_x}, {start_y})")
print(f"Wartość dopasowania (max_val): {max_val:.4f}")

cv2.imshow('Detected Logo', image)
cv2.waitKey(0)
cv2.destroyAllWindows()