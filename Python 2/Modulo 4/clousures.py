# Clousures es una forma de usar funciones anidadas para crear funciones con estado (useState)
# como en React tenemos useState para guardar el estado del componente
# basicamente es una funcion que recuerda el valores de las variables de su entorno cuando fue creada
# incluso si la función original que las contenía ya no existe en memoria
def fabricar_multiplicador(n):
    factor = 1
    def multiplicar(x):
        return x * n + factor
    return multiplicar

duplicar = fabricar_multiplicador(2)
triplicar = fabricar_multiplicador(3)

print(duplicar(5)) # 11
print(triplicar(5)) # 16
