import cv2

canvas = cv2.UMat(400, 400, cv2.CV_8UC3)
canvas.get().fill(0)

cv2.rectangle(canvas, (0, 0), (100, 50), (0, 255, 0), -1)
cv2.rectangle(canvas, (300, 350), (400, 400), (0, 0, 255), 3)

cv2.imshow('Zadanie 2', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()