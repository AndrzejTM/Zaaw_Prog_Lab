
import cv2

image = cv2.imread('wiewiorka.jpg')

if image is None:
    print("Błąd: Nie udało się wczytać obrazu")
else:
    height, width, _ = image.shape

    half_width = width // 2
    half_height = height // 2

    image[0:half_height, 0:half_width] = [255, 0, 0]

    cv2.imshow('Obraz po zmianach', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
