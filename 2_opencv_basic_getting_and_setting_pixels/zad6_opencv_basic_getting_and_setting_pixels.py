
import cv2

image = cv2.imread('wiewiorka.jpg')

if image is None:
    print("Błąd: Nie udało się wczytać obrazu")
else:
    height, width, _ = image.shape

    center_x = width // 2
    center_y = height // 2

    square_size = 100
    top_left_x = center_x - square_size // 2
    top_left_y = center_y - square_size // 2

    image[top_left_y:top_left_y + square_size, top_left_x:top_left_x + square_size] = [0, 0, 255]

    cv2.imshow('Obraz po zmianach', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
