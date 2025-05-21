import cv2
import numpy as np

image = cv2.imread('logo.jpg')
if image is None:
    print("Błąd: Nie można wczytać obrazu.")
    exit()

(B_logo, G_logo, R_logo) = cv2.split(image)

merged_swapped_logo = cv2.merge([R_logo, G_logo, B_logo])

zeros = np.zeros(image.shape[:2], dtype="uint8")
merged_no_blue_logo = cv2.merge([zeros, G_logo, R_logo])
merged_no_green_logo = cv2.merge([B_logo, zeros, R_logo])
merged_no_red_logo = cv2.merge([B_logo, G_logo, zeros])

cv2.imshow("Original Logo", image)
cv2.imshow("Swapped Blue and Red", merged_swapped_logo)
cv2.imshow("No Blue Channel", merged_no_blue_logo)
cv2.imshow("No Green Channel", merged_no_green_logo)
cv2.imshow("No Red Channel", merged_no_red_logo)
cv2.waitKey(0)

cv2.imwrite("swapped_logo.jpg", merged_swapped_logo)
cv2.imwrite("no_blue_logo.jpg", merged_no_blue_logo)
cv2.imwrite("no_green_logo.jpg", merged_no_green_logo)
cv2.imwrite("no_red_logo.jpg", merged_no_red_logo)

cv2.destroyAllWindows()