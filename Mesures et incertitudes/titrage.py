import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt



cA = 0.0499      # Selon incertitude.py
dCa = 0.230E-3

vA = 0.02
dVa = 0.03E-3  # Selon constructeur

Vequi = 18.4E-3
dVequi = sqrt(0.05E-3**2 + 2*0.005E-3)  # Incertitude manipulation + verrerie

# on entre le nombre de simulations que l'on veut effectuer

N = 10000

# calculs avec une distribution de probabilité uniforme

cA_al = np.random.uniform(cA-dCa,cA+dCa,N)
vA_al = np.random.uniform(vA-dVa,vA+dVa,N)
Vequi_al = np.random.uniform(Vequi+dVequi,Vequi-dVequi,N)


cB = (2 * cA_al * vA_al) / Vequi_al


plt.hist(cB,bins='rice')
plt.show()

# Calcul et affichage moyenne et écart-type

cB_moy = np.mean(cB)
u_cB = np.std(cB,ddof=1)
print("cB moyen vaut {:.5f} mol/L".format(cB_moy))
print("L'écart-type sur cB moyen vaut {:.5f} mol/L".format(u_cB))
