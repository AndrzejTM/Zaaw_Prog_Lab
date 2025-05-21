import cv2

canvas = cv2.UMat(300, 300, cv2.CV_8UC3)
canvas.get().fill(0)

center = (canvas.get().shape[1] // 2, canvas.get().shape[0] // 2)
for size in range(0, 150, 20):
    cv2.rectangle(canvas, (center[0]-size, center[1]-size),
                 (center[0]+size, center[1]+size), (255, 255, 255), 1)

cv2.imshow('Zadanie 5', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()