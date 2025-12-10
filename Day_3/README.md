
# 🎄 Advent of Code 2023 - Jour 3 : Le Hall d'Entrée

Bienvenue dans le dépôt de solutions pour le **Jour 3** de l'Advent of Code ! Les ascenseurs sont en panne à cause d'une surtension, et c'est à nous d'aider les elfes à redémarrer l'escalator pour descendre vers le département d'impression.

## 🎅 Le Scénario

Nous sommes coincés dans le hall. Pour faire fonctionner l'escalator de secours, nous devons configurer des banques de batteries. Chaque ligne de l'input représente une banque de batteries, et chaque chiffre est le **voltage** (joltage) d'une batterie (1-9).

L'objectif est de maximiser la puissance de sortie en sélectionnant un nombre précis de batteries dans chaque banque, sans changer leur ordre relatif.

---

## ⚡ Partie 1 : Démarrage d'Urgence

Pour la première étape, l'escalator a besoin d'une petite impulsion.
Nous devons activer **exactement 2 batteries** par banque pour former le plus grand nombre possible (concaténation des chiffres).

### Exemple
Pour la banque `12345`, si on garde les batteries `2` et `4`, on obtient **24 jolts**.

> **Objectif :** Trouver la sous-séquence de longueur 2 la plus grande (lexicographiquement) pour chaque ligne et sommer le tout.

⭐ **Réponse de la Partie 1 :** `16812`

---

## 🔋 Partie 2 : Puissance Maximale

L'escalator est trop lourd ! L'elfe appuie sur le gros bouton rouge "Override".
Nous devons maintenant activer **exactement 12 batteries** par banque pour générer une puissance massive.

Le principe reste le même : former le plus grand nombre possible en gardant l'ordre des chiffres, mais cette fois-ci, le nombre résultant aura 12 chiffres.

> **Attention :** Les nombres deviennent gigantesques (bien au-delà d'un entier 32-bit standard).
>
> *Exemple :* Pour `987654321111111`, le max est `987654321111`.

⭐ **Réponse de la Partie 2 :** `166345822896410`

---

## 🛠️ Note Technique

Ce problème est une variation classique de la recherche de la **sous-séquence lexicographique maximale** de longueur $k$.
* **Partie 1 :** $k = 2$
* **Partie 2 :** $k = 12$

L'approche gloutonne (Greedy) est de mise : on cherche le plus grand chiffre possible tant qu'il reste assez de chiffres à sa droite pour compléter la séquence requise.
