#Las excepciones en Python nos ayudan a controlar los errores que comunmente se cometen
# a la hora de programar por alguna falla en el manejo de la logica de nuestro 
# programa. Vease el siguiente fragmento, en el cual se le solicita al usuario que ingrese  
# un numero entero, sin embargo, si el numero ingresado no es entero o ni siquiera es un valor      
# numérico, el programa terminará abruptamente dejando al usuario insatisfecho, por lo tanto    
# tenemos dos alternativas, disculparnos por el error o corregirlo. Ambos son caminos viables   
# en Python gracias a try-except. Para que sea facil de entender, el bloque de codigo que   
# se encuentra almacenado en la sentencia try, es la que se ejecuta esperando que sea efectiva,
# sin embargo si ocurre un error, la sentence except es la que nos ayuda a evitar que nuestro   
# programa finalice y aplica la regla: solucionarlo o pedir perdon. Es este caso,    
# optamos por lo segundo y simplemente  imprimimos que no sabemos que hacer. Pero lo más 
# optimo es solucionarlo no? De alguna manera... 
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except:
    print('No se que hacer con la entrada que se inserto')

#Nota: es mejor optar por el uso de excepciones especificas.

#Como en este caso, no solo estamos previniendo dos errores que pueden suceder si no   
# que estamos diciendo de manera particular que tipo de errores aplican en cada excepcion.
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con la entrada que se inserto')
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.') 


#Excepciones que es necesario conocer

# ZeroDivisionError: ocurre cuando se intenta forzar la division entre cero 
# ValueError: usa esta excepcion cuando estes manejando valores que pueden usarse de manera
#    inapropiada en algun contexto, generalmente cuando se utilizan funciones int() o float() con argumento inapropiado.    
# TypeError: ocurre cuando se intenta utilizarun tipo de dato en el contexto equivocado.
#   Ej. Utilizar un flotante como indice en una lista. 
# AttributeError: surge cuando se invoca a un metodo que no existe en un elemento con el que se trabaja. 
# SyntaxError: el control llega a una línea de código que viola la gramática de Pytho


tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)