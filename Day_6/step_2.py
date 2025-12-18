# Lecture du fichier
with open('input.txt', 'r', encoding='utf-8') as fichier:
    lines = fichier.read().splitlines()

# Pour l'étape 2, on ne peut pas utiliser .split() car les espaces sont cruciaux.
# On doit s'assurer que toutes les lignes ont la même longueur (padding)
max_len = max(len(line) for line in lines)
table = [line.ljust(max_len) for line in lines]

nbr_line = len(table) - 1       # -1 pour la ligne des opérateurs
largeur = len(table[0])

result = 0
final = 0
current_problem_numbers = [] # Pour stocker les nombres du problème en cours
current_operator = None

# On parcourt les colonnes de dràçte à gauche (step -1)
for x in range(largeur - 1, -1, -1):
    
    # Vérifier si la colonne est vide
    is_empty = True
    col_content = []
    
    for y in range(nbr_line + 1):           # On regarde toute la hauteur
        char = table[y][x]
        if char != ' ':
            is_empty = False
        col_content.append(char)

    # Si c'est une colonne de données
    if not is_empty:
        # On récupère l'opérateur
        op_char = col_content[nbr_line] 
        if op_char in ['+', '*']:
            current_operator = op_char
        
        # On construit le nombre verticalement
        # On prend les caractères du haut jusqu'avant l'opérateur
        number_str = ""
        for y in range(nbr_line):
            if col_content[y].isdigit():
                number_str += col_content[y]
        
        # Si on a trouvé des chiffres, on convertit en int et on stocke
        if number_str:
            current_problem_numbers.append(int(number_str))

    # Si on tombe sur une colonne vide ou qu'on est au tout début (fin de la boucle)
    # On doit calculer le résultat du problème qu'on vient de dépasser
    if is_empty or x == 0:
        if current_problem_numbers:
            # On fait le calcul (inspiré de ton code)
            temp_res = 0
            
            # Initialisation selon l'opérateur
            if current_operator == '+':
                temp_res = 0
            elif current_operator == '*':
                temp_res = 1
            
            # Application de l'opération
            for num in current_problem_numbers:
                if current_operator == '+':
                    temp_res += num
                elif current_operator == '*':
                    temp_res *= num
            
            final += temp_res
            
            # Réinitialisation pour le prochain problème
            current_problem_numbers = []
            current_operator = None

print(final)