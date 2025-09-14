#round4

value = float(input("Qual o valor em Reais, você deseja converter em Doláres ? \n"
                    ""))
dollar = value / 5.41
dollar_t = value / 5.61

print(f" Seu valor em dólar Comercial é: {dollar:.2f}")
print(f" O valor em dólar de Turismo é: {dollar_t:.2f}")