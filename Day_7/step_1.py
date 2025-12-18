# Lecture propre du fichier
with open('input.txt', 'r', encoding='utf-8') as fichier:
    # On sépare directement les deux blocs par la double ligne vide
    content = fichier.read().split('\n')

print(content)