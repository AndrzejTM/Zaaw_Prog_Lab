import cv2

image = cv2.imread('twarz.jfif')
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

height, width = image.shape[:2]
print(width, height)

startX = 70
endX = 150
startY = 50
endY = 120

if not (0 <= startX < endX <= width and 0 <= startY < endY <= height):
    print("Nieprawidłowe współrzędne!")
    exit()

dynamic_roi = image[startY:endY, startX:endX]
cv2.imshow('Dynamiczny ROI', dynamic_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('dynamic_roi.jpg', dynamic_roi)