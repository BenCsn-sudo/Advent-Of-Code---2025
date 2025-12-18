# 🎄 Advent of Code - Day 6: Trash Compactor

## 📖 Description du Problème

Après une chute malencontreuse dans un compacteur à ordures du Pôle Nord, nous nous retrouvons coincés avec une famille de céphalopodes. En attendant qu'ils ouvrent la porte, nous devons aider le plus jeune d'entre eux à faire ses devoirs de mathématiques.

Le défi consiste à déchiffrer une feuille de calcul où les problèmes ne sont pas écrits de manière linéaire, mais **verticalement**, sous forme de grille.

### Exemple d'Input

```text
123 328  51
 45 64  387
  6 98  215
* +    *
```

Les nombres sont alignés verticalement et l'opérateur (`+` ou `*`) se trouve tout en bas de la colonne.

## 🛠️ Approche Technique

La solution a été développée en **Python**. La principale difficulté résidait dans le parsing (l'analyse) du fichier texte, car les données doivent être lues colonne par colonne et non ligne par ligne.

### Structure du Code
Le script `step_1.py` implémente la logique suivante :

1.  **Lecture et Nettoyage** : Le fichier est lu et séparé en lignes.
2.  **Création de la Matrice** : Chaque ligne est découpée (`split()`) pour former un tableau à deux dimensions (`table`), permettant d'accéder aux données via des coordonnées `[ligne][colonne]`.
3.  **Identification des Opérateurs** : Le script scanne la dernière ligne de la matrice pour déterminer l'opération à effectuer (Addition ou Multiplication).
4.  **Calcul Vertical** : Une boucle itère sur chaque colonne, accumulant les résultats selon l'opérateur identifié.

### 🌟 Partie 1 : Calculs Verticaux Standards
L'objectif était de sommer les résultats de chaque colonne indépendamment.
* **Logique** : Pour chaque colonne, si l'opérateur est `+`, on additionne les nombres. Si c'est `*`, on les multiplie.
* **Gestion du Zéro** : Une condition spécifique (`if result == 0`) a été implémentée pour gérer l'initialisation lors des multiplications et éviter de multiplier par zéro au démarrage.
* **Résultat obtenu** : `5782351442566`

### 🌟 Partie 2 : Mathématiques Céphalopodes (Logic)
Dans cette partie, la lecture change radicalement : les colonnes se lisent de droite à gauche, et chaque colonne représente un seul nombre entier (le chiffre du haut étant le plus significatif).

* **Interprétation** : Chaque colonne est parsée comme une suite de chiffres formant un grand nombre (ex: une colonne contenant 1, 4, 6 devient le nombre 146).
* **Calcul** : Les opérations sont ensuite appliquées sur ces nouveaux nombres formés.
* **Résultat** : Le grand total a été recalculé selon ces nouvelles règles de lecture "droite-à-gauche".

## 🚀 Utilisation

Pour lancer le script et voir le résultat :

```bash
python step_1.py
```

Assurez-vous que le fichier `input.txt` est présent dans le même répertoire que le script.

## 📂 Organisation des Fichiers

* `input.txt` : Les données du puzzle (la grille de nombres).
* `step_1.py` : Le script principal contenant la logique de parsing matriciel et de calcul.

---
