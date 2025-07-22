import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fix, ax = plt.subplots()
ax.scatter(x_values, y_values,  s=10)

# Set chart title and label axes
ax.set_title("Numeros cubicos", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Raiz del Valor", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

plt.show()