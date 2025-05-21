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
# a. Obrót obrazu o 30° i 45°
for angle in [30, 45]:
    rotated = imutils.rotate(image, angle)
    rotated_gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)

    # b. Powtórzenie detekcji logo
    result = cv2.matchTemplate(rotated_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    (min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(result)

    # c. Interpretacja wyników
    print(f"\nDla obrotu {angle}°:")
    print(f"Wartość dopasowania (max_val): {max_val:.4f}")

    if max_val > 0.7:  # przykładowy próg
        (start_x, start_y) = max_loc
        end_x = start_x + template.shape[1]
        end_y = start_y + template.shape[0]
        cv2.rectangle(rotated, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        cv2.imshow(f'Detected at {angle}°', rotated)
        cv2.waitKey(0)
    else:
        print("Detekcja nie powiodła się - zbyt niskie podobieństwo")