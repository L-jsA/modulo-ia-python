import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    chave = moeda + "BRL"
    if chave not in dados:
        print("Moeda não encontrada.")
        return

    info = dados[chave]
    print(f"Cotação {moeda}/BRL")
    print("Valor atual:", info["bid"])
    print("Valor máximo:", info["high"])
    print("Valor mínimo:", info["low"])
    print("Última atualização:", info["create_date"])


moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
consultar_cotacao(moeda)