#round5

valid_vote = int(input("Digite a quantidade de votos Valídos: "))
null_vote = int(input("Digite a quantidade votos Nulos: "))
blank_vote = int(input("Digite a quantidade de votos em Branco: "))

total = valid_vote + null_vote + blank_vote
percentage_v = total / valid_vote
percentage_v2 = percentage_v * 100
print(f"{percentage_v2}")
