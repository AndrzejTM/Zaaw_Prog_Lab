import cv2
image = cv2.imread('wiewiorka.jpg')

height, width, _ = image.shape

center_x = width // 2
center_y = height // 2

center_pixel_value = image[center_y, center_x]

print(f'Wartość piksela w środku obrazu: {center_pixel_value}')