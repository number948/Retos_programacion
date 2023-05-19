"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    num_start = 0
    num_actual =1

    for i in range(50):
        print(num_start)
        num = num_start+num_actual
        num_start = num_actual
        num_actual = num


fibonacci()