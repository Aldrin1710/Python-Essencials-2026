class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' en ' + self.galaxy


sun = Star("Sol", "Vía Láctea")
print(sun)

# función issubClass(classOne, classTwo) verifica si classOne es subclase de classTwo
# isinstance(object,class)
# obj1 is obj2 verifica si apuntan al mismo objeto en memoria

# Probando propiedades: variables de instancia.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__() # otra forma Super.__init__(self)
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)


#MRO DE PYTHON: HERENCIA MÚLTIPLE
# BASICAMENTE es quien decide que método ejecutar en dado caso de que haya 
# algun problema de herencia del mismo nivel
class Madre:
    def saludar(self):
        return "Hola, soy tu Madre"

class Padre:
    def saludar(self):
        return "Qué onda, soy tu Padre"

# ¡Atención a los paréntesis! Madre está a la IZQUIERDA
class Hijo(Madre, Padre): 
    pass

aldrin = Hijo()
print(aldrin.saludar())

print(Hijo.__bases__[0].__name__ + " y " + Hijo.__bases__[1].__name__)   

