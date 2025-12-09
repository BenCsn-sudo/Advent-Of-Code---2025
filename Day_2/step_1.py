# Lire le fichier texte de l'input
with open('input.txt', 'r', encoding='utf-8') as fichier:
    # .read().split() va séparer automatiquement par espaces ou retours à la ligne
    instructions = fichier.read().split(',')

res = 0

for ele in instructions:
    Ids = ele.split('-')
    start = int(Ids[0])
    end = int(Ids[1])
    for i in range(start, end):
        i = str(i)
        if i[:(int(len(i)/2))] == i[(int(len(i)/2)):]:
            res += int(i)

print("Le mot de passe est: ", res)
