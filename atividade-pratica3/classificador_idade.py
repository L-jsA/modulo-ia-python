# Programa que classifica a idade de um usuário

# O usuário irá inserir um número
idade = int(input("Digite uma idade: "))


# Condição para verificação do número inserido anteriormente
if idade >= 0 and idade <= 12:
    print("Você é criança")
elif idade >= 13 and idade <= 17:
    print("Você é adolescente")
elif idade >= 18 and idade <= 59:
    print("Você é adulto")
elif idade < 0 or idade > 110:
    print("Idade inválida")
else:
    print("Você é idoso")

