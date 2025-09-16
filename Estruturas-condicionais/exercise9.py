side1= float(input("Digite o valor do primeiro lado: "))
side2= float(input("Digite o valor do segundo lado: "))
side3= float(input("Digite o valor do terceiro lado: "))

if side1 != side2 and side2 != side3 and side1 != side3:
    print("O triângulo é escaleno.")

elif side1 == side2 and side2 == side3 and side1 == side3:
    print("O triângulo é equilátero.")  

else: 
    print("O triângulo é isósceles.")