import cv2

image = cv2.imread('wiewiorka.jpg')
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

print("Podaj współrzędne ROI (startX, endX, startY, endY):")
startX = int(input("startX: "))
endX = int(input("endX: "))
startY = int(input("startY: "))
endY = int(input("endY: "))

height, width = image.shape[:2]
if not (0 <= startX < endX <= width and 0 <= startY < endY <= height):
    print("Nieprawidłowe współrzędne!")
    exit()

dynamic_roi = image[startY:endY, startX:endX]
cv2.imshow('Dynamiczny ROI', dynamic_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zapis wynikowego ROI
cv2.imwrite('dynamic_roi.jpg', dynamic_roi)