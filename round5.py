#round5

valid_vote = int(input("Digite a quantidade de votos Valídos: "))
null_vote = int(input("Digite a quantidade votos Nulos: "))
blank_vote = int(input("Digite a quantidade de votos em Branco: "))

total = valid_vote + null_vote + blank_vote
percentage = 100 / total
result_valid = valid_vote * percentage
result_null = null_vote * percentage
result_blank = blank_vote * percentage

print(f" O total de votos foi de {total} \n O percentual de votos válidos foi de: {result_valid:.2f}% \n O percentual de votos nulos foi de: {result_null:.2f}% \n O percentual de votos em brancos foi de: {result_blank:.2f}%")