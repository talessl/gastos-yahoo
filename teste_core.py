# arquivo: teste_core.py
from src.infra.repositories.brapi_repository import BrapiRepository
from src.infra.repositories.yahoo_finance_repository import YahooFinanceRepository
from src.domain.usecases.analisar_acoes_usecase import AnalisarOportunidadesUseCase


def main():
    # 1. Instanciamos a Infraestrutura
    repo_explorador = BrapiRepository()
    repo_acao = YahooFinanceRepository()

    # 2. Injetamos no Caso de Uso
    use_case = AnalisarOportunidadesUseCase(repo_explorador, repo_acao)

    # 3. Rodamos a aplicação buscando ações até 15 reais (para ter uma amostra maior)
    print("Iniciando a varredura na B3...")
    resultado = use_case.executar(preco_maximo=15.00)

    # 4. Exibimos o resultado
    print("\n✅ ANÁLISE CONCLUÍDA! Oportunidades encontradas:")
    if not resultado:
        print("Nenhuma ação atende aos critérios de sobrevenda no momento.")
    else:
        for acao in resultado:
            print(f"-> {acao['ativo']} | {acao['preco']} | RSI: {acao['indicadores']['rsi']} | Estocástico: {acao['indicadores']['estocastico']} | Status: {acao['status']}")


if __name__ == "__main__":
    main()
