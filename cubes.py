# A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5,000 cubic numbers

import matplotlib.pyplot as plt

x_valores = range(1, 5001)
y_valores = [x**3 for x in x_valores]

plt.style.use('Solarize_Light2')
figura, eje = plt.subplots()
eje.scatter(x_valores, y_valores, c=y_valores, cmap=plt.cm.Purples, s=10)

# Titulo a los label de la grafica
eje.set_title("Valores Cubicos", fontsize=24)
eje.set_xlabel("Valor", fontsize=14)
eje.set_ylabel("Valor Cubico", fontsize=14)

eje.ticklabel_format(style='plain')

plt.show()



