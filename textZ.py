#probando hasta q los intervalos generados por el programa sean
#los mismos q los intervalos creados por la prof
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

#print(f" xyz {x}")

def tabla_frecuencia(datos):
    print("--------- PRUEBA CALCS INICIALES E INTERVALOS--------------")
    print("-----------------------")
    print("----------- PRIMEROS CALCS ------------")
    # 1) Se define n (200 datos de la muestra dada) y encontramos el rango
    n = len(datos)
    print(f" muestra de n = {n}")
    #
    rango = max(datos) - min(datos)
    print(f" Rango R = {rango}")
    #print(rango)
    # 2) Determinamos el número de clases (k) usando la regla de Sturges: k = 1 + 3.3 * log(n)
    k = int(round(1 + 3.33* math.log10(200)))
    #k = int(1 + 3.332* math.log10(n))
    print(f" k = {k}")
    #print(k)
    # 3. Calcular el ancho de clase (h) ---> h = A (amplitud)
    h = round(rango / k)
    print("-----------------------")
    print(f" A = {h}")
    print("-----------------------")
    # 4. Crear los límites de clase
    # límites de clase con intervalos cerrados a la derecha
    # (es decir, el límite superior de cada clase está incluido)
    limites_clase = [30 + i * 8 for i in range(10)]

    # 5. Crear la tabla de frecuencia
    frecuencias = []
    for i in range(k):
        # Contar la frecuencia de datos en cada clase
        frecuencia = len([x for x in datos if limites_clase[i] <= x < limites_clase[i + 1]])
        frecuencias.append((limites_clase[i], limites_clase[i + 1], frecuencia))

    return frecuencias

def printTable():
    # Calc tabla de distribuc. frecuencia
    tabla = tabla_frecuencia(datos)
    # Mostrar la tabla
    print("---------------------")
    print("Intervalos de Clase | (fi)")
    print("---------------------")
    for limite_inf, limite_sup, frecuencia in tabla:
        print(f"({limite_inf} - {limite_sup}] | {frecuencia}")
        print("------------------------------------------------")

def menuOpc():
    #menu de opciones
    print(' ----------------- MENU-------------------')
    print(' Bienvenido! Elija una de las sig. opciones: ')
    print(' --------------------------------------------')
    print('1.) x')
    print('2.) 2')
    print('3.) 3')
    print('4.) 4')
    print('5.) 5')
    print('6.) Cerrar menu')
    print(' ---------------------------------------')
    resp = input('6.) Salir del menu\n')
    if resp == '1':
        print(printTable())
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuOpc()
        else:
            print('Cerrando...')
    elif resp == '2': 
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuOpc()
        else:
            print('Cerrando...')
    elif resp == '3': 
        print("aqui va la opc 3")
        #lista = defKruskal
    elif resp == '4': 
        print("aqui va la opc 4")
        #lista = defPrim
    elif resp == '5': 
        print("aqui va la opc 5")
    elif resp == '6': 
        print('Cerrando...')
    else: print('Err0r')


def main():
    print('[------------------------------------------]')
    print('[**** FREQUENCY DISTRIBUT. TABLE -- STATISTICS II ****]')
    print('[------------------------------------------]')
    menuOpc()

if __name__ == '__main__': 
    main()
