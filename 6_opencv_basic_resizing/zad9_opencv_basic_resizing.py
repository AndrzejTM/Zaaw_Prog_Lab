import cv2

image = cv2.imread("wiewiorka.jpg")

for scale in range(100, 301, 20):
    factor = scale / 100.0
    resized = cv2.resize(image, None, fx=factor, fy=factor, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(f"Resized - {scale}%", resized)
    cv2.waitKey(500)
    cv2.destroyAllWindows()