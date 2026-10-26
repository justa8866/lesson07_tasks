# Lekcja 07 — Zadanie 5: Suma przez while

n = 50
suma = 0
i = 1
while i <= n:
    suma += i
    i += 1
wzor = n * (n + 1) // 2
print(f"Suma z pętli while: {suma}")
print(f"Suma ze wzoru: {wzor}")
print(f"Wyniki zgodne: {suma == wzor}")
