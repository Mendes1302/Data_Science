import numpy as np
from matplotlib import pyplot as plt
import random
from random import seed
seed(100)

portas = [1, 2, 3]
Nmax = 2000
P = [] # armazena a fração de vitorias
F = []
vN = [] # armazena o numero de jogos
for N in np.arange(1, Nmax,10):
    vitoria = 0
    derrota = 0
    for i in range(0,N):
        C = random.choice(portas) # coloca o carro em uma porta
        X = random.choice(portas) # seleciona uma porta
        if(C != X): # se carro não está na porta selecionada
            # o apresendador irá abrir outra porta que tem o bode. 
            # Trocando a porta, ganha-se o carro.
            vitoria = vitoria + 1
        else:
            derrota = derrota + 1
    P.append(vitoria/N)
    F.append(derrota/N)
    vN.append(N)
plt.figure(figsize=(12,8))
plt.plot(vN, P, 'ro-', label='Simulação: Muda a porta', color='blue')
plt.plot(vN, F, 'ro-', label='Simulação: Acertou de primeira')
plt.axhline(y=2/3,color='red', label='Prob. teórica com mudança de porta')
plt.ylim(0,1.05)
plt.legend()
plt.show()