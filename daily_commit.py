from datetime import datetime

# Cambia este archivo para marcar actividad diaria
with open("daily_log.txt", "a") as f:
    f.write(f"Commit del dia: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")