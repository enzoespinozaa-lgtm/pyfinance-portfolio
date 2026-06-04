import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from pathlib import Path

# Cargar retornos
ruta = Path(__file__).parent.parent / "data" / "retornos.csv"
returns = pd.read_csv(ruta, index_col=0, parse_dates=True)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

for i, col in enumerate(returns.columns):
    mu = returns[col].mean()
    sigma = returns[col].std()

    # Curva normal teórica
    x = np.linspace(returns[col].min(), returns[col].max(), 200)

    # Histograma real
    axes[i].hist(returns[col], bins='auto', density=True,
                 alpha=0.5, color="blue", label="Retornos reales")
    
    # Curva normal
    axes[i].plot(x, st.norm.pdf(x, mu, sigma),
                'r-', lw=2, label="Normal Teórica")
    
    axes[i].set_title(col, fontsize=10)
    axes[i].legend(fontsize=8)
    axes[i].set_xlabel("Retorno diario")
    axes[i].set_ylabel("Densidad")

plt.suptitle("Distribución de Retornos vs Normal Teórica", fontsize=12)
plt.tight_layout()

# Guardar figura
ruta_fig = Path(__file__).parent.parent / "data" "return_distribution.png"
plt.savefig(ruta_fig, dpi=150)

plt.show()
print("Gráfico guardado")
