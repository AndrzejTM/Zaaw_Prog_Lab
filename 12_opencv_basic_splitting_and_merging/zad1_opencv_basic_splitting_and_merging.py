import cv2

image = cv2.imread('logo.jpg')
if image is None:
    print("Błąd: Nie można wczytać obrazu.")
    exit()

(B, G, R) = cv2.split(image)

cv2.imshow("Original Image", image)
cv2.imshow("Blue Channel", B)
cv2.imshow("Green Channel", G)
cv2.imshow("Red Channel", R)
cv2.waitKey(0)

cv2.imwrite("blue_channel.jpg", B)
cv2.imwrite("green_channel.jpg", G)
cv2.imwrite("red_channel.jpg", R)

cv2.destroyAllWindows()