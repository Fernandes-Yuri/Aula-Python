# Calculadora Simples

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
opcao = int(input('Escolha uma opção: '))

if 1 <= opcao <= 4:
    a = float(input('Primeiro numero: '))
    b = float(input('Segundo numero: '))

if opcao == 1:
    print(f'Resultado da soma: {a + b}')
elif opcao == 2:
    print(f'Resultado da subtração: {a - b}')
elif opcao == 3:
    print(f'Resultado da multiplicação: {a * b}')
elif opcao == 4:
    if b != 0:
        print(f'Resultado da divisão: {a / b}')
    else:
        print('Erro. Não é possivel fazer divisão por zero')
else:
    print('Opção inválida')


