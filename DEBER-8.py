# Crear una lista con las asignaturas del curso
asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

# Crear una lista vacía para almacenar las notas
notas = []

# Preguntar al usuario la nota de cada asignatura
for asignatura in asignaturas:
    nota = float(input(f'¿Qué nota has sacado en {asignatura}? '))
    notas.append(nota)

# Mostrar las asignaturas con sus respectivas notas
for i in range(len(asignaturas)):
    print(f'En {asignaturas[i]} has sacado {notas[i]}')
    # Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Mostrar asignaturas por pantalla
print("Las asignaturas del curso son:")
for asignatura in asignaturas:
    print(f"- {asignatura}")
 # Crear una lista con los números del 1 al 10
numeros = list(range(1, 11))

# Mostrar los números en orden inverso, separados por comas
print(', '.join(map(str, numeros[::-1])))
# Crear una lista con las asignaturas del curso
asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

# Recorrer la lista e imprimir el mensaje para cada asignatura
for asignatura in asignaturas:
    print(f'Yo estudio {asignatura}')
# Crear una lista vacía para almacenar los números ganadores
numeros_ganadores = []

# Preguntar al usuario por 6 números ganadores
for i in range(6):
    numero = int(input(f'Introduce el número ganador {i+1}: '))
    numeros_ganadores.append(numero)

# Ordenar la lista de menor a mayor
numeros_ganadores.sort()

# Mostrar los números ganadores ordenados
print('Los números ganadores ordenados son:')
print(numeros_ganadores)