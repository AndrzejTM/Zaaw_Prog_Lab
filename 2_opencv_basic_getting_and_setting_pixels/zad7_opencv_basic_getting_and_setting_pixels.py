import cv2

image = cv2.imread('wiewiorka.jpg')

if image is None:
    print("Błąd: Nie udało się wczytać obrazu")
else:
    height, width, _ = image.shape

    part_width = width // 3
    part_height = height // 3

    center_x = part_width
    center_y = part_height

    cropped_image = image[part_height:2*part_height, part_width:2*part_width]

    cv2.imshow('Wycięty fragment', cropped_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()