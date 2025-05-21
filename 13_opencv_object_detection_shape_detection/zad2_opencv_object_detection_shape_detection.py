import cv2
import imutils

image = cv2.imread('kostka.jpg')
resized = imutils.resize(image, width=300)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]

modes = [
    (cv2.RETR_EXTERNAL, 'RETR_EXTERNAL (tylko zewnętrzne kontury)'),
    (cv2.RETR_TREE, 'RETR_TREE (pełna hierarchia)'),
    (cv2.RETR_LIST, 'RETR_LIST (wszystkie kontury bez hierarchii)'),
    (cv2.RETR_CCOMP, 'RETR_CCOMP (dwupoziomowa hierarchia)')
]

for mode, description in modes:
    cnts, hierarchy = cv2.findContours(thresh.copy(), mode, cv2.CHAIN_APPROX_SIMPLE)

    output = resized.copy()
    cv2.drawContours(output, cnts, -1, (0, 0, 255), 2)

    cv2.putText(output, description, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.putText(output, f'Liczba konturów: {len(cnts)}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('Tryb: ' + description, output)
    cv2.imwrite(f'contours_mode_{mode}.png', output)

    if hierarchy is not None:
        print(f"\nHierarchia dla {description}:")
        print(hierarchy)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

best_cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"\nNajlepszy tryb (RETR_EXTERNAL) znalazł {len(best_cnts)} konturów")