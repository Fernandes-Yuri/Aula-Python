#first exercise
print("1) Saudação com nome.")

name = input("Bem-vindo, esta é uma trilha do meu exercício, informe seu nome: ")
print(f"Olá {name}")


#second exercise
print("2) Soma e multiplicação de dois valores.")


value1 = float(input("Digite o valor: "))
value2 = float(input("Digite o valor: "))

print(f"Olá {name}, a soma dos valores é: {value1+value2}")
print(f"{name}, o resultado da multiplicação dos valores é: {value1*value2}")


#thrid exercise
print("3) Cálculo da média aritmética.")


print(f"Olá {name}, o calculo da média aritmética está disponível")
note1 = float(input("Digite a sua nota: "))
note2 = float(input("Digite a sua nota: "))
note3 = float(input("Digite a sua nota: "))

media = (note1 + note2 + note3) / 3
print(f"A média aritmética simples da sua nota é: {media:.2f}")


#fourth exercise
print("4) Conversão de Celsius para Fahrenheit.")

celsius = float(input(f"{name}, Digite a temperatura a ser convertida: "))
fahrenheit = (celsius * 1.8)  + 32

print(f"A temperatura em Fahrenheit é {fahrenheit}")



#fifth exercise
print("5) Cálculo do IMC.")


weight = float(input(f"{name}, Essa é uma calculadora de IMC, digite seu peso: "))
height = float(input(f"{name}, seu peso é de {weight}Kg, agora digite sua altura: "))
imc = weight / (height **2)
print(f"{name}, o valor do seu IMC, é: {imc:.2f}")



#sixth exercise
print("6) Área de um triângulo.")


base = float(input(f"{name}, está é uma calculadora de área de um triângulo. Digite a base: "))
height2 = float (input(f"{name}, Insira agora a altura: "))
area = base * height2 / 2
print(f"{name}, o valor da área é de {area:.2f}")




#seventh exercise
print("7) Desconto de 10% no produto.")

price = float(input(f"{name}, digite o valor do produto: "))
percentage = price * 0.9
print(f"{name}, o valor do produto com desconto de 10% é: R${percentage:.2f} ")



#eighth exercise
print("8) Salário do vendedor de veículos.")

name2 = input("Digite seu nome: ")
seller = input(" Digite o nome do vendedor: ")
units = int(input(f"Quantos veículos, {seller} vendeu?"))
value_unit = float(input("Qual valor de cada carro? "))

multiplication = value_unit * units
multiplication_2 = multiplication * 0.02 + (200+2500)

print(f"{name2}, foi vendido o total de R$ {multiplication:.2f} pelo vendedor {seller},"
      f"deve-se pagar ao vendedor o valor de: {multiplication_2:.2f}")



#ninth exercise
print("9) Troca de valores entre duas variáveis.")

number = int(input("Digite um número: "))
number2 = int(input("Digite outro número: "))

number, number2 = number2, number

print("Depois da inversão")
print(f"{number}")
print(f"{number2}")


#tenth exercise
print("10) Inverter uma centena.")

triplet = int(input("Digite uma centena de sua escolha: "))
triplet_result = str (triplet) [::-1]

print(triplet_result)