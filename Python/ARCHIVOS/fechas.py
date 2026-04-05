def is_year_leap(year): #si es año bisiesto
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year,month): # dias del mes
    if(year < 1500 and (month < 1 or month > 12)):
        return None
    if(is_year_leap(year) == True and month == 2):
        return 29
    else:   
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days[month-1]
    
def day_of_year(year, month, day):
    days = 0 
    monthBand = 0
    daysYear = 365 
    # verificar si el año es bisiesto
    if(is_year_leap(year)):
        daysYear = 366
    # ciclo for 1: para ir recorriendo los meses hasta llegar a month 
    for n in range(1,month):
        monthBand = days_in_month(year, n)
        days = days + monthBand 

    if(day < 1 or day > days_in_month(year,month)):
        return None
    else:
        return days + day    #retornar el numero de dias acumulado


#print(day_of_year(2000, 12, 31))

def is_prime(num):
    cont = 0
    for i in range (1,num+1):
       if(num % i == 0):
           cont += 1
           
    if(cont == 2):
        return num
    else:
        return  None

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
# Salida esperada 2 3 5 7 11 13 17 19