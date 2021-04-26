materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"] #Se almacena en una lista las materias
notas = []   # Aquí se van a acumular las notas ingresadas por el usuario
for materia in materias:
    nota = float(input("¿Ingrese la nota que obtuvo en " + materia + "?: ")) #El usuario ingresa la nota que ha obtenido en cada una de las materias
    notas.append(nota)  # Este .append agrega una nota por cada materia
for i in range(len(materias)):
    print("En " + str(materias[i]) + " has sacado: " + str(notas[i]))   # Para facilitar se convierten todos los datos en texto
