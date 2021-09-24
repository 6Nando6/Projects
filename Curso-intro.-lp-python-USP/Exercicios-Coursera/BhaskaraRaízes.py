import math
print ("\n BHASKARA")
a = float(input("\nInsira a valor de a: "))
b = float(input("\nInsira o valor de b: "))
c = float(input("\nInsira o valor de c: "))
Delta = (b**2 -4*a*c)
if Delta == 0: # Possui apenas uma raiz real
    raiz1 = (-b + math.sqrt(Delta)) / (2*a)
    print("\n a raiz desta equação é",raiz1)
else:
    if Delta < 0: #Delta negativo não possui raíz real
        print("\n esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(Delta)) / (2*a)
        raiz2 = (-b - math.sqrt(Delta)) / (2*a)
        if raiz1 > raiz2:
            print("\n as raízes da equação são", raiz2,"e",raiz1)
        else:
            print("\n as raízes da equação são", raiz1,"e",raiz2)
