
"""
Incertitudes de type A pour la mesure de la période du pendule simple

"""
import numpy as np                  # pour la manipulation des tableaux
import matplotlib.pyplot as plt     # pour les représentations graphiques

# On rentre les périodes mesurées
T = np.array([1.425, 1.434, 1.413, 1.422, 1.422, 1.428, 1.432, 1.422, 1.431, 1.431])

# Tracé de l'histogramme
plt.hist(T,bins='rice')  # 'rice' pour d'optimiser les intervalles d'affichage
plt.title("Histogramme des périodes (s)")
plt.show()

# Calcul de l'incertitude-type
u_c = np.std(T,ddof=1)/np.sqrt(len(T))
print("L'incertitude-type sur la moyenne de la période vaut {:.4f}s".format(u_c))


# Calcul de la moyenne
T_moy = np.mean(T)
print("La valeur moyenne des périodes mesurées vaut {:.4f}s".format(T_moy))
