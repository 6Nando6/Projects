print("Olá, eu sou o Dr. relógio! Muito prazer!!!")

Inicio = input("\n\n Como você se chama? ")
Nome = str(Inicio)

print("\n",Nome,"Agora vou calcular quanto tempo você viveu até agora")
resposta = input("\n Tudo bem ? ")

pergunta = input ("\n Me conta, em qual ano você nasceu ?")

print("\n Contando os minutos...........")
print ("\n Olhando pra ampulheta...")

Ano = int(pergunta)
print ("\n\n Se você nasceu em", Ano)
dias = Ano*365
Horas = dias*24
Min= Horas*60
Seg= Min*60
Idade = (2020 - Ano)
print("\n Olha só estou vendo aqui que...")
print ("\n Você tem: ", Idade, "anos /", dias, "dias /", Horas, "Horas /", Seg, "segundos")
