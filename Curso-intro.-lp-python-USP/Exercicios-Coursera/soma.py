numero = int(input("Insira um número inteiro: "))
count = len(str(numero))
soma = 0
resto = 0
while count != 0 and numero >= 0:
    resto = numero % 10
    numero = numero // 10
    soma = (soma + resto)
    count = count - 1

print(soma)
