import pandas as pd
import requests
from src.domain.interfaces.repository_interfaces import IExploradorMercadoRepository
import requests


class BrapiRepository(IExploradorMercadoRepository):
    def buscar_tickers_por_preco_maximo(self, preco_maximo: float) -> list[str]:
        url = "https://brapi.dev/api/quote/list"
        response = requests.get(url, params={"type": "stock"})
        data = response.json()

        tickers = [item["stock"] + ".SA" for item in data["stocks"]]
        return tickers
