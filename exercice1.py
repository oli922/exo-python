# Nom et prénom à afficher
nom = "POSSIAN"  # Remplacez par votre nom
prenom = "Olivia"  # Remplacez par votre prénom

# Valeur prédéfinie pour n
n = 5  # Vous pouvez définir une autre valeur ici

# Solution 1 : Calcul de la factorielle avec une boucle for
def factorielle_for(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

# Solution 2 : Calcul de la factorielle avec une boucle while
def factorielle_while(n):
    resultat = 1
    i = 1
    while i <= n:
        resultat *= i
        i += 1
    return resultat

# Calcul de la factorielle avec les deux méthodes
print(f"Factorielle de {n} (méthode for): {factorielle_for(n)}")
print(f"Factorielle de {n} (méthode while): {factorielle_while(n)}")

# Affichage pour les nombres de 1 à 50
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: {nom} {prenom}")
    elif i % 3 == 0:
        print(f"{i}: {nom}")
    elif i % 5 == 0:
        print(f"{i}: {prenom}")
    else:
        print(i)
