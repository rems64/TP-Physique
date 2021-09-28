import numpy as np
import matplotlib.pyplot as plt

OA   = [-50.0, -45.0, -55.0, -60.0, -15.0, -10.0, -20.0 , 35.0, 40.0, 45.0]
OAp  = [ 50.0,  57.5,  48.3,  44.0, -35.0, -17.0, -105.0, 15.0, 16.0, 17.0]

nOA  = np.array(OA)
nOAp = np.array(OAp)

OFp  = (nOAp*nOA)/(nOA-nOAp)

moyenne = np.mean(OFp)
incertitude = np.std(OFp,ddof=1)/np.sqrt(len(nOA))
print("La distance focale de la lentille est {:.3f}".format(moyenne))
print("L'incertitude vaut {:.3f}".format(incertitude))

plt.hist(OFp,bins='rice')
plt.title("Histogramme des f\' (cm)")
plt.show()