"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""
def primo():
    end = 6
    for num in range(2, 100+1):
      if num <2:
          print(False) 
      else:
        #creamos variable que cntiene true y se imprime si el num es primo y no se queda en el bucle
        es_primo=True
        for i in range(2, num):
            if num%i==0:
              es_primo = False
              break
              
              
        print(num,es_primo)

primo()