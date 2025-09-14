#round3

chicken = int(input("Digite a quantidade total de fragos que precisam de chip: "))
right = 0.40 * chicken
left = 0.35 * chicken * 2
result = right + left

print(f"O valor total de frangos que precisam de apenas um chip é: R${right:.2f},\n"
      f"já o valor total de frangos que precisam de 2 chips é: R${left:.2f}.\n"
      f"Totalizando o total de R${result:.2f}")