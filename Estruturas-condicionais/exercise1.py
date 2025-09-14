#exercise1
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f'a sua média é {media:.2f} e você foi aprovado.')
else:
    print(f'a sua média é {media:.2f} e você foi reporvado')



