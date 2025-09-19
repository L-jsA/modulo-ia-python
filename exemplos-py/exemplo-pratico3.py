import requests

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    usuario = dados["results"][0]
    nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")

obter_usuario_aleatorio()