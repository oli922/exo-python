import matplotlib.pyplot as plt
import math  # Import du module math

rayon = float(input("Entrez le rayon du cercle: "))

# Création des coordonnées
theta = [i * 0.01 for i in range(0, 628)]  # 0 à 2π en radians
x = [rayon * math.cos(t) for t in theta]
y = [rayon * math.sin(t) for t in theta]

# Dessiner le cercle
plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.title(f"Cercle avec rayon = {rayon}")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")  # Échelle égale pour un vrai cercle
plt.grid()
plt.show()
