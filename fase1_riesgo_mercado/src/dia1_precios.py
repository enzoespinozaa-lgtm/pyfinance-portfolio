import yfinance as yf
import pandas as pd
from pathlib import Path

tickers = ["BAP", "ALICORC1.LM", "EPU"]

data = yf.download(tickers, start="2020-01-01", end="2024-12-31")["Close"]
data.dropna(inplace=True)

print(data.shape)
print(data.head())
print(data.tail())

ruta = Path(__file__).parent.parent / "data" / "prices.csv"
data.to_csv(ruta)
print("Archivo guardado en:", ruta)
