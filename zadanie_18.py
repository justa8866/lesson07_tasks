# Lekcja 07 — Zadanie 18: Histogram binning

dane = [12, 15, 18, 22, 25, 28, 31, 35, 38, 42, 45, 48, 52, 55, 58]
granice = [10, 20, 30, 40, 50, 60]
biny = [0, 0, 0, 0, 0]
for x in dane:
    for i in range(5):
        if granice[i] <= x < granice[i + 1]:
            biny[i] += 1
            break
for i in range(5):
    przedzial = f"[{granice[i]}, {granice[i + 1]})"
    print(f"{przedzial:<12} {'*' * biny[i]}")
