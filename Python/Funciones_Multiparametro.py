#funcion que calcula el factorial de un numero
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    
    return factorial_function((n-1)) * n
 
for n in range(1, 6): # probando
    print(n, factorial_function(n))



#Serie de fibonacci
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10): # probando
    print(n, "->", fib(n))

print("  ")

#Fibonaci con recursividad
def fibonacci(n):
    if n<1:
        return None
    if n<3:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 10): # probando
    print(n, "->", fib(n))