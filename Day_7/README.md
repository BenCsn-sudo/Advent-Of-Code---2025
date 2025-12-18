
# 🎄 Advent of Code 2025 - Jour 7

## 🧪 Laboratories (Les Laboratoires)

À peine sorti du compacteur à ordures, je me retrouve dans l'aile de recherche du Pôle Nord. Curieux, je tente d'utiliser un téléporteur... et je finis dans une pièce sans issue avec une machine qui fume. Le code d'erreur `0H-N0` indique un problème de "collecteur de tachyons".

Pour réparer le téléporteur et m'enfuir, je dois analyser comment les faisceaux de particules se comportent dans ce collecteur.

---

### 📝 Le Problème

L'input est un diagramme représentant le collecteur de tachyons. C'est une grille contenant :

* `S` : La source du faisceau (Start).
* `.` : De l'espace vide.
* `^` : Des séparateurs (splitters).

**Les règles de la physique des tachyons :**

1. Le faisceau part de `S` et descend toujours vers le bas.
2. Dans le vide (`.`), il continue tout droit.
3. S'il touche un séparateur (`^`), le faisceau s'arrête et **deux nouveaux faisceaux** sont créés : un juste à gauche et un juste à droite (tous deux continuent de descendre).

#### Exemple de flux :

```text
.......S.......   (Départ)
.......|.......   (Descente)
......|^|......   (Division !)
......|.|......
.....|^|^|.....   (Re-division)

```

### ⭐ Partie 1 : Fission de Tachyons

L'objectif est de simuler le parcours du faisceau depuis la source et de compter combien de fois une division ("split") se produit.

* **Simulation** : Il faut suivre la coordonnée de chaque tête de faisceau ligne par ligne.
* **Fusion** : Si deux séparateurs envoient un faisceau au même endroit (ex: le séparateur de gauche envoie à droite, et celui de droite envoie à gauche), les faisceaux fusionnent et ne comptent que pour un seul flux.
* **Objectif** : Compter le nombre total de rencontres avec un `^` qui génèrent une division.

### ⭐⭐ Partie 2 : [À Venir]

*(Cette section sera complétée une fois l'étape 1 validée et l'énoncé de l'étape 2 révélé).*

> **Note :** Probablement une complexification des règles de mouvement ou une optimisation nécessaire sur une grille beaucoup plus grande.

---

### 🚀 Résultats

| Partie | Réponse | Étoile |
| --- | --- | --- |
| **Partie 1** | *À calculer* | ⏳ |
| **Partie 2** | *Verrouillé* | 🔒 |

---

### 🛠️ Comment lancer la solution

```bash
cd Day_7
python step_1.py

```

*Prêt à réparer ce téléporteur !* ⚛️
