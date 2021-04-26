while True:
 tamañoarreglo = int(input("Ingrese el tamaño del arreglo: "))  # Se solicita la cantidad de multiplos que se quieren
 multiplo = int(input("Ingrese el número de múltiplos: "))   # Se solicita el numero del cual se desean conocer multiplos
 a = []   # Se agrega una lista vacia para luego ser rellenada con los multiplos
 for i in range(1, tamañoarreglo + 1):  # Este ciclo se repite la cantidad de veces que en este caso seria el Tamaño del arreglo
  a.append(i * multiplo)   # Se introducen el la lista todos los multiplos dependiendo del numero dado por el usuario
 print(a)   # Se imprime la lista
 p = input("¿Desea volver a calcular de nuevo? : ")   # se le pregunta al usuario si desea volver a calcular
 if p == "no":
  print("¡Vuelva pronto!")
  break
