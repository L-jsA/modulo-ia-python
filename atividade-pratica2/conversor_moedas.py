# Valores das moedas
valor_em_reais = float(input("Digite o valor em reais para conversão: "))
cotacao_dolar = 5.20
cotacao_euro = 6.15

# Conversão
conversao_em_dolares = valor_em_reais / cotacao_dolar
conversao_em_euros = valor_em_reais / cotacao_euro

# Exibição dos resultados
print(f"Saldo em reais: R$ {valor_em_reais}")
print(f"Valor em dolares: $ {cotacao_dolar}")
print(f"Saldo em euro: $ {conversao_em_euros}")