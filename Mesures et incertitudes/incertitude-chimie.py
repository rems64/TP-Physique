import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt


m = 1.26
dm = 0.01

M = 126.07

V = 0.2
dV = 0.00015

# on entre le nombre de simulations que l'on veut effectuer
 
N = 1000
 
# calculs avec une distribution de probabilité uniforme
 
m_al = np.random.uniform(m-dm,m+dm,N)
v_al = np.random.uniform(V-dV,V+dV,N)

c = m_al / M / v_al


plt.hist(c,bins='rice')
plt.show()
 
# Calcul et affichage moyenne et écart-type
 
c_moy = np.mean(c)
u_c = np.std(c,ddof=1)
print("C moyen vaut {:.5f} mol/L".format(c_moy))
print("L'écart-type sur V moyen vaut {:.5f} mol/L".format(u_c))
