class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
    def seating_capacity(self, capacity= 50): # capacity= 50 es otorgarle el valor 50 por default a la variable
        return super().seating_capacity(capacity=50) 
    
bus = Bus("School", 180, 12) #crear objeto de la clase Bus
print(bus.seating_capacity())  #imprimir metodo de la clase bus