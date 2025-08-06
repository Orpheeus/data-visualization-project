from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

# Define la ruta al archivo CSV con los datos meteorológicos
path = Path('weather_data/sitka_weather_2021_full.csv')

# Lee todo el contenido del archivo como texto y lo divide en líneas individuales
lines = path.read_text(encoding='utf-8').splitlines()

# Crea un lector CSV a partir de las líneas leídas (cada línea será tratada como una fila)
reader = csv.reader(lines)

# Lee la primera fila del archivo (encabezados de las columnas) y la guarda en una variable
header_rows = next(reader)


# Identificar la posicion de "PRCP"
prcp_index = header_rows.index('PRCP')
date_index = header_rows.index('DATE')
print(prcp_index)
print(date_index)

# Crea listas vacías para almacenar los valores de lluvia (PRCP) y las fechas correspondientes
prcp_values, dates = [], []

# Recorre cada fila del archivo CSV después del encabezado
for row in reader:
    try:
        # Intenta convertir el valor de lluvia a número decimal (float)
        prcp = float(row[prcp_index])

        # Convierte la cadena de texto de la fecha en un objeto datetime
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')

    except ValueError:
        # Si falta algún dato o no se puede convertir, imprime un mensaje y omite la fila
        print(f"Datos faltantes o invalidos en fila: {row}")

    else:
        # Si todo fue correcto, guarda el valor de lluvia y su fecha correspondiente
        prcp_values.append(prcp)
        dates.append(current_date)

# Visualiza los datos en una grafica.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, prcp_values)


# Detalles de la grafica (Titulo, nombre de los ejes).
titulo = "Informacion de los Dias de lluvia en Sitka."
ax.set_title(titulo, fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Dias de lluvia')
fig.autofmt_xdate()


plt.show()

