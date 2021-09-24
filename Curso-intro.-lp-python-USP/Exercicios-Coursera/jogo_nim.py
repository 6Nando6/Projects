print(' Bem-vind@ ao jogo do NIM! \n\n Escolha: ')
def jogo():
    partida_isolada = 1
    campeonato = 2


print(''' 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato''')

escolha = int(input())
if escolha == 1:
        print('\nVoce escolheu uma partida isolada!\n')
if escolha == 2:
        print('Voce escolheu um campeonato!\n')

print( '''**********  Rodada 1 ***********''')

n= int(input('Quantas peças? '))
m= int(input('Limite de peças por jogada? '))
if m >0:
    if n % (m+1) ==0:
        print('Você começa!')
        tira = int(input('Quantas peças voçê vai tirar? '))
        if tira <= m:
            n = n - tira
            print('Você tirou' ,tira, 'peça')
            print('Há', n ,'peças no tabuleiro')
            if tira >m:
                print('O valor deve ser menor')          
    else:
        print('Computador começa')
        

