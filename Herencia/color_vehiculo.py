class Vehicle:

    color = "white" #aqui definimos la llamada variable de clase, es una variable global

    def __init__(self, name, max_speed, mileage): #est es un metodo
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


b = Bus("School", 180, 12)
print("Color:", b.color, "Vehicle name: ", b.name, "Speed: ", b.max_speed, "Mileage: ", b.mileage) #esto es como acceder al dato ej: nombre mediante el objet b de la clase bus

c = Car("Toyota", 200, 13)
print("Color: ", c.color, "Vehicle name: ", c.name, "Speed: ", c.max_speed,"Mileage: ", c.mileage )