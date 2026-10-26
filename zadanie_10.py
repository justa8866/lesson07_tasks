# Lekcja 07 — Zadanie 10: Liczby pierwsze do 100

pierwsze = []
for n in range(2, 101):
    czy_pierwsza = True
    for dzielnik in range(2, int(n ** 0.5) + 1):
        if n % dzielnik == 0:
            czy_pierwsza = False
            break
    if czy_pierwsza:
        pierwsze.append(n)
print(f"Liczby pierwsze: {pierwsze}")
print(f"Liczba znalezionych liczb: {len(pierwsze)}")
