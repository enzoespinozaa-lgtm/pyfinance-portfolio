# Objetivo: Calcular retornos logarítmicos de los activos de la cartera
# -> Logarítmicos: Propiedad aditiva
# -> Estadística: Retornos logarítmicos tiene un comportamiento más próximo a la normalidad

# r_t = Ln(P_t) - Ln(P_{t-1})
# r_t = Ln(P_t/P_{t-1})

import pandas as pd
import numpy as np
from pathlib import Path

# Cargar precios guardados el día anterior
ruta = Path(__file__).parent.parent / "data" / "prices.csv"
data =pd.read_csv(ruta, index_col=0, parse_dates=True)

# Calcular retornos logarítmicos
returns = np.log(data / data.shift(1)).dropna()

# Estadísticas descriptivas
print("=== Retornos Logarítmicos Diarios ===")
print(returns.describe().round(4))

# Volatilidad anualizada (multiplicar por raíz de 252 días hábiles)
ann_vol = returns.std() * np.sqrt(252)
print("\n=== Volatilidad Anualizada ===")
print(ann_vol.round(4))

# Guardar retornos
ruta_retornos = Path(__file__).parent.parent / "data" / "retornos.csv"
returns.to_csv(ruta_retornos)
print("\nRetornos guardados correctamente")

