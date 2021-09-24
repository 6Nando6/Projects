#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
def  maior_primo(x):
    par = x % 2
    impar = x % 3
    cinco = x % 5
    if x ==2 or x ==1 or x ==3 or x ==5:
        return x
    if par and impar and cinco !=0:
        return x
    while x%2==0 or x%5 ==0 or x%3 ==0:
        x = x - 1
    return x
