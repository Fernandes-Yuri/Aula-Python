#round2

seconds = int(input("Diga uma quantidade de segundos que deseja: "))
hour1 = seconds // 3600
seconds2 = seconds % 3600
minute = seconds2 // 60
seconds3 = seconds2 % 60

print(f" {hour1} hora , {minute} minutos, {seconds3} segundos.")