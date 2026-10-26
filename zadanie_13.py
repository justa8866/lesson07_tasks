# Lekcja 07 — Zadanie 13: Klasyfikacja kNN 1D

trening = [(1.5, 'A'), (2.3, 'A'), (3.8, 'B'), (4.2, 'B'), (5.1, 'B')]
x_nowy = 3.5
odleglosci = [(abs(x_nowy - x), klasa) for x, klasa in trening]
posortowane = sorted(odleglosci)
sasiedzi = posortowane[:3]
liczba_a = sum([1 for odleglosc, klasa in sasiedzi if klasa == 'A'])
liczba_b = sum([1 for odleglosc, klasa in sasiedzi if klasa == 'B'])
predykcja = 'A' if liczba_a > liczba_b else 'B'
print(f"Trzej najbliżsi sąsiedzi (odległość, klasa): {sasiedzi}")
print(f"Głosy: A={liczba_a}, B={liczba_b}")
print(f"Przewidywana klasa: {predykcja}")
