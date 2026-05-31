import yfinance as yf
import pandas as pd
from pathlib import Path

# Activos - Credicorp | Alicorp | Índice BVL General
tickers = ["BAP", "ALICORC1.LM", "EPU"]

# Descargar datos: Precios ajustados
data = yf.download(tickers, start="2020-01-01", end="2024-12-31")["Close"]
data.dropna(inplace=True)

# Verificar datos
print(data.shape)
print(data.head(1))
print(data.tail(1))
print(data.dtypes)

# Guardar datos
ruta = Path(__file__).parent.parent / "data" / "precios.csv"
data.to_csv(ruta)
print("Archivo guardado correctamente")


