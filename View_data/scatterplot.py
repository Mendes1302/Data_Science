from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "casablanca", "Ganndhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]


xl = list()
for i, _ in enumerate(movies):
    xl.append(i+0.1)

plt.bar(xl, num_oscars)
plt.ylabel("# de Premiações")
plt.title("Meus Filmes Favoritos")
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()
