import math



numero = int(input("Insira um número: "))
count = len(str(numero))
p = 0

while p < count:
    dv = numero // 10 **p
    und = dv % 10
    p = p + 1
    
    print("dv",dv)
    print("und",soma)

# NA LINHA 9 ACHAR UMA FORMA DE SOMAR OS RESULTADOS OBTIDOS
