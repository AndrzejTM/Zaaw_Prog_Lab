import cv2

canvas = cv2.UMat(300, 300, cv2.CV_8UC3)
canvas.get().fill(0)

center = (canvas.get().shape[1] // 2, canvas.get().shape[0] // 2)
cv2.line(canvas, center, (300, 300), (255, 0, 0), 2)

cv2.imshow('Zadanie 1', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()