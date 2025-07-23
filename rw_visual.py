import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Hace una caminata aleatoria.
rw = RandomWalk()
rw.fill_walk()

# Plotea los puntos en la caminata
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()