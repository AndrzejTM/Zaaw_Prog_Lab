import cv2

image = cv2.imread('wiewiorka.jpg')
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

height, width = image.shape[:2]
h_part = height // 3
w_part = width // 3

parts = []
for i in range(3):
    for j in range(3):
        part = image[i*h_part:(i+1)*h_part, j*w_part:(j+1)*w_part]
        parts.append(part)
        cv2.imwrite(f'czesc_{i+1}_{j+1}.jpg', part)

for idx, part in enumerate(parts):
    cv2.imshow(f'Część {idx//3 + 1}-{idx%3 + 1}', part)
    cv2.waitKey(500)

cv2.destroyAllWindows()