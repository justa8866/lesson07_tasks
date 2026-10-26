# Lekcja 07 — Zadanie 12: Walidacja numeru PESEL

numery = ['92041812345', '8501015432', 'abc123', '78121698765']
for pesel in numery:
    if len(pesel) == 11 and pesel.isdigit():
        print(f"PESEL {pesel}: poprawny format")
    elif len(pesel) != 11:
        print(f"PESEL {pesel}: błędny format (długość {len(pesel)})")
    else:
        print(f"PESEL {pesel}: błędny format (znaki inne niż cyfry)")
