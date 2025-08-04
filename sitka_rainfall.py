from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_rows = next(reader)

# Identificar la posicion de "PRCP"
prcp_index = header_rows.index('PRCP')
date_index = header_rows.index('DATE')
print(prcp_index)
print(date_index)

# Trabajar la linea de PRCP.
prcp_values, dates = [], []
for row in reader:
    try:
        prcp_values.append(float(row[prcp_index]))
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    except ValueError:
        print(f"Datos faltantes o invalidos en fila: {row}")
    else:
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

