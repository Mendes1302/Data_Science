import numpy as np

p = 0.5
nsim = 10
nhead = 0
saida = []


for i in range(0, nsim):
    aux = np.random.uniform()
    if(aux < p):
        nhead += 1
        saida.append(1)
    else:
        saida.append(0)

print("Saida: ", saida)
print("Frequencia de caras: ", (nhead/nsim)*100)