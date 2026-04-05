# x = float(input("Ingresa el valor para x: "))

# # Escribe tu código aquí.
# y = 1/ (x+ 1/(x + 1 / (x + 1/x)))

# print("y =", y)


hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.
#Se suman los minutos y se dividen enter 60 
nuevos_min = (mins + dura) % 60
nueva_hora = int((mins+ dura) / 60) + hour

#validaciond de horas > 24

num_dia = int(nueva_hora / 24)

if num_dia >= 1:
    nueva_hora -= 24 * num_dia 


print(nueva_hora, nuevos_min)

