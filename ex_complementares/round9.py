#round9 
name = (input(" Parabéns você é o terceiro ganhador do premio total de, R$ 780.000,00. \n Prêmio será dividido entre três ganhadores: \n O PRIMEIRO RECEBE 46% DO VALOR DO PRÊMIO \n O SEGUNDO RECEBE 32% DO VALOR DO PRÊMIO \n O TERCEIRO REBECE O PRÊMIO 22% DO VALOR DO PRÊMIO \n Digite agora seu nome para ser liberado o valor a receber do seu  prêmio: "))

win =  780000
winner1 = 0.46 * win
winner2 = 0.32 * win
winner3 = 0.22 * win 
print (f" Parabéns {name}, você foi o Terceiro colocado e seu prêmio é, R${winner3:.2f} \n ")