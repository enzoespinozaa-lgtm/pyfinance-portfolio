import pandas as pd
import numpy as np
from scipy.stats import norm
from pathlib import Path

ruta = Path(__file__).parent.parent / "data" / "retornos.csv"
returns = pd.read_csv(ruta, index_col = 0, parse_dates = True)

w = np.array([0.4, 0.4, 0.2])
portfolio_value = 100_000

port_returns = pd.Series(
    returns.values @ w,
    index = returns.index
)

print("=== Retoros del Portafolio ===")
print(f"Media diaria:               {port_returns.mean():.6f}")
print(f"Volatilidad anualizada:     {port_returns.std() * np.sqrt(252):.4f}")

# VaR Histórico del portafolio
sorted_r    = port_returns.sort_values()
var_pct     = sorted_r.quantile(0.05)
cvar_pct    = sorted_r[sorted_r <= var_pct].mean()

var_hist    = abs(var_pct) * portfolio_value
cvar_hist   = abs(cvar_pct) * portfolio_value

print(f"\n=== VaR Histórico Portafolio ===")
print(f"VaR 95%     : S/{var_hist:,.0f}")
print(f"CVaR 95%    : S/{cvar_hist:,.0f}")

# VaR analítico (matriz de covarianza)
cov_matrix      = returns.cov()
port_vol        = np.sqrt(w @ cov_matrix.values @ w)
z               = norm.ppf(0.05)
var_analytic    = abs(z) * port_vol * portfolio_value

print(f"\n=== VaR Analítico Portafolio ===")
print(f"Volatilidad diaria portafolio: {port_vol:.6f}")
print(f"VaR  95%: S/ {var_analytic:,.0f}")