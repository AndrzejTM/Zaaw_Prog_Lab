import cv2
import numpy as np

image = cv2.imread('logo.jpg')
if image is None:
    print("Błąd: Nie można wczytać obrazu.")
    exit()

(B, G, R) = cv2.split(image)

merged_swapped = cv2.merge([R, B, G])
cv2.imshow("Swapped Channels (R, B, G)", merged_swapped)

zeros = np.zeros(image.shape[:2], dtype="uint8")
merged_no_red = cv2.merge([B, G, zeros])
merged_no_green = cv2.merge([B, zeros, R])
merged_no_blue = cv2.merge([zeros, G, R])

cv2.imshow("No Red Channel", merged_no_red)
cv2.imshow("No Green Channel", merged_no_green)
cv2.imshow("No Blue Channel", merged_no_blue)
cv2.waitKey(0)

cv2.imwrite("swapped_channels.jpg", merged_swapped)
cv2.imwrite("no_red_channel.jpg", merged_no_red)
cv2.imwrite("no_green_channel.jpg", merged_no_green)
cv2.imwrite("no_blue_channel.jpg", merged_no_blue)

cv2.destroyAllWindows()