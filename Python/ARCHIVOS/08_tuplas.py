# Una tupla es una secuencia inmutable. Se puede comportar como una lista 
# pero no puede ser modificada en el momento.

tupla1 = (1,2,3,4)
tupla2 = 1,2.5,3,"hola"

print(1 not in tupla1)

print(tupla1," ", tupla2)

print(tupla1[0])
print(len(tupla1))
print("Uniendo tuplas: " + str(tupla1 + tupla2))
print(tupla1 * 2)
# Nota: cada elemento de una tupla puede ser de distinto tipo
# Si deseas leer los elementos de una tupla, lo puedes hacer de la misma manera que se hace con las listas.
'''
la función len() acepta tuplas, y regresa el número de elementos contenidos dentro;
el operador + puede unir tuplas 
el operador * puede multiplicar las tuplas, así como las listas;
los operadores in y not in funcionan de la misma manera que en las listas.
'''