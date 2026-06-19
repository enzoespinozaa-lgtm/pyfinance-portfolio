import pandas as pd
import numpy as np
from pathlib import Path

ruta = Path(__file__).parent.parent / "data" / "retornos.csv"
returns = pd.read_csv(ruta, index_col = 0, parse_dates = True)

def historical_var(returns_series, confidence = 0.95, portfolio_value = 100_000):
    """
    Calcula VaR y CVaR histórico

    Parámetros:
        returns_series  : Serie de retornos logarítmicos diarios
        confidence      : Nivel de confianza (típicamente 95%)
        portfolio_value : Valor del portafolio en soles (default S/100,000)
    
    Retorna:
        (VaR, CVaR) en soles
    """
    sorted_r    = returns_series.sort_values()
    var_pct     = sorted_r.quantile(1 - confidence)
    cvar_pct    = sorted_r[sorted_r <= var_pct].mean()
    return abs(var_pct) * portfolio_value, abs(cvar_pct) * portfolio_value

print("=== VaR Histórico 95% - Portfolio S/100,000 ===\n")
for col in returns.columns:
    var, cvar = historical_var(returns[col])
    print(f"{col}:")
    print(f"    VaR 95%:    S/{var:,.0f}")
    print(f"    CVaR 95%:   S/{cvar:,.0f}\n")
