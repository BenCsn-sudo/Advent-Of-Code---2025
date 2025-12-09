# 🎄 Jour 2 de l'Advent of Code : Boutique de Souvenirs

## 📝 Contexte
Vous visitez la boutique de souvenirs du Pôle Nord. Un jeune elfe s'est amusé avec l'ordinateur et a inséré une série d'**Identifiants de Produits (ID) invalides** dans la base de données. On vous demande de scanner des plages d'ID spécifiques pour trouver et additionner tous ces identifiants corrompus.

## 📂 Entrée du Puzzle (Input)
L'entrée est une longue chaîne de caractères représentant des plages d'ID séparées par des virgules.
- **Format :** `debut-fin,debut-fin,debut-fin...`
- **Exemple :** `11-22,95-115,998-1012`

Il faut analyser chaque nombre entier compris dans ces plages (inclus).

---

## ⭐ Partie 1 : Motifs doubles

Pour cette première étape, un ID est considéré comme **invalide** s'il est constitué **uniquement d'une séquence de chiffres répétée exactement deux fois**.

### Règles :
- Le nombre doit être formé par la concaténation d'un motif `X` avec lui-même (`XX`).
- Les nombres ne commencent jamais par 0.

### Exemples d'ID invalides (à compter) :
- `55` (le chiffre `5` répété 2 fois)
- `6464` (la séquence `64` répétée 2 fois)
- `123123` (la séquence `123` répétée 2 fois)

### Objectif
Trouver tous les ID invalides dans les plages données et calculer leur **somme**.

---

## ⭐⭐ Partie 2 : Répétitions multiples

L'elfe a créé d'autres motifs. Les règles changent légèrement : un ID est maintenant considéré comme **invalide** s'il est constitué **uniquement d'une séquence de chiffres répétée au moins deux fois** (2 fois, 3 fois, 4 fois, etc.).

### Règles mises à jour :
- Le nombre doit être formé par la répétition d'un motif `X` (`XX`, `XXX`, `XXXX`...).

### Nouveaux exemples d'ID invalides :
- `12341234` (répété 2 fois, déjà valide en partie 1)
- `123123123` (répété 3 fois)
- `1111111` (répété 7 fois)

### Objectif
Recalculer la **somme** de tous les ID invalides selon cette nouvelle définition.

---

## 🚀 Résultat attendu
Le programme doit afficher deux nombres :
1. La somme des ID invalides selon la règle de la Partie 1.
2. La somme des ID invalides selon la règle de la Partie 2.
