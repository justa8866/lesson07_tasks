# Lekcja 07 — Zadanie 8: Konwersja wzrostów

wzrosty_cm = [165, 178, 182, 159, 171, 190]
wzrosty_m = [wzrost / 100 for wzrost in wzrosty_cm]
print(f"Wzrosty w cm: {wzrosty_cm}")
print(f"Wzrosty w m: {wzrosty_m}")
