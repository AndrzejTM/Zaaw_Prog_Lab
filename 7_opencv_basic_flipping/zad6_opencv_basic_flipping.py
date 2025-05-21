import cv2

image = cv2.imread("wiewiorka.jpg")

print("Wybierz sposób odbicia:")
print("0 - pionowe")
print("1 - poziome")
print("-1 - oba")
choice = int(input("Twój wybór: "))

if choice in [0, 1, -1]:
    flipped = cv2.flip(image, choice)
    cv2.imshow("Wynik odbicia", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nieprawidłowy wybór. Wprowadź 0, 1 lub -1.")