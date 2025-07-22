import matplotlib.pyplot as plt

valores = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(valores, squares, linewidth=3)

# Define el titulo y el de los ejes.
ax.set_title("Raiz de numeros", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Raiz del valor", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()