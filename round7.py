factory = float(input("Digite o valor de fábrica do veículo: "))

distribuidor = 1.28 * factory
taxes = 1.45 * factory
total = distribuidor + taxes

print(f" O valor do veículo com o acréscimo do distribuidor é: {distribuidor:.2f}")
print(f"O valor do veículo com o acréscimo dos impostos é: {taxes:.2f}")
print(f"O valor total é {total:.2f}")