import cv2
import imutils
import numpy as np

# a. Wczytanie obrazu butelki i szablonu logo
image = cv2.imread('butelka_z_logo.JPG')
template = cv2.imread('coca_cola_logo.JPG')

# b. Konwersja do skali szarości i wykonanie template matching
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
(min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(result)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for method in methods:
    # a. Wykonanie template matching różnymi metodami
    result = cv2.matchTemplate(image_gray, template_gray, eval(method))
    (min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(result)

    # Dla metod SQDIFF szukamy minimum
    if method in ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']:
        top_left = min_loc
        match_val = min_val
    else:
        top_left = max_loc
        match_val = max_val

    # b. Narysowanie prostokąta
    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
    detected = image.copy()
    cv2.rectangle(detected, top_left, bottom_right, (0, 255, 0), 2)

    # c. Wyświetlenie wyników
    print(f"\nMetoda: {method}")
    print(f"Wartość dopasowania: {match_val:.4f}")
    print(f"Współrzędne: {top_left}")

    cv2.imshow(method, detected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()