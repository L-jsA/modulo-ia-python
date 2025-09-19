
import random
import string

def gerar_senha(tamanho):
letras = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(letras) for _ in range (tamanho))
return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada:"))
senha_aleatoria = gerar_senha(tamanho_senha)
print(f"Sua senha gerada é: {senha_aleatoria}")