# Importamos las librerías para el dashboard
from re import X
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from pathlib import Path

ruta_prices = Path(__file__).parent.parent / "data" / "prices.csv"
ruta_returns = Path(__file__).parent.parent / "data" / "retornos.csv"

data = pd.read_csv(ruta_prices, index_col = 0, parse_dates = True)
returns = pd.read_csv(ruta_returns, index_col = 0, parse_dates = True)

# Funciones auxiliares
def calculate_drawdown(prices):
    return (prices - prices.cummax()) / prices.cummax()

# Dashboard 2x2
fig, axes = plt.subplots(2, 2, figsize = (14, 10))
fig.suptitle("Dashboard - Análisis de Riesgo de Mercado", fontsize = 14)

# Panel 1 - Precios normalizados
normalized = data / data.iloc[0] * 100
normalized.plot(ax=axes[0, 0])
axes[0, 0].set_title("Precios Normalizados (base 100)")
axes[0, 0].set_ylabel("Índice")
axes[0, 0].axhline(100, color='black', lw=0.8, linestyle='--')
axes[0, 0].grid(alpha=0.3)

# Panel 2 - Volatilidad rolling 30 días
rolling_vol = returns.rolling(30).std() * np.sqrt(252)
rolling_vol.plot(ax=axes[0, 1])
axes[0, 1].set_title("Volatilidad Rolling 30 días (anualizada)")
axes[0, 1].set_ylabel("Volatilidad")
axes[0, 1].grid(alpha=0.3)

# Panel 3 - Distribuciones vs Normal
for col in returns.columns:
    mu      = returns[col].mean()
    sigma   = returns[col].std()
    x       = np.linspace(returns[col].min(), returns[col].max(), 200)
    axes[1, 0].hist(returns[col], bins=60, density=True, alpha=0.4, label=col)
    axes[1, 0].plot(x, st.norm.pdf(x, mu, sigma), lw=1.5)
axes[1, 0].set_title("Distribuciones de Retornos vs Normal")
axes[1, 0].set_ylabel("Densidad")
axes[1, 0].legend(fontsize = 8)
axes[1, 0].grid(alpha=0.3)

# Panel 4 - Drawdown(data)
dd = calculate_drawdown(data)
dd.plot(ax=axes[1, 1])
axes[1, 1].axhline(0, color='black', lw=0.8)
axes[1, 1].set_title("Drawdown por Activo")
axes[1, 1].set_ylabel("Drawdown")
axes[1, 1].grid(alpha=0.3)

plt.tight_layout()

ruta_fig = Path(__file__).parent.parent / "data" /"dashboard.png"
plt.savefig(ruta_fig, dpi=150)
plt.show()
print("Dashboard guardado")