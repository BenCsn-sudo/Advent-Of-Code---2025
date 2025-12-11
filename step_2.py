# Lecture propre du fichier
with open('input.txt', 'r', encoding='utf-8') as fichier:
    # On sépare directement les deux blocs par la double ligne vide
    content = fichier.read().strip().split('\n\n')

# On ne s'intéresse qu'au premier bloc (les plages)
raw_ranges = content[0].split('\n')

# 2. Parsing et Conversion en INT (Crucial !)
ranges = []
for line in raw_ranges:
    start, end = line.split('-')
    ranges.append([int(start), int(end)])

# 3. Tri des plages par ordre croissant de début
# Cela permet de vérifier les chevauchements en un seul passage
ranges.sort() 

# Algorithme de fusion (Merge Intervals)
merged = []
if ranges:
    # On commence avec le premier intervalle
    current_start, current_end = ranges[0]

    for i in range(1, len(ranges)):
        next_start, next_end = ranges[i]

        if next_start <= current_end + 1: # +1 car c'est inclusif (ex: 3-5 et 6-8 se touchent si on considère les entiers)
             # S'il y a chevauchement ou continuité, on prolonge la fin si nécessaire
            current_end = max(current_end, next_end)
        else:
            # Pas de chevauchement, on enregistre l'intervalle courant et on passe au suivant
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end
    
    # Ne pas oublier d'ajouter le dernier intervalle
    merged.append((current_start, current_end))

# 5. Calcul du résultat final
total_count = 0
for start, end in merged:
    # +1 car les bornes sont inclusives (ex: 3-5 fait 3,4,5 donc 5-3+1 = 3)
    total_count += (end - start + 1)

print("Nombre d'IDs frais (Part 2) :", total_count)