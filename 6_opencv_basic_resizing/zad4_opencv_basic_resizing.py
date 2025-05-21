import cv2

image = cv2.imread("wiewiorka.jpg")

methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]

for (name, method) in methods:
    resized = cv2.resize(image, None, fx=3, fy=3, interpolation=method)
    cv2.imshow(f"Method: {name}", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()