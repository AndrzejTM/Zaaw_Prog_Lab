import cv2

image1 = cv2.imread('wiewiorka.jpg')

if image1 is None:
    print("Błąd: Nie udało się wczytać obrazu 1")

if image1 is not None:
    cv2.namedWindow('Obraz 1', cv2.WINDOW_NORMAL)

    cv2.resizeWindow('Obraz 1', 800, 600)  # Zmieniamy rozmiar okna na 800x600

    cv2.imshow('Obraz 1', image1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()