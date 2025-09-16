number1 =   int(input("Digite o primeiro número: "))
number2 =   int(input("Digite o segundo número: "))
number3 =   int(input("Digite o terceiro número: "))

if number1 and number2 > number3:
    print(f'{number3}')

elif number3 and number2 > number1:
    print(f'{number1}')

elif number1 and number3 > number2:
    print(f'{number2}')

else:
    number1 == number2 == number3
    print(f'Os números são iguais.')