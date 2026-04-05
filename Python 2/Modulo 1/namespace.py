# import math     -> math.pi
# from math import *  -> importa todas las entidades del mundo sin,pi,etc.
from math import sin as seno, pi as pi314
# import math as alias

print(seno(pi314 / 2))

def sin(x):
    print("Soy la función seno redefinida en el namespace del programa", pi)

pi = 3.142121

sin(pi)

# Como podemos observar podemos importar módulos en python usando import, y usar una importación selectiva usando from-import


from random import *

print(dir(random))


from platform import platform, machine,processor,system,version
 
print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print(system(), version())


from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)