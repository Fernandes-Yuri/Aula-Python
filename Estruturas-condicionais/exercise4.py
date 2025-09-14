#Exercise 4

letra = input('Digite a letra: ')

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'u':
    print(f'A sua letra é uma vogal {letra}')
else:
    print(f'A sua letra ({letra}) é uma consoante.')