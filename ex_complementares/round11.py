value1 = int(input("Digite aqui a quantidades de pães vendidos: "))
value2 = int(input("Digte aqui a quantidade de Broa vendidas: "))

bread1 = 0.38 * value1
bread2 = 4.50 * value2 
sum = bread1 + bread2 
savings = 0.10 * sum 

print(f"O total de vendas foi: R${sum:.2f}")
print(f"O valor correspondente à 10% das vendas para guardar em poupança é exatamente: R${savings:.2f}")