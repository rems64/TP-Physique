# Créé par Cécile, le 02/09/2021 en Python 3.7

import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt

# on entre la période et la longueur du pendule ainsi que leurs incertitudes
T = 1.426
L = 0.505
u_T = 0.002
u_L = 0.005/sqrt(3)    # on a divisé la précision par racine de 3


# on entre le nombre de simulations que l'on veut effectuer

N = 10000

# calculs avec une distribution de probabilité normale

L_al = np.random.normal(L,u_L,N)
T_al = np.random.normal(T,u_T,N)
g = 4*np.pi**2*L_al/T_al**2

plt.hist(g,bins='rice')
plt.show()

# Calcul et affichage moyenne et écart-type

g_moy = np.mean(g)
u_g = np.std(g,ddof=1)

print("g moyen vaut {:.2f} m/s²".format(g_moy))
print("L'écart-type sur g moyen vaut {:.2f} m/s²".format(u_g))


# Détermination de g et de l'incertitude-type sur g par calcul à partir des incertitudes relatives

g_bis = 4*np.pi**2*L/T**2
u_g_bis = g_bis*sqrt((u_L/L)**2+(2*u_T/T)**2)

print("g vaut {:.2f} m/s²".format(g_bis))
print("L'incertitude-type sur g par composition vaut {:.2f} m/s²".format(u_g_bis))
