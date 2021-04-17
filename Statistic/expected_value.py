from random import seed
import numpy as np 
seed(1)

n = 5
x = 0
p = 0.9

lucro = 5
prejuizo = -1

for _ in range(n):
    r = np.random.uniform()
    if r <= p:
        x += lucro
    else:
        x -= prejuizo

x = x/n

print("Valor médio do lucro: ", x)