# #Lectura de datos via consola
# print("Dime lo que sea...")
# anything = input()
# print("Hmm...", anything, "... ¿en serio?")

# #Input con argumento: le quita la chamba al print
# anything = input("Dime lo que sea...")
# print("Hmm...", anything, "...¿en serio?")

# #Lectura de valores y conversión en Python
# num = float(input("Ingrese un numero"))
# num_cuadrado = num ** 2.0
# print("El numero", num, " a la potencia 2 es ",num_cuadrado)


# #Cadenas y sus operadores

# #Operador concatenacion '+'
# fnam = input("¿Me puedes dar tu nombre por favor? ")
# lnam = input("¿Me puedes dar tu apellido por favor? ")
# print("Gracias. ")
# print("\nTu nombre es " + fnam + " " + lnam + ".")


# #Operador duplicador '*'

# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")


#  LAB 01. EXPRESION CULERA 1

# x = int(input("Ingresa un numero: "))

# print("El resultado de la expresion es: " + str( 1 / (x + (1 / (x + (1 / (x + 1/x)))))))

# # LAB 02. Expresion Culera 2
# hora_inicio = int(input("Ingresa la hora de inicio: "))
# minuto_inicio = int(input("Ingresa el minuto de inicio: "))
# duracion = int(input("Ingresa la duracion del evento: "))

# minutos_totales = duracion + minuto_inicio

# minutos_finalizacion = minutos_totales % 60 #esto ya esta, hay que encontrar otra forma de hallar las horas ( hora_entera - hora_inicial)
# hora_finalizacion =  hora_inicio + (minutos_totales // 60)

# print("Finaliza a las: " + str(hora_finalizacion) +":" + str(minutos_finalizacion))


x = 11 
y = 4

x = x % y
x = x % y
y = y % x
print(y)