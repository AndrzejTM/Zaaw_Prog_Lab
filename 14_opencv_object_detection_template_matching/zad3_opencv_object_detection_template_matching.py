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

# a. Zmiana rozmiaru oryginalnego obrazu Fanty
for scale in [0.8, 1.0, 1.2]:
    resized = cv2.resize(image, None, fx=scale, fy=scale)
    resized_gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # b. Dopasowanie tym samym szablonem
    result = cv2.matchTemplate(resized_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    (min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(result)

    # c. Obserwacja wyników
    print(f"\nDla skali {scale}:")
    print(f"Wartość dopasowania: {max_val:.4f}")

    if max_val > 0.7:
        (start_x, start_y) = max_loc
        end_x = start_x + template.shape[1]
        end_y = start_y + template.shape[0]
        cv2.rectangle(resized, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        cv2.imshow(f'Detected at scale {scale}', resized)
        cv2.waitKey(0)
    else:
        print("Detekcja nie powiodła się - zbyt niskie podobieństwo")