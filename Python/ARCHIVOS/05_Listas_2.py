#Copiar una lista a otra 
list_01 = [1,2,3]
list_02 = list_01[:]
#List_02 = list_01[0:3]
print(list_02)


#Eliminar rebanadas de una lista
my_list = [10, 8, 6, 4, 2]
del my_list[1:3] #El end siempre es n-1
print(my_list)

#Operador IN and Not In
#Ambos verifican si un elemento esta o no en una lista, otorgando un valor booleano

list_03 = [12,3,5,6]

print(5 in list_03)
print(16 not in list_03)
print(16 in list_03)


#Aplicaciones de listas

squares = [x ** 2 for x in range(10)]
print(squares)

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)