segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
horas = segundos // 3600
dias = (horas//24)
horas = horas - dias*24
segs_restantes = segundos % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")
