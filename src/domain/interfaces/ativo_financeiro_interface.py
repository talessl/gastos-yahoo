from abc import ABC, abstractmethod
from typing import Dict, Any


class IStockRepository(ABC):
    @abstractmethod
    def buscar_historico(self, ticker: str) -> Dict[str, Any]:
        """
        Deve retornar um dicionário contendo o preço atual 
        e o histórico de fechamentos para o cálculo dos indicadores.
        """
        pass
