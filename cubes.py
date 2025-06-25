import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values , c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and albex axes
ax.set_title("Numeros Cubicos", fontsize=25)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Valor Cubico", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set the range for each axis.

plt.show()