# Palindrome-Transformation-MinCost
Algorithme pour calculer le coût minimal d'insertion de caractères pour transformer une chaîne en palindrome, basé sur la plus longue sous-séquence palindromique.

# Palindrome Transformation - Minimum Cost

Ce projet implémente un algorithme en Python pour déterminer le coût minimal d'insertion de caractères afin de transformer une chaîne donnée en palindrome. Cet algorithme utilise la dynamique de programmation (Dynamic Programming) pour calculer la plus longue sous-séquence palindromique (Longest Palindromic Subsequence - LPS) et en déduire le nombre minimum d'insertions nécessaires.

## Description du Problème

Alice aime les palindromes et souhaite transformer une chaîne de caractères en palindrome avec le minimum de modifications. À chaque insertion de caractère dans la chaîne, un coût de 1 est appliqué. L'objectif est de trouver le coût total minimum nécessaire pour rendre la chaîne symétrique.

### Exemple

- **Entrée :** `mbadm`
- **Sortie attendue :** `2`
  
Dans cet exemple, deux insertions sont nécessaires pour transformer `"mbadm"` en palindrome, comme `"mbdadbm"` ou `"mdbabdm"`.

## Solution

L'algorithme repose sur le calcul de la plus longue sous-séquence palindromique (LPS) de la chaîne. Le nombre minimum d'insertions est donné par la formule :

\[ \text{Coût minimal} = \text{longueur de la chaîne} - \text{LPS} \]

### Complexité

- **Complexité temporelle :** \(O(n^2)\), où \(n\) est la longueur de la chaîne, en raison de l'utilisation de la dynamique de programmation.
- **Complexité spatiale :** \(O(n^2)\), pour la matrice de mémoire dynamique (tableau DP).

## Utilisation

### Pré-requis

- Python 3.x

### Exécution du Code

Pour exécuter le script, utilisez la commande suivante dans votre terminal :

```bash
python3 palindrome_transformation.py
