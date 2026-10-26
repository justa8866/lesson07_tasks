# Lekcja 07 — Zadanie 17: Algorytm Euklidesa NWD

a = 252
b = 105
iteracje = 0
while b != 0:
    a, b = b, a % b
    iteracje += 1
print(f"NWD = {a}")
print(f"Liczba iteracji = {iteracje}")
