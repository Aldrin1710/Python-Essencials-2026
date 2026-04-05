#Operadores Basicos en Python 
#suma, resta y multiplicacion
print(2+5)
print(2*5)
print(2-5)
print("\n") #salto de linea
#Division flotante

print(4/2)
print(4//2) #Operador division entera
print(6 // 4)
print(6. // 4)
print(14 % 4)

print(2+3*5)




#Ejercicio de operadores basicos
kilometers = 12.25

miles = 7.38

miles_to_kilometers = (miles*1.61)
kilometers_to_miles = (kilometers/1.61)

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


#Ejemplo: Convertidor de minutos a horas
minutos = 120020102
horas = 100

minutos_to_horas = minutos/60
horas_to_minutos = horas * 60

print(minutos, "minutos son ", round(minutos_to_horas, 4), "horas")
print(horas ,"horas son ", round(horas_to_minutos,3), "minutos")

a = 6
b = 3
a /= 2 * b
print(a, "\n")


#Operadores de comparacion
print(1 == 2) #compara si dos valores son iguales
print(1 != 2) #compara si dos valores son diferentes

#Variables en Python
#Como en cualquier otro lenguaje de programacion las reglas sintacticas para la declaracion de las variables son las mismas.
# 1. Pueden contener letras mayusculas como minúsculas, digitos y guiones bajos.
# 2. Deben comenzar con una letra o un guión bajo (Nunca con un número)
# 3. Python distingue entre mayusculas y minusculas, alicia y ALICIA son dos variables distintas.
# 4. No pueden usarse como nombres de variables las palabras reservadas (if, while, for, print)

# Regla especial. Al ser Python un lenguaje de tipado dinamico no necesitamos declarar el tipo de dato.

variable1 = "soy una variable de tipo cadena "
num_entero = 16
_flotante = 5.3

#10variable es un nombre incorrecto


print("\n",variable1)
print(num_entero)
print(_flotante)