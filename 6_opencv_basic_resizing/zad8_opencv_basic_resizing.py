import cv2

image = cv2.imread("wiewiorka.jpg")

resized_cubic = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

resized_lanczos = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)

# Wyświetlenie wyników
cv2.imshow("Resized - INTER_CUBIC", resized_cubic)
cv2.imshow("Resized - INTER_LANCZOS4", resized_lanczos)
cv2.waitKey(0)
cv2.destroyAllWindows()