#Alcance de las variables en Python
#Ejemplo 1. Definimos una variable en el cuerpo del programa, si llamamos a esa variable dentro de una función, 
# reconocerá el valor de la variable a pesar de no estar declarada en el cuerpo de la función?
def my_function():
    print("¿Conozco a la variable?", var)

var = 1
my_function()
print(var) #En efecto, en Python una variable que existe fuera 
            # de una función tiene alcance dentro del cuerpo de la función.


#Ejemplo 2: Llamada a una Variable global dentro de una función
def function_global():
    global variable #llamada de la variable global
    variable = 2
    print("El valor de la variable global es: ", variable)

variable = 1   #variable global
function_global() #Al declarar una variable global dentro del cuerpo de la funcion, Python evita la repetición y accede
print(variable)       # a la variable creada fuera del cuerpo, var = 1. Por lo tanto, los cambios que se dan en la funcion 
                      # afectan a la variable original y se modifica su valor de 1 a 2. 



#Interaccion de una función y sus argumentos

#Ejemplo: Paso por parametro
def func_escalar(escalar):
    print("Yo recibi un valor: ", escalar)
    escalar = escalar + 1
    print("Ahora tengo otro escalar: ", escalar)

escalar = 1
func_escalar(escalar)
print(escalar) #Notamos que el valor de la variable, no cambia, ya que solo pasamos un valor de argumento (una copia de lo que contiene la variable)
        

#Ejemplo: Paso por referencia
def func_listas(my_list_2):
    print("Print #1:", my_list_2)
    del my_list_2[0] # Presta atención a esta línea.
    print("Print #2:", my_list_2)
 
# si se modifica la lista identificada por el parámetro 
# (nota: ¡la lista, no el parámetro!), la lista reflejará el cambio.
my_list_2 = [2, 3]
func_listas(my_list_2)
print("Print #3:", my_list_2)  

#Nota. en Python las listas al ser objetos dinámicos se pasan por referencia, es decir, se manda la direccion de memoria de la lista original
# y por ende, todos los cambios que se le apliquen pues se veran reflejados en la lista. 