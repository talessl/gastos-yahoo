import yfinance as yf
from domain.interfaces.ativo_financeiro_interface import IStockRepository


class YahooFinanceRepository(IStockRepository):
    def buscar_historico(self, ticker) -> dict:
        try:
            acao = yf.Ticker(ticker)
            historico = acao.history(period="60d")

            if historico.empty:
                raise ValueError(
                    f"Nenhum dado encontrado para o ticker {ticker}")

            # Extrai o preço mais recente e a lista de preços passados
            preco_atual = float(historico['Close'].iloc[-1])
            precos_fechamento = historico['Close'].tolist()

            # Retorna os dados crus formatados para o Caso de Uso
            return {
                "ticker": ticker,
                "preco_atual": preco_atual,
                "historico_fechamento": precos_fechamento
            }

        except Exception as e:
            # Em uma arquitetura real, você pode criar um erro customizado aqui
            raise Exception(f"Erro ao buscar dados no Yahoo Finance: {str(e)}")
