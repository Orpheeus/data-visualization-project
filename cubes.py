import matplotlib.pyplot as plt

# Valor de los ejes
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, s=1)

# Nombrar la tabla y los nombres de los ejes
ax.set_title("Numeros Cubicos", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Valor Cubico", fontsize=14)

# Personaliza el rango de los ejes.
ax.tick_params(axis='both', labelsize=14)

plt.show()
