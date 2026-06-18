# ¿Qué es un drawdown?
# Es la caída desde el máximo histórico hasta el día de hoy.
# Mide cuánto ha perdido el activo desde su pico más reciente.

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ruta = Path(__file__).parent.parent / "data" / "prices.csv"
data = pd.read_csv(ruta, index_col=0, parse_dates = True)

def calculate_drawndown(prices):
    rolling_max = prices.cummax()
    return (prices - rolling_max) / rolling_max

dd = calculate_drawndown(data)

# Estadísticos clave
print("=== Máximo Drawdown por activo ===")
print(dd.min().round(4))

# Graficar
fig, ax = plt.subplots(figsize=(12,5))
dd.plot(ax=ax)
ax.axhline(0, color='black',lw=0.8)
ax.set_title("Drawdown por Activo", fontsize=12)
ax.set_ylabel("Drawdown")
ax.set_xlabel("Fecha")
ax.grid(alpha=0.3)

plt.tight_layout()

ruta_fig = Path(__file__).parent.parent / "data" / "drawdown.png"
plt.savefig(ruta_fig, dpi=150)
plt.show()