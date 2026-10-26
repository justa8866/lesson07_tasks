# Lekcja 07 — Zadanie 14: Korelacja Pearsona

wzrost = [165, 170, 175, 180, 185]
waga = [60, 65, 70, 75, 80]
sr_x = sum(wzrost) / len(wzrost)
sr_y = sum(waga) / len(waga)
sum_xy = 0
sum_x2 = 0
sum_y2 = 0
for i in range(len(wzrost)):
    sum_xy += (wzrost[i] - sr_x) * (waga[i] - sr_y)
    sum_x2 += (wzrost[i] - sr_x) ** 2
    sum_y2 += (waga[i] - sr_y) ** 2
r = sum_xy / (sum_x2 * sum_y2) ** 0.5
print(f"Współczynnik korelacji Pearsona: r = {r:.4f}")
