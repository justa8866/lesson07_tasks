# Lekcja 07 — Zadanie 20: Normalizacja Min-Max

dane = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
mn = dane[0]
mx = dane[0]
for x in dane:
    if x < mn:
        mn = x
    if x > mx:
        mx = x
znorm = [(x - mn) / (mx - mn) for x in dane]
print(f"Minimum: {mn}, maksimum: {mx}")
print(f"Lista znormalizowana: {znorm}")
print(f"Pierwsza wartość = 0.0: {znorm[0] == 0.0}")
print(f"Ostatnia wartość = 1.0: {znorm[-1] == 1.0}")
