class Perruno:
    counter = 1
    def __init__(self, age, name):
        self.age = age
        self.name= name
        Perruno.counter += 1
    def get_name(self):
        return self.name

bob = Perruno(11, "Bob")

print(bob.__dict__)
print(Perruno.__dict__)


# Para saber de que tipo es un objeto podemos usar type y __name__
print(Perruno.__name__)
print(type(bob).__name__)

print(Perruno.__module__)


import time
class Timer:
    def __init__(self, hrs, minutes, seconds):        
        if (hrs < 0 or hrs > 23) or (minutes < 0 or minutes > 59) or (seconds < 0 or seconds > 59):
            self.hrs = 0
            self.minutes = 0
            self.seconds = 0
        else:   
            self.hrs = hrs
            self.minutes = minutes
            self.seconds = seconds

    def __str__(self):
        return f"{self.hrs:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hrs += 1
        if self.hrs == 24:
            self.hrs = 0

    def prev_second(self):
        self.seconds -= 1
        if self.seconds < 0:
            self.seconds = 59
            self.minutes -= 1
        if self.minutes < 0:
            self.minutes = 59
            self.hrs -= 1
        if self.hrs < 0:
            self.hrs = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
timer.next_second()
print(timer)
    
