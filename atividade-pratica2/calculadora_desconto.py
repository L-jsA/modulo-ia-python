# Calculadora de desconto em uma loja

# Informações do produto
nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o valor do produto: "))
porcentagem_desconto = int(input("Digite a porcentagem de desconto: "))

# Cálculo do desconto e preço final
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print(f"\nProduto: {nome_produto}")
print(f"Preço:  {preco_original}")
print(f"Desconto:  {porcentagem_desconto}%")
print(f"\nValor desconto  {valor_desconto:.2f}")
print(f"Total final com desconto: R$ {preco_final:.2f}")