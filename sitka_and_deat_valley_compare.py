from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

path_sitka = Path('weather_data/sitka_weather_2021_simple.csv')
path_dv = Path('weather_data/death_valley_2021_simple.csv')
lines_sitka = path_sitka.read_text(encoding='utf-8').splitlines()
lines_dv = path_dv.read_text(encoding='utf-8').splitlines()

reader_sitka = csv.reader(lines_sitka)
reader_dv = csv.reader(lines_dv)
header_row_sitka = next(reader_sitka)
header_row_dv = next(reader_dv)

# Asegura que los indices sean los correctos
# Sitka
sitka_dates = header_row_sitka.index('DATE')
sitka_lows = header_row_sitka.index('TMIN')
sitka_highs = header_row_sitka.index('TMAX')
sitka_station = header_row_sitka.index('NAME')

# Death Valley
dv_dates = header_row_dv.index('DATE')
dv_lows = header_row_dv.index('TMIN')
dv_highs = header_row_dv.index('TMAX')
dv_station = header_row_dv.index('NAME')

# Extract dates, and high and lows temperatures.
# Datos para Sitka
dates_sitka, highs_sitka, lows_sitka = [], [], []
station_name_sitka = ""
for row in reader_sitka:
    current_date = datetime.strptime(row[sitka_dates], '%Y-%m-%d')
    high = int(row[sitka_highs])
    low = int(row[sitka_lows])
    if not station_name_sitka:
        station_name_sitka = row[sitka_station]
    dates_sitka.append(current_date)
    highs_sitka.append(high)
    lows_sitka.append(low)

# Datos para Death Valley.
dates_dv, highs_dv, lows_dv = [], [], []
station_name_dv = ""
for row in reader_dv:
    current_date = datetime.strptime(row[dv_dates], '%Y-%m-%d')
    try:
        high = int(row[dv_highs])
        low = int(row[dv_lows])
    except ValueError:
        print(f"Datos faltantes o invalidos en fila: {row}")
    else:
        if not station_name_dv:
            station_name_dv = row[dv_station]
        dates_dv.append(current_date)
        highs_dv.append(high)
        lows_dv.append(low)

# Valores minimos globales.
global_min_values = min(min(lows_sitka), min(lows_dv))
global_max_values = max(max(highs_sitka), max(highs_dv))

# Plot the high and low temperatures.
# Base de la grafica.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Datos visuales de Sitka
ax.plot(dates_sitka, highs_sitka, color='red', alpha=0.5)
ax.plot(dates_sitka, lows_sitka, color='blue', alpha=0.5)
ax.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

# Datos visuales de Death Valley
ax.plot(dates_dv, highs_dv, color='purple', alpha=0.5)
ax.plot(dates_dv, lows_dv, color='pink', alpha=0.5)
ax.fill_between(dates_dv, highs_dv, lows_dv, facecolor='pink', alpha=0.1)



# Format plot
title = f"Comparacion de temperaturas diaras de Sitka - {station_name_sitka} y \nDeath Valley - {station_name_dv}"
ax.set_title(title, fontsize=21)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatrue(F)", fontsize=16)
ax.tick_params(labelsize=16)
ax.set_ylim(global_min_values, global_max_values)

plt.show()
