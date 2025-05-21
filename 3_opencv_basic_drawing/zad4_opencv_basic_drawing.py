import cv2

canvas = cv2.UMat(300, 300, cv2.CV_8UC3)
canvas.get().fill(0)

center = (canvas.get().shape[1] // 2, canvas.get().shape[0] // 2)
cv2.rectangle(canvas, (center[0]-50, center[1]-50),
              (center[0]+50, center[1]+50), (0, 255, 0), 2)
cv2.circle(canvas, center, 30, (0, 0, 255), -1)

cv2.imshow('Zadanie 4', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()