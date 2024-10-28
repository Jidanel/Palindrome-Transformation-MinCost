def min_insertions_to_palindrome(s):
    # Inverse de la chaîne
    s_reverse = s[::-1]
    n = len(s)

    # Table pour la longueur de la plus longue sous-séquence commune
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Remplir la table de DP pour calculer la LCS entre `s` et `s_reverse`
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s_reverse[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Longueur de la plus longue sous-séquence palindromique (LPS)
    lps = dp[n][n]

    # Le coût minimal pour faire de `s` un palindrome
    return n - lps

# Lecture de l'entrée
s = input("Entrez la chaîne : ").strip()
# Calcul et affichage du résultat
print(f"Coût minimal pour rendre la chaîne un palindrome : {min_insertions_to_palindrome(s)}")
