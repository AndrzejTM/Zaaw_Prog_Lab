import cv2
import numpy as np
import imutils


def preprocess_image(image):
    """Przetwarzanie wstępne obrazu przed wykrywaniem konturów"""
    # Konwersja do skali szarości
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Rozmycie Gaussa do redukcji szumów
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Binaryzacja - metoda Otsu automatycznie dobiera próg
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Operacje morfologiczne - zamknięcie i otwarcie
    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    return opening


def find_potential_objects(image, min_area=500, max_area=50000):
    """Znajdowanie konturów potencjalnych obiektów"""
    # Znajdowanie konturów
    contours, _ = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtrowanie konturów na podstawie powierzchni
    filtered_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if min_area < area < max_area:
            filtered_contours.append(cnt)

    return filtered_contours


def template_matching_for_contours(main_image, contours, template, threshold=0.8):
    """Wykonanie template matching dla każdego wyciętego fragmentu"""
    # Konwersja szablonu do skali szarości
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]

    # Kopia obrazu do rysowania wyników
    result_image = main_image.copy()
    matches = []

    for i, contour in enumerate(contours):
        # Pobranie współrzędnych prostokąta otaczającego kontur
        x, y, w_ctr, h_ctr = cv2.boundingRect(contour)

        # Sprawdzenie czy kontur jest odpowiednio duży
        if w_ctr > w and h_ctr > h:
            # Wycięcie regionu zainteresowania (ROI)
            roi = main_image[y:y + h_ctr, x:x + w_ctr]
            roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            # Wykonanie template matching
            res = cv2.matchTemplate(roi_gray, template_gray, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            # Jeśli dopasowanie przekracza próg
            if max_val > threshold:
                matches.append({
                    'contour_id': i,
                    'contour_area': cv2.contourArea(contour),
                    'match_value': max_val,
                    'bounding_box': (x, y, w_ctr, h_ctr),
                    'template_size': (w, h)
                })

                # Narysowanie prostokąta wokół dopasowanego obiektu
                cv2.rectangle(result_image, (x, y), (x + w_ctr, y + h_ctr), (0, 255, 0), 2)
                cv2.putText(result_image, f"Match: {max_val:.2f}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return result_image, matches


def main():
    # Wczytanie głównego obrazu i szablonu
    main_image = cv2.imread('lego_blocks.jpg')  # Obraz z wieloma obiektami
    template = cv2.imread('lego_template.jpg')  # Szablon obiektu do znalezienia

    # Sprawdzenie czy obrazy zostały poprawnie wczytane
    if main_image is None or template is None:
        print("Błąd: Nie można wczytać obrazów. Sprawdź ścieżki plików.")
        return

    # 1. Przetwarzanie wstępne obrazu
    processed_image = preprocess_image(main_image)

    # 2. Znajdowanie potencjalnych obiektów (konturów)
    contours = find_potential_objects(processed_image)
    print(f"Znaleziono {len(contours)} potencjalnych obiektów")

    # 3. Wykonanie template matching dla każdego konturu
    result_image, matches = template_matching_for_contours(main_image, contours, template)

    # Wyświetlenie wyników
    print(f"\nZnaleziono {len(matches)} dopasowań powyżej progu:")
    for match in matches:
        print(f"- Kontur {match['contour_id']}: wartość dopasowania = {match['match_value']:.4f}, "
              f"powierzchnia = {match['contour_area']}, pozycja = {match['bounding_box']}")

    # Wyświetlenie obrazu wynikowego
    cv2.imshow('Original Image', imutils.resize(main_image, width=800))
    cv2.imshow('Processed Image', imutils.resize(processed_image, width=800))
    cv2.imshow('Detection Results', imutils.resize(result_image, width=800))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()