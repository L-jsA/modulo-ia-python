import requests

def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print(f"Rua: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")

# Entrada do usuário
cep = input("Digite o CEP (somente número): ")
buscar_endereco(cep)