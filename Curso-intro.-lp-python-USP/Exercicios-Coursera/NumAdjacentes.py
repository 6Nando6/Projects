#vai dizer sem tem ou nao numero adjascente repetido
n = int(input("Insira um número inteiro: ")) #saber se o numero adjascente é igual ou não
Count = False
while Count == False:
    b = n % 10
    b1 = n % 100
    b1 = b1 // 10
    n = n // 10
    if b == b1:
        print("sim")
    if b!=b1:
        print("não")
        Count = True
