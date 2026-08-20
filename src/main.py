from infra.repositories.yahoo_finance_repository import YahooFinanceRepository

repositorio = YahooFinanceRepository()

# Buscando dados da Petrobras
dados = repositorio.buscar_historico("PETR4.SA")

print(f"Ação: {dados['ticker']}")
print(f"Preço Atual: R$ {dados['preco_atual']:.2f}")
print(f"Tamanho do histórico: {len(dados['historico_fechamento'])} dias")
