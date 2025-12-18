# 🎄 Advent of Code 2025 - Jour 5

## 🍲 Cafeteria (La Cafétéria)

Après avoir traversé le mur avec les chariots élévateurs, nous tombons nez à nez avec... une cafétéria \! Les Elfes sont ravis, mais c'est la panique en cuisine. Le nouveau système de gestion d'inventaire est un cauchemar et ils ne savent plus quels ingrédients sont frais ou avariés pour préparer le festin de Noël.

C'est là que j'interviens pour sauver le dîner (et peut-être Noël).

-----

### 📝 Le Problème

L'input se divise en deux parties :

1.  Une liste de **plages d'identifiants (IDs)** correspondant aux ingrédients frais (ex: `3-5` signifie 3, 4 et 5).
2.  Une liste d'IDs d'ingrédients actuellement disponibles qu'il faut vérifier.

#### Exemple de données :

```text
3-5
10-14
16-20
12-18

1
5
8
11
...
```

### ⭐ Partie 1 : Le tri sélectif

L'objectif est de vérifier, pour chaque ingrédient de la seconde liste, s'il tombe dans **au moins une** des plages de validité définies dans la première partie.

  * L'ID `1` est avarié (nulle part).
  * L'ID `5` est frais (dans `3-5`).
  * L'ID `11` est frais (dans `10-14`).

**Résultat :** Il fallait compter combien d'ingrédients disponibles sont valides.

### ⭐⭐ Partie 2 : L'inventaire complet

Les Elfes changent de stratégie. Ils veulent simplement connaître le **nombre total** d'IDs uniques considérés comme "frais" par l'ensemble des plages données. La seconde liste (les ingrédients disponibles) est désormais inutile.

La difficulté réside dans le **chevauchement des plages** (ex: `10-14` et `12-18` se chevauchent). Il faut fusionner les intervalles pour ne pas compter les mêmes ingrédients deux fois, surtout avec des nombres astronomiques.

> **Note :** Les plages peuvent être massives, une approche par itération simple (brute force) serait trop lente.

-----

### 🚀 Résultats

| Partie | Réponse | Étoile |
| :--- | :--- | :---: |
| **Partie 1** | **640** | ⭐ |
| **Partie 2** | **365 804 144 481 581** | ⭐ |

-----

### 🛠️ Comment lancer la solution

```bash
cd Day_5
python step_1.py
```

*Joyeux code et bon appétit aux Elfes \!* 🍪
