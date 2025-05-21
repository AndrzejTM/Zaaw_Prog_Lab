import numpy as np
import cv2

def draw_triangle(image, center_x, center_y, size):
    pts = np.array([
        [center_x, center_y - size],
        [center_x - size, center_y + size],
        [center_x + size, center_y + size]
    ])
    cv2.fillPoly(image, [pts], 255)
    return image

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 100, 255, -1)

positions = [
    (100, 100),
    (200, 100),
    (150, 150),
    (100, 200),
    (200, 200)
]

for i, (x, y) in enumerate(positions):
    triangle = np.zeros((300, 300), dtype="uint8")
    triangle = draw_triangle(triangle, x, y, 50)

    bitwise_and = cv2.bitwise_and(triangle, circle)
    bitwise_or = cv2.bitwise_or(triangle, circle)
    bitwise_xor = cv2.bitwise_xor(triangle, circle)

    cv2.imshow(f"Triangle position {i + 1}", triangle)
    cv2.imshow(f"AND position {i + 1}", bitwise_and)
    cv2.imshow(f"OR position {i + 1}", bitwise_or)
    cv2.imshow(f"XOR position {i + 1}", bitwise_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()