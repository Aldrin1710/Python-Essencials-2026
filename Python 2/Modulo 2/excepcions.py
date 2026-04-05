try:
    x = int(input("Ingresa un número"))
    num = 10 / x
    print(num)
except ZeroDivisionError:
    print("nO puedes dividr entre cero")
except ValueError: 
    print("Debes ingresar un entero")
except: 
    print("No se pero algo fallo")

# importa el orden en donde coloquemos las excepciones
# una excepción puede tener mas de un bloque except donde puede entrar ya que existe un arbol de generalización
# Siempre colocar las escepciones más especificas primero
# las generales hasta el final
try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre cero!")
except ArithmeticError:
    print("¡Problema Aritmético!")

print("FIN.")


# raise exception_name 
def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("¿Qué pasó? ¿Un error?")

print("FIN.")

# ValueError:
# Ocurre cuando existe un argumento invalido o del tipo incorrecto (dividir una cadena entre un número)

# ArithmeticError:  excepción abstracta que incluye todas las excepciones causadas por
#  operaciones aritméticas como división cero o dominio inválido de un argumento.    

# BaseException: 
# La excepción más general, todas las demás excepciones provienen de esta. 

# IndexError:
# una excepción concreta que surge cuando se intenta acceder al elemento de una secuencia inexistente 
# (por ejemplo, el elemento de una lista).

# KeyboardInterrupt:
# surge cuando el usuario usa un atajo de teclado diseñado para terminar la 
# ejecución de un programa (Ctrl-C en la mayoría de los Sistemas Operativos)

# LookupError:
# excepción abstracta que incluye todas las excepciones causadas por errores resultantes de 
# referencias no válidas a diferentes colecciones (listas, diccionarios, tuplas, etc.).

# OverflowError:
# una excepción concreta que surge cuando una operación produce
#  un número demasiado grande para ser almacenado con éxito.

# ImportError:
# se generará una excepción cuando falla una operación de importación

# KeyError:
# Ocurre cuando se intenta acceder a un elemento inexistente dentro de una colección 
