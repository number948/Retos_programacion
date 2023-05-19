class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


#crear una instacia

my_vehiculo = Vehicle(248, 345)
print(my_vehiculo.max_speed, my_vehiculo.mileage)
