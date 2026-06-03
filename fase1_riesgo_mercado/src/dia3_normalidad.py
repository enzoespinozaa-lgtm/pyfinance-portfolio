import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats

# Cargar retornos
ruta = Path(__file__).parent.parent / "data" / "retornos.csv"
returns = pd.read_csv(ruta, index_col=0, parse_dates=True)

# Si no hubieramos limpiado los NA:
# returns.dropna(inplace=True)

# Estadísticos de distribución
print("== Test de Normalidad ==\n")
for col in returns.columns:
    sk = returns[col].skew()
    kurt = returns[col].kurtosis()
    stat, p = stats.jarque_bera(returns[col])
    print(f"{col}:")
    print(f" Skewness: {sk:.4f}")
    print(f" Kurtosis: {kurt:.4f}")
    print(f" Jarque-Bera: {stat:.4f}, p-value: {p:.6f}")
    print(f" Normal: {'No' if p < 0.05 else 'Sí'}")

    
