# Iniciamos um bloco try para capturar possíveis erros que podem ocorrer durante a execução do código
try:
    # Solicita ao usuário que digite o primeiro número inteiro
    numero1 = int(input("Digite o primeiro numero: "))
    
    # Solicita ao usuário que digite o segundo número inteiro
    numero2 = int(input("Digite o segundo numero: ")) 
    
    # Solicita ao usuário que digite a operação desejada (+, -, *, /)
    operacao = input("Digite a operação as opções são: (+ - * /) :")
    
    # Verifica se a operação digitada é válida
    if operacao not in ['+', '-', '*', '/']:
        # Se a operação for inválida, levanta um erro do tipo KeyError com uma mensagem personalizada
        raise KeyError("Operação invalida, as validas são: (+ - * /) ")

    # Realiza a operação de acordo com o operador digitado
    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    elif operacao == '/':
        resultado = numero1 / numero2

# Captura erro de entrada inválida (por exemplo, se o usuário digitar letras ao invés de números)
except ValueError:
    print("Erro: Entrada invalida, Digite um numero inteiro Ex: 10")

# Captura erro de operação inválida (capturado pelo raise KeyError)
except KeyError as keyerror:
    print(f"Erro: {keyerror}")

# Captura erro de divisão por zero
except ZeroDivisionError:
    print("Divisão por zero não é permitida")

# Bloco else que será executado apenas se nenhum erro ocorrer
else:
    # Exibe o resultado da operação
    print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}")