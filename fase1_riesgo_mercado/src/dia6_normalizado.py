import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ruta = Path(__file__).parent.parent / "data" / "prices.csv"
data = pd.read_csv(ruta, index_col=0, parse_dates=True)

normalized_data = data / data.iloc[0] * 100

fig, ax = plt.subplots(figsize=(12,5))
normalized_data.plot(ax=ax)

ax.set_title("Precios Normalizados - Base 100 (enero 2020)", fontsize=12)
ax.set_ylabel("Índice (base 100)")
ax.set_xlabel("Fecha")
ax.axhline(100, color='black', lw=0.8, linestyle='--')
ax.grid(alpha=0.3)

plt.tight_layout()

ruta_fig = Path(__file__).parent.parent / "data" / "normalized_prices"
plt.savefig(ruta_fig, dpi=150)
plt.show()
print("Gráfica guardado")
plt.show()