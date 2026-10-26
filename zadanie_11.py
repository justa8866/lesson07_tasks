# Lekcja 07 — Zadanie 11: Trendy sprzedaży

sprzedaz = [1200, 1350, 1290, 1480, 1520, 1510, 1680,
            1720, 1700, 1890, 1950, 2100]
wzrosty = 0
spadki = 0
suma_wzrostow_proc = 0
for i in range(1, len(sprzedaz)):
    poprzednia = sprzedaz[i - 1]
    obecna = sprzedaz[i]
    zmiana_proc = (obecna - poprzednia) / poprzednia * 100
    if zmiana_proc > 0:
        wzrosty += 1
        suma_wzrostow_proc += zmiana_proc
        print(f"Miesiąc {i + 1}: wzrost z {poprzednia} do {obecna} (+{zmiana_proc:.2f}%)")
    elif zmiana_proc < 0:
        spadki += 1
sredni_wzrost = suma_wzrostow_proc / wzrosty if wzrosty > 0 else 0
print(f"Miesiące ze wzrostem: {wzrosty}")
print(f"Miesiące ze spadkiem: {spadki}")
print(f"Średni dodatni wzrost: {sredni_wzrost:.2f}%")
