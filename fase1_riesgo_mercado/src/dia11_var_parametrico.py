import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import norm

ruta = Path(__file__).parent.parent / "data" / "retornos.csv"
returns = pd.read_csv(ruta, index_col = 0, parse_dates = True)

def parametric_var(returns_series, confidence = 0.95, portfolio_value = 100_000):
    """
    Calcula VaR y CVaR paramétrico asumiendo normalidad.

    Parámetro:
        returns_series  : Serie de retornos logarítmicos
        confidence      : Nivel de confianza (típicamente 95%)
        portfolio_value : Valor del portafolio en soles (default S/100,000)

    Retorna:
        (VaR,CVaR) en soles
    """

    mu      = returns_series.mean()
    sigma   = returns_series.std()
    z       = norm.ppf(1 - confidence)

    var_pct     = -(mu + z * sigma)
    cvar_pct    = -(mu - sigma * norm.pdf(norm.ppf(1 - confidence)) / (1 - confidence))

    return var_pct * portfolio_value, cvar_pct * portfolio_value

# Calcular para cada activo
print("=== VaR Paramétrico 95% - Portfolio S/100,000 ===\n")
for col in returns.columns:
    var, cvar = parametric_var(returns[col])
    print(f"{col}:")
    print(f"    VaR 95%:    S/{var:,.0f}")
    print(f"    CVaR 95%:    S/{cvar:,.0f}")