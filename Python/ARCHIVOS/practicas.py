# # Indicar al usuario que ingrese una palabra
# # y asignarlo a la variable user_word.

# user_word = input("Ingrese una palabra: ")
# word_without_vowels = ""
# user_word = user_word.upper()
# for letter in user_word:
    
#     if(letter == "A"):
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     elif letter == "I":
#         continue
#     else:
#         word_without_vowels += letter

# print (word_without_vowels)
    

# toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
# si es par, evalúa un nuevo c0 como c0 ÷ 2;
# de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
# si c0 ≠ 1, salta al punto 2.


# #La hipótesis de Collatz
# num = int(input("Ingresa un numero: "))
# cont = 0
# while(num != 1):
#     if(num % 2 == 0):
#         num = num // 2
#     else: 
#         num = 3 * num + 1 
#     cont += 1   
#     print(num) 

# print("Iteraciones", cont)


#Ejercicio god 
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")

#Nota: la funcion range siempre será exclusiva con el limite superior
# for i in range(0, 6, 3):  donde start = 0, stop = 6 y step = 3
#     print(i)



# beatles = []

# beatles.append("John Lennon")
# beatles.append("Paul McCartey")
# beatles.append("George Harrison")

# print(beatles)


# for i in range(2):
#     miembro = input("Ingrese un miembro: ")
#     beatles.append(miembro)

# print(beatles)
# print("Beatles con miembros eliminados....")
# for i in range(2):
#     del(beatles[-(i)])


# beatles.insert(0, "Ringo Starr")

# print(beatles)



#PRACTICA CON LISTAS

int_list = [12,34,2,2,4,5,7,7,8,10,11]
int_list.sort()

new_list = []

for i in range(len(int_list)):
    if(int_list[i] not in new_list):

        new_list.append(int_list[i])

print(new_list)



tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # salida: 4

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)


my_list = ["car", "Ford", "flower", "Tulip"]
 
t = tuple(my_list)
print(t)


colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = {}
# Escribe tu código aquí.
for tup, value in colors:
     colors_dictionary[tup] = value
     
print(colors_dictionary)