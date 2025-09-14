days = int(input("Digite a quantidade de dias trabalhados pelo funcionário: "))

pay = 80 * days 
discount = pay * 0.08
salary = pay - discount

print(f"O valor total a pagar corresponde à: R${salary:.2f}")