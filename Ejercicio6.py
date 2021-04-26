palabra = input("Introduce una palabra: ")
reversed_word = palabra  # La variable reverse_word tomara el valor de la varialbe palabra
palabra = list(palabra)  # La variable palabra sera ahora una lista de la palabra ingresada
reversed_word = list(reversed_word)
reversed_word.reverse()
if palabra == reversed_word:   # Si la palabra al revez es igual a la original, entonces:
    print("La palabra Si es un palíndromo")
else:
    print("La palabra No es un palíndromo")
