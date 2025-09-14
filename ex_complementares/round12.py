length = float(input("Digite o comprimento da parede: "))
width = float(input("Digite a largura da parede: " ))
heigth = float(input("Digite a altura da parede: "))

form = 2 * heigth * ( length + width )
result = form / 1.5 

print (f" {result:.2f}")