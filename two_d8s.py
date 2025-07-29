import plotly.express as px
from die import Die

# Crea un D6 y un D10
die_1 = Die()
die_2 = Die()

# Hace unas tiradas y guarda los resultados en una lista.
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

# Analiza los resultados
max_result = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_result+1)

frequencies = [results.count(value) for value in possible_results]

# Visualiza los resultados
title = "Resultados de tirar tres dados D6 y D10 50,000 veces."
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)


# Mas personalizaciones.
fig.update_layout(xaxis_dtick=1)


fig.show()
