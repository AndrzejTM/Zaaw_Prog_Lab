import cv2

image_gray = cv2.imread("wiewiorka.jpg", cv2.IMREAD_GRAYSCALE)
if image_gray is None:
    print("Błąd: Nie udało się załadować obrazu.")
else:
    cv2.imshow("Obraz w skali szarości", image_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    (h, w) = image_gray.shape
    print(f'width: {w} pixels')
    print(f'height: {h} pixels')
    print('channels: 1 (skala szarości)')
