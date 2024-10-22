import math
# datos agrupados -- entrada
datos = [
    30,46,71,66,34,95,50,69,31,55,42,65,75,77,32,87,75,89,31,54,
    63,95,35,86,80,47,90,82,53,58,48,66,78,78,38,82,75,31,80,79,
    48,94,77,64,38,95,46,70,30,60,50,68,34,73,98,98,33,84,98,92,
    65,44,76,96,97,37,81,85,48,61,52,47,77,50,50,49,96,97,82,49,
    33,78,70,48,96,82,40,68,34,62,54,58,54,70,35,69,98,30,88,94,
    35,51,46,92,37,38,80,54,40,39,38,54,77,62,90,39,55,50,67,31,
    68,42,48,62,40,56,94,66,39,45,33,59,78,64,50,35,45,56,69,80,
    69,39,78,65,42,55,95,78,45,56,36,58,80,68,56,36,54,65,96,76,
    74,67,93,66,44,55,82,72,54,80,94,48,34,73,61,46,76,82,64,64,
    89,89,75,66,45,59,71,89,76,74,86,56,44,91,62,79,89,87,79,69
]

def tabla_frecuencia(datos):
    print("--------- PRUEBA CALCS INICIALES E INTERVALOS--------------")
    print("-----------------------")
    print("----------- PRIMEROS CALCS ------------")
    # 1. Encontrar el rango de los datos
    rango = max(datos) - min(datos)
    print("Rango: R = ")
    print(rango)
    # 2. Determinar el número de clases (k)
    # Usando la regla de Sturges: k = 1 + 3.3 * log(n)
    n = len(datos)
    print("n =")
    print(n)
    k = int(round(1 + 3.33* math.log10(200)))
    #k = int(1 + 3.332* math.log10(n))
    print("k =")
    print(k)
    # 3. Calcular el ancho de clase (h) ---> h = A (amplitud)
    h = rango / k
    print("-----------------------")
    print("A =")
    print(h)
    print("-----------------------")
    # 4. Crear los límites de clase
    # límites de clase con intervalos cerrados a la derecha
    # (es decir, el límite superior de cada clase está incluido)
    limites_clase = [min(datos) + i * h for i in range(k + 1)]

    # 5. Crear la tabla de frecuencia
    frecuencias = []
    for i in range(k):
        # Contar la frecuencia de datos en cada clase
        frecuencia = len([x for x in datos if limites_clase[i] <= x < limites_clase[i + 1]])
        frecuencias.append((limites_clase[i], limites_clase[i + 1], frecuencia))

    return frecuencias
# Calcular la tabla de frecuencia
tabla = tabla_frecuencia(datos)
# Mostrar la tabla
print("---------------------")
print("Intervalos de Clase | Frecuencia1 (fi)")
print("---------------------")
for limite_inf, limite_sup, frecuencia in tabla:
    print(f"{limite_inf} - {limite_sup} | {frecuencia}")
