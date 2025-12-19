# 🎄 Advent of Code - Day 1: Secret Entrance

## 🔐 Secret Entrance (L'Entrée Secrète)

Les Elfes ont enfin découvert la gestion de projet ! Mais avant de commencer à décorer le Pôle Nord, nous devons entrer dans la base. Le mot de passe a changé et se trouve dans un coffre-fort protégé par un cadran rotatif numéroté de 0 à 99.

Le coffre est en réalité un leurre : la véritable clé réside dans l'analyse des mouvements du cadran.

---

### 📝 Le Problème

Nous disposons d'une liste d'instructions de rotation (ex: `R5`, `L10`...).

* Le cadran commence à la position **50**.
* Il contient 100 positions (0-99).
* **R** (Right) augmente la valeur (sens horaire).
* **L** (Left) diminue la valeur (sens anti-horaire).
* Le cadran est circulaire : après 99 on retourne à 0, et avant 0 on retourne à 99.

### ⭐ Partie 1 : La position finale

L'objectif est de compter combien de fois le cadran **s'arrête** sur la position `0` à la fin d'une instruction.

**Approche Code (`step_1.py`) :**
La solution utilise l'arithmétique modulaire pour gérer la circularité du cadran sans faire de boucles complexes.

* Mise à jour : `position = (position + valeur) % 100`.
* Vérification simple après chaque mouvement : `if position == 0`.

**Réponse :** 982

### ⭐⭐ Partie 2 : Le passage par zéro

La sécurité a été renforcée ("Method 0x434C49434B"). Il ne suffit plus de s'arrêter sur zéro, il faut compter **chaque fois que le cadran touche ou traverse le zéro** pendant la rotation.

**Approche Code (`step_2.py`) :**
Ici, le modulo ne suffit plus car il ne nous dit pas ce qui s'est passé *pendant* le mouvement.

1. **Calcul de la distance vers zéro** :
* Vers la droite (`R`) : `100 - position`.
* Vers la gauche (`L`) : `position` (ou `100` si on est déjà sur 0).


2. **Détection du croisement** :
* Si le mouvement est plus grand que la distance vers zéro, on a croisé au moins une fois (`result += 1`).
* Si le mouvement est très grand, on compte les tours complets supplémentaires : `(valeur - dist_vers_zero) // 100`.


---

### 🚀 Résultats

| Partie | Réponse | Étoile |
| --- | --- | --- |
| **Partie 1** | **982** | ⭐ |
| **Partie 2** | **386** | ⭐ |

*(Note : La réponse de la partie 2 est calculée par le script `step_2.py`)*

---

### 🛠️ Comment lancer la solution

J'ai séparé la logique en deux fichiers distincts pour plus de clarté.

Pour la partie 1 (Compter les arrêts sur 0) :

```bash
python step_1.py

```

Pour la partie 2 (Compter les passages par 0) :

```bash
python step_2.py

```

*Le Pôle Nord est ouvert, place à la décoration !* 🎄
