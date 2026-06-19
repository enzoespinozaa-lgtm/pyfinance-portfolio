from signal import Sigmasks
import pandas as pd
import numpy as np
from pathlib import Path

# Cargar retornos
ruta = Path(__file__).parent.parent / "data" / "retornos.csv"
returns = pd.read_csv(ruta, index_col = 0, parse_dates = True)

def monte_carlo_var(returns_series, confidence = 0.95, portfolio_value = 100_000, n = 10_000):
    """
    Calcula VaR y CVaR por simulación Monte Carlo.

    Parámetros:
        returns_series  : Serie de retornos logarítmicos
        confidence      : Nivel de cofnianza (default 95%)
        portfolio_value : Valor del portafolio en soles
        n               : Número de simulaciones (default 10,000)
    
    Retorna:
        (VaR, CVaR) en soles
    """

    mu      = returns_series.mean()
    sigma   = returns_series.std()

    # Generar 'n' retornos simulados desde la distribución normal
    np.random.seed(42)
    simulated = np.random.normal(mu, sigma, n)

    var_pct     = np.percentile(simulated, (1 - confidence)*100)
    cvar_pct    = simulated[simulated <= var_pct].mean()

    return abs(var_pct) * portfolio_value, abs(cvar_pct) * portfolio_value

# Calcular para cada activo

print("=== VaR Monte Carlo 95% - Portfolio S/100,000 ===\n")
for col in returns.columns:
    var, cvar = monte_carlo_var(returns[col])
    print(f"{col}:")
    print(f"    VaR 95% :   S/{var:,.0f}")
    print(f"    CVaR 95%:   S/{cvar:,.0f}")