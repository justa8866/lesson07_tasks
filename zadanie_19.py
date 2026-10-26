# Lekcja 07 — Zadanie 19: Macierz przejść

stany = ['A', 'B', 'A', 'A', 'C', 'B', 'C', 'A', 'B', 'B']
unikalne = sorted(set(stany))
przejscia = {}
for s1 in unikalne:
    for s2 in unikalne:
        przejscia.setdefault(s1, {}).setdefault(s2, 0)
for i in range(len(stany) - 1):
    przejscia[stany[i]][stany[i + 1]] += 1
print('     ' + ''.join([f'{s:>5}' for s in unikalne]))
for s1 in unikalne:
    print(f'{s1:>5}' + ''.join([f'{przejscia[s1][s2]:>5}' for s2 in unikalne]))
