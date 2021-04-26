A = int(input("Introduzca el numero de personas que desea poner: "))  # Se solicita cual es el numero de personas
B = []   # Se inicializan las listas en 0 para luego ser rellenadas
C = []
y = 0
z = 0
for i in range(0, A):  # Este ciclo se repite la cantidad de veces que en este caso seria el Tamaño del arreglo, osea "A"
 B.append(input("Ingresa el nombre de las persona: "))  # Se llena la lista B con "A" Nombres
print(B)
for j in range(0, A):
 C.append(len(B[j]))   # Para cada nombre se lee el numero de caracteres, y se van añadiendo a la lista.
 print("El nombre", B[y], "tiene", C[z], "letras")
 y += 1
 z += 1
