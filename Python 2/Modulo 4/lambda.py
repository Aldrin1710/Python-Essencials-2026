# El uso de la función lambda es para crear funciones anonimas
# Simplificar el codigo y evitar escribir funciones que solo se van a usar una vez|

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y
 
for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')
 
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2) # 2x^2 - 4x + 2 



# Función Map(function, list)

# La función map() aplica una función a cada elemento de un iterable (como una lista) y 
# devuelve un nuevo iterable con los resultados.
list1 = [x for x in range(5)]
list2 = list(map(lambda x : 2 ** x,list1))
print(list2)


# Filter(function, list)
# Primer parametro: función que devuelve un valor booleano
# Segundo parametro: lista a filtrar
# Si la funcion devuelve true se mete dentro de la nuestra lista filtrada
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)