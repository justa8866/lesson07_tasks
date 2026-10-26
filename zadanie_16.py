# Lekcja 07 — Zadanie 16: Aproksymacja pi Leibniza

n = 1_000_000
suma = 0.0
for i in range(n):
    suma += (-1) ** i / (2 * i + 1)
pi_przyblizone = 4 * suma
pi_referencyjne = 3.141593
blad = abs(pi_przyblizone - pi_referencyjne)
print(f"Aproksymacja π: {pi_przyblizone:.6f}")
print(f"Wartość referencyjna: {pi_referencyjne:.6f}")
print(f"Błąd bezwzględny: {blad:.6f}")
