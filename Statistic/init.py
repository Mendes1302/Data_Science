from matplotlib import pyplot as plt
from random import randint
from collections import Counter


num_friends = [randint(0, 100) for i in range(100)]
friend_counts = Counter(num_friends)

xs = range(101)
ys = [friend_counts[x] for x in xs]


fig = plt.figure()   
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histograma de Contagem de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("# pessoas")
plt.show()