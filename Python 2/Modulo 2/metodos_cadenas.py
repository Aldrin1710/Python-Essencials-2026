# Método Sort
list1.sort() # Afecta a la MISMA lista
print(list1)

#capitalize: convierte el primer caracter de una cadena a mayúscula y el resto a minúscula
print("hola".capitalize)

# Demostración del método endswith(): comprueba si una cadena termina con un sufijo específico
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

#Demostracion del método startswith(): la misma gata pero al inicio
print("Starts: ","tasteback".startswith("tas"))

# Demostración del método find(): busca si una subcadena existe dentro de una cadena y devuelve su posicón, 
# en caso contrario devuelve -1
print("FIND: ", "hola mundo".find("mundo"))

# Demostración del método isalpha():
print("Moooo".isalpha()) #True 
print('Mu40'.isalpha())

# Demostración del método isdigit():
print("1234".isdigit())     

#Demostración isupper() y islower():
print("HOLA".isupper()) #True
print("HOLA".islower()) #False

#Demostración del metodo join()
print("-".join(["Hola", "Mundo"]))

#Demostración del método lower()
print("Next SEmEster".lower())

#Demostración del método replace()
print("Hola Mundo".replace("Hola", "Adios"))

#Demostración del método split()
print("Taste Back".split()) 

#Demostración del método strip()
print("[" + "   This Love   ".strip() + "]")

# Demostración del método title():
print("Yo solo sé que no sé nada. Parte 1.".title())

#Demostración del método upper():
print("Next SEmEster".upper())


