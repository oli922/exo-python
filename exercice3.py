from itertools import product

# Fonction qui compte les combinaisons de dés qui totalisent 20
def count_combinations(target_sum, num_dice, faces):
    # Générer toutes les combinaisons possibles de résultats des dés
    possibilities = product(range(1, faces+1), repeat=num_dice)
    
    # Compter les combinaisons dont la somme est égale à target_sum
    count = sum(1 for comb in possibilities if sum(comb) == target_sum)
    
    return count

# Paramètres du problème
target_sum = 20
num_dice = 5
faces = 6

# Calculer le nombre de combinaisons
result = count_combinations(target_sum, num_dice, faces)

# Afficher le résultat
print(f"Le nombre de façons différentes d'obtenir une somme de {target_sum} avec {num_dice} dés à {faces} faces est : {result}")
