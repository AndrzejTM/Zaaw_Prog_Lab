import cv2
import imutils
import numpy as np

image = cv2.imread('kostka.jpg')
resized = imutils.resize(image, width=300)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
ratio = image.shape[0] / float(resized.shape[0])

# Filtrowanie
filtered_cnts = []
min_area, max_area = 500, 5000

for c in cnts:
    area = cv2.contourArea(c) * (ratio ** 2)
    if min_area <= area <= max_area:
        filtered_cnts.append(c)

# Obliczanie statystyk
dimensions = []
for c in filtered_cnts:
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    x, y, w, h = cv2.boundingRect(c)
    area = cv2.contourArea(c)
    dimensions.append((w, h, area))

# Przygotowanie raportu
widths = [d[0] for d in dimensions]
heights = [d[1] for d in dimensions]
areas = [d[2] for d in dimensions]

report = f"""
=== RAPORT KOŃCOWY ===

1. Podstawowe statystyki:
   - Liczba wykrytych kostek: {len(filtered_cnts)}
   - Srednia szerokosc: {np.mean(widths):.1f} ± {np.std(widths):.1f} px
   - Srednia wysokosc: {np.mean(heights):.1f} ± {np.std(heights):.1f} px
   - Sredni obszar: {np.mean(areas):.1f} ± {np.std(areas):.1f} px²

2. Zakresy wymiarow:
   - Minimalna szerokosc: {np.min(widths)} px
   - Maksymalna szerokosc: {np.max(widths)} px
   - Minimalna wysokosc: {np.min(heights)} px
   - Maksymalna wysokosc: {np.max(heights)} px
   - Minimalny obszar: {np.min(areas):.1f} px²
   - Maksymalny obszar: {np.max(areas):.1f} px²

3. Procentowe roznice:
   - Roznica min/max szerokosci: {(np.max(widths) - np.min(widths)) / np.mean(widths) * 100:.1f}%
   - Roznica min/max wysokosci: {(np.max(heights) - np.min(heights)) / np.mean(heights) * 100:.1f}%
   - Roznica min/max obszaru: {(np.max(areas) - np.min(areas)) / np.mean(areas) * 100:.1f}%

4. Wspolczynniki ksztaltu:
   - Sredni stosunek wysokosci do szerokosci: {np.mean([h / w for w, h in zip(widths, heights)]):.3f}
   - Odchylenie standardowe stosunku: {np.std([h / w for w, h in zip(widths, heights)]):.3f}
"""

print(report)

# Zapis raportu do pliku (z kodowaniem UTF-8)
with open('raport_kostek.txt', 'w', encoding='utf-8') as f:
    f.write(report)

# Wizualizacja wyników
output = image.copy()
for i, c in enumerate(filtered_cnts):
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")

    # Rysowanie konturu i numeru
    cv2.drawContours(output, [c], -1, (0, 255, 0), 2)
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.putText(output, str(i + 1), (cX - 10, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

# Dodanie podsumowania
summary = f"Kostki: {len(filtered_cnts)}, Sr. wymiar: {np.mean(widths):.0f}x{np.mean(heights):.0f} px"
cv2.putText(output, summary, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

cv2.imwrite('final_result.png', output)
cv2.imshow("Final Result", output)
cv2.waitKey(0)
cv2.destroyAllWindows()