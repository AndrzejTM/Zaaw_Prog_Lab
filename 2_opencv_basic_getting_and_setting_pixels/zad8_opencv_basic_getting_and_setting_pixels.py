import cv2

image = cv2.imread('wiewiorka.jpg')

if image is None:
    print("Błąd: Nie udało się wczytać obrazu")
else:
    cv2.imshow('Obraz przed zmianą', image)

    image[99, :] = [0, 255, 0]

    cv2.imshow('Obraz po zmianie', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()