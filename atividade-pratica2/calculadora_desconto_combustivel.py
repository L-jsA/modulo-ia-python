# calculadora de consumo de combustível

# Dados da viagem
distancia_percorrida = int(input("Digite a distância percorrida em Km: "))
combustivel_gasto = int(input("Digite a quantidade gasta de combustivel em Litros: "))

# Cálculo do consumo
consumo = distancia_percorrida / combustivel_gasto

# Exibição do resultado
print("\nDados da Viagem:")
print(f"Distancia Percorrida: {distancia_percorrida} Km")
print(f"Combustivel Gasto: {combustivel_gasto} Litro(s)")
print(f"Consumo Medio: {consumo:.2f} km/l")