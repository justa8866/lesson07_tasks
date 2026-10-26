# Lekcja 07 — Zadanie 6: Gorączka

temperatury = [36.5, 37.8, 36.2, 38.5, 36.9, 39.2, 37.0]
liczba_goraczek = 0
for temperatura in temperatury:
    if temperatura >= 38.0:
        print(f"gorączka: {temperatura:.1f}°C")
        liczba_goraczek += 1
odsetek = liczba_goraczek / len(temperatury) * 100
print(f"Odsetek przypadków z gorączką: {odsetek:.2f}%")
