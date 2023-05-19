class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)

# linea para saber si  el objeto School_bus es instancia de la clase Vehicle
print(isinstance(School_bus, Vehicle))
