def calculadora():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+ - * /): ")

            if operacao == '+':
                resultado = numero1 + numero2
            elif operacao == '-':
                resultado = numero1 - numero2
            elif operacao == '*':
                resultado = numero1 * numero2
            elif operacao == '/':
                if numero2 == 0:
                    raise ZeroDivisionError
                resultado = numero1 / numero2
            else:
                raise ValueError("Operação inválida")

        except ValueError as e:
            print(f"Entrada inválida: {e}")
        except ZeroDivisionError:
            print("Inválido: Divisão por zero não é permitida. Tente novamente!")
        else:
            print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}")
            break  
calculadora()