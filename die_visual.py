from die import Die

# Crea un D6.
die = Die()

# Hace unas lanzadas, y guarda el resultado en una lista.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analiza los resultados
frequencies = []
possible_results = range(1, die.num_sides+1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)