#Receba 3 números inteiros na entrada e imprima

#crescente

#se eles forem dados em ordem crescente. Caso contrário, imprima

#não está em ordem crescente
a = int(input(" Insira o 1º número inteiro: "))
b = int(input(" Insira o 2º número inteiro: "))
c = int(input(" Insira o 3º número inteiro: "))
if a<b<c:
    print("crescente")
else:
    print("não está em ordem crescente")
