
str1 = input("Ingrese una cadena: ").lower()
str2 = input("Ingresa otra cadena: ").lower()

# Dos palabras son anagramas si tienen las mismas letras (en orden diferente) pero forman diferentes palabras.
# 1. Que las cadenas sean del mismo tamaño
# anagram = True
# if(len(str1) == len(str2)):
#     # 2. Asegurarse que cada letra de la cadena 1 este en algún lado de la cadena 2
#     letters_str2 = list(str2)
#     for ch in str1:
#         # 3. Si se encuentra le letra en la cadena 2, la "quitamos"
#         if(ch in letters_str2):
#             letters_str2.remove(ch)
#         else: 
#             anagram = False
#             break 
#     # 4. Verificar si son anagramas o no
#     if(anagram): 
#         print("Son anagramas")  
#     else: 
#         print("No son anagramas")
# else: 
#     print("No son anagramas")


anagram = True
if(len(str1) == len(str2)):
    # 2.1 Ordenemos ambas listas con sorted y verificar si son iguales 
    list_1 = list(str1)
    list_2 = list(str2)
    letters_str1 = sorted(list_1)
    letters_str2 = sorted(list_2)
    if(letters_str1 == letters_str2):
        print("Son anagramas")
    else: 
        print("No son anagramas")
else: 
    print("No son anagramas")    





