# Programa que calcula o Índice de massa corporal

# O usuário irá inserir dois valores
peso_corporal = float(input("Digite o seu peso corporal: "))
altura_metros = float(input("Digite sua altura(com pontos ou vírgulas: "))

# Aqui será feito o calculo dos número inseridos 
peso_altura = peso_corporal / (altura_metros ** 2)

# Condição que os números serão aplicados
if peso_altura <= 18.5:
    print("Classificação: Abaixo do peso")
elif peso_altura <= 25:
    print("Classiicação: Normal")
elif peso_altura <= 30:
    print("Classificação: Sobrepeso")
else:
    print("Obeso")

# Resultado com decimal
print(f"Seu IMC é: {peso_altura:.2f}")