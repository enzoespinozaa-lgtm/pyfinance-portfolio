import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

ruta = Path(__file__).parent.parent / "data" / "retornos.csv"
returns = pd.read_csv(ruta, index_col=0, parse_dates=True)

rolling_vol = returns.rolling(30).std() * np.sqrt(252)

fig, ax = plt.subplots(figsize=(12,5))
rolling_vol.plot(ax=ax)

ax.set_title("Volatilidad Histórica (30 días)", fontsize=12)
ax.set_xlabel("Fecha")
ax.set_ylabel("Volatilidad (%)")
ax.legend(returns.columns)
ax.grid(alpha=0.3)

plt.tight_layout()

ruta_fig = Path(__file__).parent.parent / "data" / "roling_vol.png"
plt.savefig(ruta_fig, dpi=150)
print("Gráfico guardado")

plt.show()
