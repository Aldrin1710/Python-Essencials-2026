class Person: 
    __slots__ = ["__name", "__lastName"]  # con slots definimos el conjunto de atributos de la clase
    def __init__(self, name, lastName):
        self.__name = name
        self.__lastName = lastName
        
    
    def getName(self):
        return self.__name

class Student(Person):
    __slots__ = ["__id"]
    count = 0 # Variable de la clase
    def __init__(self, name, lastName, id):
        super().__init__(name, lastName)    
        self.__id = id
        Student.count += 1

    def getId(self):
        return self.__id
    
aldrin = Student("Aldrin", "Novelo", "219281")
# print(aldrin.__dict__, aldrin.getName())
# print(aldrin.getId() + "\n")
# print(Student.__dict__)

# XD se pueden agregar atributos de la nada
aldrin.semestre = 6
print(aldrin.__dict__)