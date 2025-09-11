# Conversor de ano bissexto

ano = int(input("Digite o ano: "))

if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
    # Verifica se o ano é divisível por 4 
    # Se o ano é divisível por 4 e por 100, então ele só será bissexto se também for divisível por 400
    print(f"{ano} é um ano bissexto!")
else:
    print(f"{ano} não é bissexto!")