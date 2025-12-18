# Lecture propre du fichier
with open('input.txt', 'r', encoding='utf-8') as fichier:
    # On sépare directement les deux blocs par la double ligne vide
    content = fichier.read().split('\n')

nbr_line = len(content)-1

table = []      # Pour la séparation de chaque élément sans les espaces

for i in range(len(content)):
    table.append(content[i].split())

result = 0
final = 0

'''
Attribution des opérateurs comme suit:
    addition = 0
    multiplication = 1
'''
operator = None       # Valeur caduque pour déclaration

for i in range(len(table[0])):          # pour parcourir chaque élément de chaque liste

    operator = table[nbr_line][i]       # on va chercher l'opérateur dans la dernière liste

    if operator == "+":
        operator = 0
    else:
        operator = 1

    for e in range(nbr_line):           # pour parcourir chaque ligne une par une
        if operator == 0:
            result += int(table[e][i])
        if operator == 1:
            if result == 0:             # pour éviter la multiplication par 0
                result = int(table[e][i])
            else:
                result *= int(table[e][i])

    final += result
    result = 0                          # réinitialiser la variable

print(final)
