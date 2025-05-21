import cv2

canvas = cv2.UMat(400, 400, cv2.CV_8UC3)
canvas.get().fill(100)  # Szare tło

# Oczy
cv2.circle(canvas, (150, 150), 20, (0, 0, 255), -1)
cv2.circle(canvas, (250, 150), 20, (0, 0, 255), -1)
# Usta
cv2.rectangle(canvas, (170, 250), (230, 260), (0, 255, 0), -1)
# Obramowanie twarzy
cv2.circle(canvas, (200, 200), 150, (255, 0, 0), 2)

cv2.imshow('Zadanie 6', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()