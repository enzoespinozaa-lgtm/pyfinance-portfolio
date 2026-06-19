import pandas as pd
import numpy as np
from scipy.stats import norm
from pathlib import Path

ruta = Path(__file__).parent.parent / "data" / "retornos.csv"
returns = pd.read_csv(ruta, index_col = 0, parse_dates = True)

def historical_var(returns_series, confidence=0.95, portfolio_value=100_000):
    sorted_r    =   returns_series.sort_values()
    var_pct     =   sorted_r.quantile(1-confidence)
    cvar_pct    =   sorted_r[sorted_r <= var_pct].mean()
    return abs(var_pct) * portfolio_value, abs(cvar_pct) * portfolio_value

def parametric_var(returns_series, confidence=0.95, portfolio_value=100_000):
    mu, sigma   = returns_series.mean(), returns_series.std()
    z           = norm.ppf(1-confidence)
    var_pct     = -(mu + z * sigma)
    cvar_pct    = -(mu - sigma * norm.pdf(norm.ppf(1-confidence)) / (1-confidence))
    return var_pct * portfolio_value, cvar_pct * portfolio_value

def monte_carlo_var(returns_series, confidence=0.95, portfolio_value=100_000, n=10_000):
    mu, sigma   = returns_series.mean(), returns_series.std()
    np.random.seed(42)
    simulated   = np.random.normal(mu, sigma, n)
    var_pct     = np.percentile(simulated, (1-confidence))
    cvar_pct    = simulated[simulated <= var_pct].mean()
    return abs(var_pct) * portfolio_value, abs(cvar_pct) * portfolio_value

# Tabla Comparativa

results = {}
for col in returns.columns:
    h_v, h_c = historical_var(returns[col])
    p_v, p_c = parametric_var(returns[col])
    m_v, m_c = monte_carlo_var(returns[col])
    results[col] = {
        'VaR Histórico':        h_v,
        'CVaR Histórico':       h_c,
        'VaR Paramétrico':      p_v,
        'CVaR Paramétrico':     p_c,
        'VaR Monte Carlo':      m_v,
        'CVaR Monte Carlo':     m_c
    }

tabla = pd.DataFrame(results).T.round(0)
print("=== Comparativa VaR 95% - Portfolio S/100,000 ===\n")
print(tabla.to_string())

ruta_csv = Path(__file__).parent.parent / "data" / "var_comparison.csv"
tabla.to_csv(ruta_csv)
print("\nTabla Guardada")