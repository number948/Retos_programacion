"""* Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(word1,word2):
  #"transformar" caracteres a minusculas
  word1 = word1.lower()
  word2 = word2.lower()

  #transformar string a lista, imagino que para usar el metodo sort() que sirve en las listas
  word1_list = list(word1)
  word2_list = list(word2)

  # Los ordenamos. sort los ordena internamente, es decir, no regresa nada
  word1_list.sort()
  word2_list.sort()

  #volvemos a transformar variables a cadenas
  word1_ordenada = "".join(word1_list)
  word2_ordenada = "".join(word2_list)

  if word1_ordenada == word2_ordenada:
    return True
  else:
    return False

  
  

print(anagrama("amor","roma"))
    