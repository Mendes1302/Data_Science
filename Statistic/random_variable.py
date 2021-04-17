import matplotlib.pyplot as plt
from random import randint

aposta = 5
Ns = 150000
p = 0

for n in range(1, Ns):
    G = 0
    x = randint(1, 6)
    y = randint(1, 6)
    if y > x:
        G = 2*(y-x)
    if (G > aposta):
        p += 1

p = p/Ns
print("Aposta:", aposta, "reais. ")
print("Valor teórico: ", 1/6)
print("Chance de lucro: ", p)

plt.figure(figsize=(8, 6))
plt.plot(p, Ns, linestyle='-', color='blue', linewidth=2, label = 'Valor simulado')
plt.axhline(y=1/6, color='r', linestyle='--', label='Valor teorico')
plt.ylabel("Fração de cara", fontsize =20)
plt.xlabel("Número de  simulações", fontsize =20)
plt.xlim([0.0, Ns])
plt.ylim([0.0, 1.0])
plt.legend()
plt.show(block=False)
plt.pause(8)
plt.close()