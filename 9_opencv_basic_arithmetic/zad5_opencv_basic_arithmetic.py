import cv2

image1 = cv2.imread('wiewiorka.jpg')
image2 = cv2.imread('wiewiorka_gray.jpg')

difference = cv2.absdiff(image1, image2)

gray_diff = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
_, threshold_diff = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

cv2.imshow('Obraz 1', image1)
cv2.imshow('Obraz 2', image2)
cv2.imshow('Różnica', difference)
cv2.imshow('Binaryzacja różnicy', threshold_diff)
cv2.waitKey(0)

cv2.imwrite('zad5_difference.jpg', difference)
cv2.imwrite('zad5_threshold_diff.jpg', threshold_diff)