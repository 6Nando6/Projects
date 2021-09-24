n = int(input("Insira um número inteiro: "))
cont = n % 2 # Dividindo por 2, pois o resto será 0 se o numero for par.
cont1 = n % 3
if n == 2 or n == 3:
    print("Número primo")
else:
    if (cont1 and cont != 0):
        print ("Número primo")
    else:
        if cont1 or cont == 0:
            print("Número não primo")
        else:
            if cont or cont1 == 0:
                print("Número não primo")
