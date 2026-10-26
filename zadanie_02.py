# Lekcja 07 — Zadanie 2: Suma liczb dodatnich

liczby = [-5, 3, -2, 8, 12, -1, 6, 0, 15, -3]
suma = 0
licznik = 0
for liczba in liczby:
    if liczba > 0:
        suma += liczba
        licznik += 1
print(f"Suma dodatnich: {suma}")
print(f"Liczba dodatnich: {licznik}")
