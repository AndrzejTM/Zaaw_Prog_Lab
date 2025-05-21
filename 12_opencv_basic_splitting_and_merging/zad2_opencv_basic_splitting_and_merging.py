import cv2

colorful_image = cv2.imread('logo.jpg')
if colorful_image is None:
    print("Błąd: Nie można wczytać obrazu.")
    exit()

(B, G, R) = cv2.split(colorful_image)

cv2.imshow("Original Colorful Image", colorful_image)
cv2.imshow("Blue Channel - Colorful", B)
cv2.imshow("Green Channel - Colorful", G)
cv2.imshow("Red Channel - Colorful", R)
cv2.waitKey(0)

red_object = cv2.bitwise_and(colorful_image, colorful_image, mask=cv2.threshold(R, 200, 255, cv2.THRESH_BINARY)[1])
cv2.imshow("Red Object Highlighted", red_object)
cv2.waitKey(0)

cv2.destroyAllWindows()