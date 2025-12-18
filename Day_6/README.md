# 🎄 Advent of Code 2025 - Jour 6

## 🗑️ Trash Compactor (Le Compacteur à Ordures)

Après avoir traversé la cuisine, je prends une pause bien méritée... qui se transforme en chute libre dans le vide-ordures ! Je me retrouve coincé dans un compacteur avec une famille de céphalopodes. La porte est scellée magnétiquement et, en attendant qu'ils la débloquent, ils me demandent de l'aide pour les devoirs de mathématiques du petit dernier.

C'est parti pour du tutorat de mathématiques inter-espèces (et pour survivre).

---

### 📝 Le Problème

L'input est une feuille de calcul mathématique, mais elle ne ressemble à rien de connu. Les problèmes ne sont pas écrits ligne par ligne, mais **verticalement**, sous forme de colonnes, et séparés par des colonnes vides.

#### Exemple de données :

```text
123 328  51
 45 64  387
  6 98  215
* +    *
```

### ⭐ Partie 1 : Mathématiques Verticales

L'objectif est de lire la grille colonne par colonne (de gauche à droite). Chaque colonne représente une liste de nombres à traiter avec l'opérateur situé tout en bas (`+` ou `*`).

Mon script `step_1.py` s'attaque à ce parsing visuel :
* Il sépare les blocs de nombres grâce aux colonnes vides.
* Il gère l'initialisation des calculs (attention à ne pas multiplier par 0 au départ !).
* Il additionne le résultat de chaque problème individuel.

**Résultat :** Il fallait faire abstraction des lignes pour voir les colonnes.

### ⭐⭐ Partie 2 : Logique Céphalopode

Les céphalopodes reviennent et m'expliquent que je lis tout de travers ! Leur mathématique se lit **de droite à gauche**. De plus, une colonne ne contient pas *plusieurs* nombres, mais **un seul nombre** écrit verticalement (chiffre des milliers en haut, unités en bas).

Mon script `step_2.py` adapte la logique :
* **Lecture inversée :** On parcourt les colonnes en partant de la fin (droite vers gauche).
* **Padding :** Utilisation de `.ljust()` pour égaliser la longueur des lignes (les espaces sont cruciaux ici).
* **Construction de nombre :** Chaque colonne est concaténée verticalement pour former un entier unique avant d'appliquer l'opération.

> **Note :** La difficulté principale ici était de changer complètement le sens de lecture et la méthode de construction des nombres sans casser la logique de détection des séparateurs.

-----

### 🚀 Résultats

| Partie | Réponse | Étoile |
| :--- | :--- | :---: |
| **Partie 1** | **5 782 351 442 566** | ⭐ |
| **Partie 2** | **3 263 827** | ⭐ |

*(Note : J'ai mis le résultat de l'exemple pour la partie 2 dans le tableau, pense à le remplacer par ta vraie réponse générée par `step_2.py`)*

-----

### 🛠️ Comment lancer la solution

J'ai séparé la logique en deux fichiers distincts pour plus de clarté.

Pour la partie 1 (Lecture gauche-droite classique) :
```bash
python step_1.py

```

Pour la partie 2 (Lecture droite-gauche céphalopode) :

```bash
python step_2.py

```

*Merci aux céphalopodes pour cette leçon de perspective !* 🐙
