import matplotlib.pyplot as plt
import numpy as np

p = 0.5
Nmax = 1000
vp = []
vsim = []
saida = []

for nsim in np.arange(1, Nmax, 10):
    nhead = 0
    for i in range(1, nsim):
        aux = np.random.uniform()
        if(aux < p):
            nhead += 1
    vp.append(nhead/nsim)
    vsim.append(nsim)



plt.figure(figsize=(8, 6))
plt.plot(vsim, vp, linestyle='-', color='blue', linewidth=2, label = 'Valor simulado')
plt.axhline(y=p, color='r', linestyle='--', label='Valor teorico')
plt.ylabel("Fração de cara", fontsize =20)
plt.xlabel("Número de  siulações", fontsize =20)
plt.xlim([0.0, Nmax])
plt.ylim([0.0, 1.0])
plt.legend()
plt.show(block=False)
plt.pause(3)
plt.close()