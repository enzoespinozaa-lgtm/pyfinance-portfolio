# A continuación
# Practicaremos el scaling del VaR para un período de tiempo 't'

# Cargamos las librerías
import pandas as pd
import numpy as np
from pathlib import Path

# Cargamos los datos
ruta = Path(__file__).parent.parent / "data" / "retornos.csv"
returns = pd.read_csv(ruta, index_col = 0, parse_dates = True)

def historical_var(returns_series, confidence = 0.95, portfolio_value = 100_000):
    sorted_r = returns_series.sort_values()
    var_pct = sorted_r.quantile(1 - confidence)
    cvar_pct = sorted_r[sorted_r <= var_pct].mean()
    return abs(var_pct) * portfolio_value, abs(cvar_pct) * portfolio_value

def scale_var(daily_var, days):
    return daily_var * np.sqrt(days)

print("=== Scaling de VaR - BAP | S/100,000 ===\n")
var_1d, _ = historical_var(returns["BAP"])

for days, label in [(1, "1 día"), (10, "10 días"), (21, "1 mes"), (63, "1 trimestre")]:
    print(f"VaR {label:<12}: S/ {scale_var(var_1d, days):,.0f}")

print("\nNota: Válido solo bajo supuesto de independencia")
print("Subestima el riesgo en períodos de crisis (volatility clustering).")