import cv2

image = cv2.imread('wiewiorka.jpg')

height, width, _ = image.shape
try:
    x = int(input(f"Podaj współrzędną X (szerokość obrazu: 0 do {width - 1}): "))
    y = int(input(f"Podaj współrzędną Y (wysokość obrazu: 0 do {height - 1}): "))

    if 0 <= x < width and 0 <= y < height:

        image[y, x] = [0, 0, 0]
        print(f'Piksel na ({x}, {y}) został ustawiony na czarny.')


        cv2.imshow('Obraz po zmianie', image)


        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Błąd: Współrzędne są poza zakresem obrazu.")

except ValueError:
    print("Błąd: Podano nieprawidłową wartość. Upewnij się, że wpisujesz liczby całkowite.")