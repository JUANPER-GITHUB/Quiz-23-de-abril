alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #Se almacena una lista con las letras del abecedario
for i in range(len(alfabeto), 1, -1):  # Cuenta de para atras, desde el numero de letras del abecedario hasta 1.
    if i % 3 == 0:      #Ubica la letras que se encuentran en los espacios de un múltiplo de 3
        alfabeto.pop(i-1)    #Con la función .pop se elimina los números múltiplos de 3
print(alfabeto)
