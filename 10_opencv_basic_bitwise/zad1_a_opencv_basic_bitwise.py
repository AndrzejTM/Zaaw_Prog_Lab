import numpy as np
import cv2

image = np.zeros((300, 300), dtype="uint8")

triangle_pts = np.array([[150, 25], [25, 275], [275, 275]])
triangle = np.zeros((300, 300), dtype="uint8")
cv2.fillPoly(triangle, [triangle_pts], 255)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)

cv2.imshow("Triangle", triangle)
cv2.imshow("Circle", circle)

bitwise_and = cv2.bitwise_and(triangle, circle)
bitwise_or = cv2.bitwise_or(triangle, circle)
bitwise_xor = cv2.bitwise_xor(triangle, circle)
bitwise_not_triangle = cv2.bitwise_not(triangle)
bitwise_not_circle = cv2.bitwise_not(circle)

cv2.imshow("AND (Triangle AND Circle)", bitwise_and)
cv2.imshow("OR (Triangle OR Circle)", bitwise_or)
cv2.imshow("XOR (Triangle XOR Circle)", bitwise_xor)
cv2.imshow("NOT Triangle", bitwise_not_triangle)
cv2.imshow("NOT Circle", bitwise_not_circle)

cv2.waitKey(0)
cv2.destroyAllWindows()