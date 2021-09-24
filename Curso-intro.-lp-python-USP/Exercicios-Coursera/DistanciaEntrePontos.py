import math
x1 = float(input("> Insira valor x1: "))
y1 = float(input("> Insira valor y1: "))
x2 = float(input("\n> Insira valor x2: "))
y2 = float(input("> Insira valor y2: "))
dist= math.sqrt((pow((x1-x2),2) + (pow((y1-y2),2))))
#print("\n R: A distância entre os dois pontos é: ",dist)
if dist >= 10:
    print("\n Longe")
else:
    print("\n Perto")
