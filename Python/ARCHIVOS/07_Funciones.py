#Declaracion de una funcion
def function():
    print("Esta es una funcion")

function()


#Funciones con parametros
def message(number):
    print("Tu numero ingresado es: ",number)

message(1)


#Funciones con mas parametros
def multimessage(number, string, text):
    print("Tu numero es: ", number, "mientras que tu string es: ", string, "y tu texto es: ", text)
multimessage(3,"Hola mundo", "Aldrin")


#Paso de argumento por palabra clave: ya viene predefinido el orden con el nombre de las variables
def name(first_name, last_name):
    print(first_name, last_name)

name(first_name = "Aldrin" , last_name = "Novelo")
name(last_name = "Novelo", first_name = "Andony")


#Ejemplos
def perruno(first_dog, last_dog):
    print(first_dog," y ", last_dog)

perruno (last_dog = "poncho", first_dog = "Bob")


def introduction(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)

introduction("Aldrin")


def amikos(first_friend ="Javi", last_friend="eduardo"):
    print("Mi primer amigo fue: ", first_friend, "y  mi ultimo es: ", last_friend);

#amikos(last_friend="Carlos")
#amikos(first_friend="Toño")
#amikos("Lupe")


#Elemento nulo (None) en Python
def strange_function(n):
    if(n % 2 == 0):
        return True
    else: 
        return None

print(strange_function(1))
print(strange_function(3))


#Ejemplo año bisiesto: 
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year,month):
    if(is_year_leap(year) == True and month == 2):
        return 29
    else:   
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days[month-1]
    
test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr,mo,"-> ",end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


        