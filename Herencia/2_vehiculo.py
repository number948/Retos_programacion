class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle): # esto es crear una clase bus que 
  #solo hereda todos los metodos y variables de la clase Vehiculo, no tiene otras lineas de codigo
  pass

vehicle_1 = Bus("School Volvo", 180, 12)

print("Vehicle name: ", vehicle_1.name, "Speed: ", vehicle_1.max_speed, "Mileage: ", vehicle_1.mileage)