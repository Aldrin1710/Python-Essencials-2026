#Un diccionario en Python es una estructura de datos que almacena un conjunto de pares y claves.

dictionary = {"gato": "katze", "perro": "hund", "conejo": "kaninchen"}
print(dictionary)
print("El valor de la clave conejo: ",dictionary["conejo"])

#Cuestiones a considerar:
# 1. Una clave puede se de cualquier tipo de dato y debe de ser ÚNICA
# 2. Un diccionario no es una lista, un diccionario almacena pares clave-valor
# 3. Solo funciona en un sentido (clave - > valor) mas no (valor -> clave)

print("------------------")
#Comprobar si una clave esta en el diccionario
words = ['gato', 'leon', 'perro']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print("La palabra no se encuentra en el diccionario")
print("------------------")

#Metodos items: retorna o regresa una lista de todas las claves dentro del diccionario
for word in words:
    for key in dictionary.keys():
        if word == key:
            print(key, "->", dictionary[key])
print("------------------")

#Metodos items: retorna una lista de tuplas, cada tupla es un elemento clave-valor. 
for spanish, deustch in dictionary.items():
    print(spanish, "->", deustch)

print("------------------")
#Para ordenar el diccionario, usamos sorted.
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

#Agregar elementos y eliminar elementos
dictionary['leon'] = "Löwe"
print(dictionary)

del dictionary['perro']
print(dictionary)