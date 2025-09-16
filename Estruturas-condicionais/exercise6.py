hour = int(input("Digite um número correspondente a uma hora (0-23): "))

minutes = int(input("Digite um número correspondente a minutos (0-59): "))
 
if hour <= hour <= 23 and 0 <= minutes <= 59:
    print(f'O horário digitado foi {hour:02}:{minutes:02}')

else:
    print('Horário inválido!')

    