
def squares(list):
    if(not len(list)): return

    for i in range(len(list)):
        list[i] = list[i] ** 2 
    return list

my_list = []

n = int(input("Ingresa la cantidad de elementos de la lista: "))

for i in range(n):
    my_list.append((int(input("Ingresa un numero: "))))

print(squares(my_list))

