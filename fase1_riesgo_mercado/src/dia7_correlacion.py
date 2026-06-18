import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

ruta = Path(__file__).parent.parent / "data" / "retornos.csv"
returns = pd.read_csv(ruta, index_col=0, parse_dates=True)

corr = returns.corr()
print("=== Matriz de Correlación ===")
print(corr.round(2))

plt.figure(figsize=(7,5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            center=0, linewidths=0.5)
plt.title("Matriz de Correlación - Retornos Diarios", fontsize = 12)
plt.tight_layout()

ruta_fig = Path(__file__).parent.parent / "data" / "correlation_matrix.png"
plt.savefig(ruta_fig, dpi=150)
plt.show()
print("Gráfico Guardado")