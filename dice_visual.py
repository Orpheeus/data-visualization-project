import plotly.express as px
from die import Die

# Crea un D6 y un D10
die_1 = Die()
die_2 = Die()

# Hace unas lanzadas, y guarda el resultado en una lista.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza los resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_result+1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza los resultados
title = "Resultados de tirar dos dados D6 1,000 veces."
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)


# Mas personalizaciones.
fig.update_layout(xaxis_dtick=1)


fig.show()



