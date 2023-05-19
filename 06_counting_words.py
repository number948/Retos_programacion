"""/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */"""
import re
word = "Hola, mi nombre es ashley. Mi nombre completo es Ashley Caroca es"

words = word.lower()
no_space_word = words.split(" ")

for i in range(0, len(no_space_word)):
    if no_space_word[i] != "0":
        count = 1
        for x in range(i+1, len(no_space_word)):
            if no_space_word[i] == no_space_word[x]:
                count = count + 1
                no_space_word[x] = "0"
        if count > 1:
            print(no_space_word[i])

