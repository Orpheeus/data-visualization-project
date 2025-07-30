import plotly.express as px
from die import Die

# Crea dos instancias de la clase Die, esta vez con 8 caras.
dado_1 = Die(8)
dado_2 = Die(8)

# Lanza ambos dados 10,000 veces.
# Suma los resultados de cada lanzamiento y guarda cada suma en una lista.
resultados = []
for roll_num in range(10_000):
    resultado = dado_1.roll() + dado_2.roll()
    resultados.append(resultado)

# Usa plotly para visualizar la frecuencia de cada posible resultado (De 2 a 16)
frecuencias = []
maximo_resultado = dado_1.num_sides + dado_2.num_sides
posibles_resultados = range(2, maximo_resultado+1)
for value in posibles_resultados:
    frecuencia = resultados.count(value)
    frecuencias.append(frecuencia)

# El grafico debe de tener titulo y etiquetas de eje.
titulo = "Resultados de tirar dos D8 1000 veces."
label = {'x': 'Resultado', 'y': 'Frecuencia del Resultado'}
fig = px.bar(x=posibles_resultados, y=frecuencias, title=titulo, labels=label)

# Asegurate que el eje de X muestre cada valor posible sin omitir ninguno.
fig.update_layout(xaxis_dtick=1)

fig.show()


