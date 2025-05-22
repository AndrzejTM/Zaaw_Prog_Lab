import os
import time
import xml.etree.ElementTree as ET
from paddleocr import PaddleOCR
import cv2

# 1. Wczytaj adnotacje z XML
def load_annotations(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    annotations = {}
    for image in root.findall('image'):
        filename = image.get('name')
        plate_number = None
        for box in image.findall('box'):
            for attr in box.findall('attribute'):
                if attr.get('name') == 'plate number':
                    plate_number = attr.text.strip().upper().replace(" ", "")
        if plate_number:
            annotations[filename] = plate_number
    return annotations

# 2. Obliczanie oceny końcowej
def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0
    accuracy_norm = (accuracy_percent - 60) / 40
    time_norm = (60 - processing_time_sec) / 50
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    return round(grade * 2) / 2  # zaokrąglenie do najbliższej 0.5

# 3. Inicjalizacja OCR
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False)

# 4. Ścieżki
images_folder = "photos"
annotations_file = "annotations.xml"
annotations = load_annotations(annotations_file)

# 5. Przetwarzanie maksymalnie 100 obrazów
correct = 0
total = 0
total_time = 0

for image_file in sorted(os.listdir(images_folder)):
    if total >= 100:
        break

    if not image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    image_path = os.path.join(images_folder, image_file)
    expected = annotations.get(image_file)
    if not expected:
        continue  # pomijamy obrazy bez anotacji

    # Zmierz czas przetwarzania pojedynczego obrazu
    start = time.time()

    # Wczytaj i przeskaluj do HD
    image = cv2.imread(image_path)
    if image is None:
        print(f"⚠️ Nie można wczytać: {image_file}")
        continue
    hd_image = cv2.resize(image, (1280, 720))

    # OCR na obrazie w pamięci
    result = ocr.ocr(hd_image, cls=True)
    text_results = [line[1][0] for block in result for line in block]

    end = time.time()
    total_time += (end - start)

    # Najdłuższy ciąg jako wynik
    detected = max(text_results, key=len, default='').upper().replace(" ", "").replace("-", "").replace(":", "")
    expected_clean = expected.replace("-", "").replace(" ", "").replace(":", "")
    is_correct = detected == expected_clean

    print(f"📷 {image_file} ➡️  Detected: \"{detected}\"  | Expected: \"{expected}\" {'✅' if is_correct else '❌'}")

    total += 1
    if is_correct:
        correct += 1

# 6. Ocena
accuracy = (correct / total) * 100 if total else 0
final_grade = calculate_final_grade(accuracy, total_time)

print(f"\n✅ Dokładność: {accuracy:.2f}%")
print(f"🎯 Liczba poprawnych: {correct} / {total}")
print(f"⏱️  Czas przetwarzania: {total_time:.2f} s")
print(f"🎓 Ocena końcowa (wg wzoru): {final_grade}")
