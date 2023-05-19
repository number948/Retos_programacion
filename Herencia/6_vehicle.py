class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def nombre(self):
        return self.name


class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount


class Car:
    def __int__(self):
        print("el nombre de este auto es ")


class Carrito(Car):
    def __init__(self):
        print("el auto es un volvo")
        super().__init__()


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

cars = Carrito()
#print("nombre: ")
