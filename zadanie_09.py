# Lekcja 07 — Zadanie 9: BMI pięciu pacjentów

wagi = [70, 85, 62, 95, 78]
wzrosty = [1.75, 1.80, 1.65, 1.78, 1.72]
for i in range(len(wagi)):
    bmi = wagi[i] / wzrosty[i] ** 2
    if bmi < 18.5:
        kategoria = "niedowaga"
    elif bmi < 25:
        kategoria = "norma"
    elif bmi < 30:
        kategoria = "nadwaga"
    else:
        kategoria = "otyłość"
    print(f"Pacjent {i + 1}: waga {wagi[i]} kg, wzrost {wzrosty[i]:.2f} m, BMI {bmi:.2f} – {kategoria}")
