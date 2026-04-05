#CREANDO LISTAS EN PYTHON
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.
 
numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.


#FUNCIONES LEN & DEL
print(len(numbers)) # Imprimiendo el tamaño de la lista

del(numbers[3])  #Borrando el elemento 4 de la lista
print(numbers)


lista = [1,2,3,4]

#append es un metodo de listas que inserta un elemento al final de la lista
lista.append(5)
print(lista)

#insert lo mete en una psocion especifica de la lista
lista.insert(0,150)
print(lista)


#Lista vacia
print("--------Lista vacia--------")
lista_vacia = []

for i in range(5):
    lista_vacia.append(i+1)

print(lista_vacia)

#Insertar un arreglo en forma inversa
lista_vacia2 = []
for j in range(5):
    lista_vacia2.insert(0, j+1)

print(lista_vacia2)



#Ordenamiento Bubble Sort
my_list = [8,13,21,65,5]
band = True

while band:
    band = False
    
    for i in range(len(my_list) - 1):
        if(my_list[i] > my_list[i+1]):
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            band = True
    
print(my_list)

#Funcion sort
List_3 = [12,43,54,65]

List_3.sort()
print(List_3)

