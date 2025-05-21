import cv2

image = cv2.imread('wiewiorka.jpg')
if image is None:
    print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
    exit()

height, width = image.shape[:2]
roi_width = 300
roi_height = 200
step = 10

for x in range(0, width - roi_width, step):
    roi = image[0:roi_height, x:x+roi_width]
    cv2.imshow('Przesuwający się ROI', roi)
    key = cv2.waitKey(100)
    if key == ord('q'):
        break

cv2.destroyAllWindows()