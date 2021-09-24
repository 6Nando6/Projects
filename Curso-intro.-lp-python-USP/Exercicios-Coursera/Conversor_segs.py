print("\n CONVERSOR DE SEGUNDOS")

print ("\n Vou te mostrar quantos segundos representa em uma escala de dias, horas, minutos e segundos. Tudo bem ? .......")
segundos_str = input("\n Por favor, entre com o número de segundos que deseja converter: ")
print("\n Bora converter isso aí.... \(^ u^)/")

total_segs = int(segundos_str)


horas = total_segs // 3600
dias = (horas//24)
horas = horas - dias*24
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60
print("\n\n você me disse", segundos_str, "segundos, certo ? Isso equivale a ...")
print("\n\n", dias, "dias, ", horas, "horas, ", minutos, "minutos e ", segs_restantes_final, "segundos.")

print("\n\n .......................Até logo............................")
print("\n\n.............pra calcular de novo é só cliclar F5............")
