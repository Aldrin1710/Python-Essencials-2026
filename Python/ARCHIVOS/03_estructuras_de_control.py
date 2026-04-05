# Sentencia IF: compara una preposicion y si es verdadera, produce una accion. O en su contraria, no hace nada. O si? Si usamos else (entonces)
# entonces la cosa cambia.

#Ejemplo vago de codigo real
# if the_weather_is_good:
#     go_for_a_walk()
# else:
#     go_to_a_theater()

var = 2
if(var % 2 == 0): #verifica si es multiplo de 2
    print("El numero es par")
else:
    print("El numero es impar")

# #Sentencia con Elif
# if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()



# Ciclo while: Nos ayuda a controlar una ejecución continua de un bloque de codigo siempre y cuando se cumpla la condicion del bucle.
#  #while condition
#     instructions
num = 10
while(num < 20):
    print(num)
    num= num+1

print("\n")
#Ciclo for: misma idea que while, pero esta controlado mediante un numero de iteraciones y un paso. 
num = 10
print("Ciclo for: ")
for i in range(num):
     print("El valor de i es", i)
#Es decir, repite una seccion de codigo siempre y cuando se cumpla una condicion que esta sujeta a un incremento/decremento llamado paso
# en este caso, mientras que i=0 este en el rango de num = 10, y por defecto, en un ciclo for el valor de la variable de control, aumenta.
# en 1 por iteracion. Es por eso que imprime los primeros 10 digitos.  


#Break y Continue
#Break sirve para terminar la ejecucion de un bucle en un momento determinado de ejecucion
#Continue sirve para saltarse la ejecucion actual del bucle y evaluar la condicion del siguiente bucle 



# Codigo para calcular el numero mayor dado n numeros 
# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")



# palabra_reservada = "chupacabra"
# palabra_ingresada = input("Ingrese una palabra: ")

# while(True):
#     if(palabra_ingresada == palabra_reservada):
#         break
#     palabra_ingresada = input("Ingrese una palabra: ")
    
# print("Saliste del bucle")    

#bucle for
for i in range(5):
    print("Esta es la repeticion: " + str(i))

print(" ")
for i in range(5,10):
    print("Esta es la repeticion: " + str(i))

for i in range(2,9,3):
    print("Valor de i: ", i)