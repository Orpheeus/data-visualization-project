import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Hace una caminata al azar
rw = RandomWalk()
rw.fill_walk()

# Plot los puntos que estan en la caminata
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()