# Lekcja 07 — Zadanie 15: Outliers metodą IQR

wyniki = [78, 82, 85, 88, 90, 92, 95, 97, 99, 45, 101, 103, 105, 180]
posort = sorted(wyniki)
q1 = posort[len(posort) // 4]
q3 = posort[3 * len(posort) // 4]
iqr = q3 - q1
dolna = q1 - 1.5 * iqr
gorna = q3 + 1.5 * iqr
odstajace = [x for x in wyniki if x < dolna or x > gorna]
print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")
print(f"Granice: [{dolna:.2f}, {gorna:.2f}]")
print(f"Wartości odstające: {odstajace}")
