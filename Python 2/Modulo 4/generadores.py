class Suma():
    def __init__(self,i):
        self.__n = 0
        self.__tope = i
        self.__sum = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__n > self.__tope:
            raise StopIteration
        self.__sum += self.__n
        self.__n += 1
        return self.__sum 

for i in Suma(10):
    print(i)


# # Forma con funcion generadora
# nums1 = [x for x in range(10000000)] # Crear una lista con 10 millones de numeros gasta mucha RAM

# nums2 = (x for x in range(10000000)) # Crear un generador con 10 millones de numeros gasta muy poca RAM

# Forma con una función definida 
def generar_nums_hasta(n):
    for i in range(n):
        yield i
        print("Hola") # Utilidades reales: Limpieza de recursos o mensajes  de depuración.

num2 = generar_nums_hasta(10)

print(next(num2)) # 0

print(next(num2)) #1
