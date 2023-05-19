"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 """


class Poligono():
    def area(self):
      pass

#crear clases que contengan cada poligono
class Triangulo(Poligono):
  def __init__(self, base, altura):
      self.base = base
      self.altura = altura
  def area(self):
      return (self.base * self.altura) / 2
  
class Cuadrado(Poligono):
  def __init__(self, altura):
      self.altura = altura
  def area(self):
     return(self.altura**2)
  
class Rectangulo(Poligono):
   def __init__(self, base, altura):
      self.base = base
      self.altura = altura
   def area(self):
      return (self.base * self.altura)
   
def area(poligono):
    print("El área del polígono es:", poligono.area())

triangulo = Triangulo(10.0, 5.0)
cuadrado = Cuadrado(4.0)
rectangulo = Rectangulo(5.0, 7.0)
area(triangulo)
area(cuadrado)
area(rectangulo)
