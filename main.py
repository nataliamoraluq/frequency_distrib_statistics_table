#CALCULOS
"""
--------------------------------
(MTC - MEDIDAS DE TENDENCIA CENTRAL) (all done)
0.1 punto medio (mi = xi)
1.	media aritmética, 
2.	moda,
3.	 mediana,
-----------------------------------------
(MDV - MEDIDAS DE VARIABILIDAD)
-----------------------------------------
4.	 varianza; ((sum(fi * xi2cuadrado) / n) - (xArit)2cuadrado)
5.	 desviación típica; raiz de s2cuadrado
6.	P65; li65 + ((((n * (k/100)) - (Fi - 1)) / fi) * A)
7.	Q1, Q3; 
8.	D3, D8; 
12.	Rango intercuartil; (Q3 - Q1)
13. CV; S / xArit
14.	Índice de asimetría; ((3 * (xArit - Med)) / S ) Si As = 0, {o Si As !=0 then Si As > 0, Si As < 0
15.	Curtosis; ((P75 - P25) / (P90 - P10)) * 0.5
-----------------------------------------
"""
#probando hasta q los intervalos generados por el programa sean
#los mismos q los intervalos creados por la prof
import math
# tabla array vacio para los nuevos datos a guardar
tabla = []
#------------------------------------------------------------------
#arrays 
modas = [] #array modas
mediaTot = [] #array media aritmetica
medidasTC = [] #resultados medidas de tendencia central
medidasDV = [] #resultados medidas de variabilidad
#------------------------------------------------------------------      
#muestra con los datos agrupados
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
#------------------------------------------------------------------
#
# ______________________ TABLA DE DISTRIBUCION DE FRECUENCIA (MAIN FUNCTION)___________________________
def tabla_frecuencia(datos):
    # 1) Se define n (200 datos de la muestra dada) y encontramos el rango
    # 1.a) definimos cals iniciales y variables tales como n. k. xmin ...
    n = len(datos)
    #print(f" muestra de n = {n}")
    # determinamos xmax y xmin
    xMax = max(datos) 
    xMin = min(datos)
    #print(f" Xmin = {xMin} & Xmax = {xMax}")
    #calculamos rango
    rango = max(datos) - min(datos)
    #print(f" Rango R = {rango}")
    #print(rango)
    # 2) Determinamos el número de clases (k) usando la regla de Sturges: k = 1 + 3.33 * log(n)
    k = int(round(1 + 3.33* math.log10(n)))
    #print(f" k = {k}")
    #print(k)
    # 3) Calculamos el ancho de clase (h) ---> h = A (amplitud)
    hAmplitud = round(rango / k)
    #redondeado al entero mas proximo
    """
    print("-----------------------")
    print(f" A = {hAmplitud}")
    print("-----------------------")"""

    # 4) Se crean los límites de clase

    # límites de clase con intervalos cerrados a la derecha
    # (es decir, el límite superior de cada clase está incluido)
    limites_clase = [xMin + i * hAmplitud for i in range(k+1)]
    # 5) Se llena y genera la tabla de distribuc. de frecuencia
    datosTabla = []
    #aqui tenemos algunas variables inicializadas para los valores a llenar y calc en la tabla
    facum = 0 #frec acumulada
    media = 0 #media
    #
    sumfixi2 = 0 # suma de fi * xi2
    #
    for i in range(k): 
        # frec absoluta / simple
        fi = len([x for x in datos if limites_clase[i] <= x < limites_clase[i + 1]])
        #frec acum
        facum += fi
        # punto medio
        xi = calcPuntoMedio(limites_clase[i], limites_clase[i + 1])
        #media por intervalo
        mediaPerInt = medAritmetica(fi, xi)
        #media
        media += mediaPerInt
        # para la varianza
        sumfixi2 += ((fi * xi) * xi)
        # se llena el espacio donde estaran los datos y calcs de la tabla
        datosTabla.append((limites_clase[i], limites_clase[i + 1], fi, facum, xi, mediaPerInt))
    #print(f"media sumada sin dividir{media}")
    #media aritmetica
    xArit = media / n
    medidasTC.append(xArit) #se agrega a un arreglo de MTC
    """
    print("-----------------------")
    print(f"media arit: {xArit}")"""
    #mediana
    mediana = calcMediana(datosTabla, n, hAmplitud, k)
    medidasTC.append(mediana)
    """
    print("-----------------------")
    print(f"mediana: {mediana}")"""
    #
    calcModas(datosTabla, k, hAmplitud)
    #
    medidasTC.append(modas)
    #
    #
    """
    print("-----------------------")
    print(f" suma de fi * xi2: {sumfixi2}")
    print("-----------------------")"""
    #fixi2 para calc varianza
    fixi2 = sumfixi2
    # varianza y desviac estandar
    s2 = varianza(n, fixi2, xArit)
    s = desvicEstandar(s2)
    #
    """
    print("-----------------------")
    print(f"varianza: {s2} y desviac. estandar: {s}")"""
    medidasDV.append(s2)
    medidasDV.append(s)
    #coeficiente de variacion
    cVariac = coefVariac(s, xArit)
    #percentiles prueba
    """
    p50 = quantiles(datosTabla, 50, 100, n, hAmplitud)
    print(f"P50: {p50}")"""
    #---------------------------------------------------
    # percentil 65
    p65 = quantiles(datosTabla, 65, 100, n, hAmplitud)
    #
    medidasDV.append(p65)
    # cuartiles 1 y 3
    q3 = quantiles(datosTabla, 3, 4, n, hAmplitud)
    q1 = quantiles(datosTabla, 1, 4, n, hAmplitud)
    #
    medidasDV.append(q3)
    medidasDV.append(q3)
    #deciles 3 y 8
    d3 = quantiles(datosTabla, 3, 10, n, hAmplitud)
    d8 = quantiles(datosTabla, 8, 10, n, hAmplitud)
    medidasDV.append(d3)
    medidasDV.append(d8)
    #rango intercuartil
    rI = calcRangoInterq(q3, q1)
    #print(f"Rango Intercuartil: {rI}")
    medidasDV.append(rI)
    #percentiles para calcular curtosis
    #
    p90 = quantiles(datosTabla, 90, 100, n, hAmplitud)
    p75 = quantiles(datosTabla, 75, 100, n, hAmplitud)
    #
    p25 = quantiles(datosTabla, 25, 100, n, hAmplitud)
    p10 = quantiles(datosTabla, 10, 100, n, hAmplitud)
    #curtosis
    cKurtosis = curtosis(p90, p75, p25, p10)
    #print(f"Curtosis: {cKurtosis}")
    medidasDV.append(cKurtosis)
    #print(f"Coeficiente de Variacion: {cVariac}")
    medidasDV.append(cVariac)
    #indice de asimetria
    aS = indiceAsime(xArit, mediana, s)
    #print(f"Indice de Asimetria: {aS}")
    medidasDV.append(aS)
    #
    #
    return datosTabla
# ==============================================================================
# ______________________________________ MEDIDAS DE TENDENCIA CENTRAL ______________________________________
# ----- MET. CALCULO PUNTO MEDIO(xi = mi)- ------
def calcPuntoMedio(li, ls): 
    mi = round(li + ls) / 2
    return mi
    #se recibe por parametro el li, el ls y se divide entre 2
    #el met retorna el valor de mi que llamamos en el met tabla_frecuencia, y se agrega a la
    #tabla junto con los demas valores
#
#------------------------------------------------------------------
# ----- MET. CALCULO - MEDIA ARITMETICA (x)------
def medAritmetica(fi, xi):
    return fi * xi
def calcMediana(tabla, n, a, k):
    #n = len(datos)
    #por posic
    temp = n/2
    index = 0
    for i in range(k):
        if tabla[i][3] >= temp:
            index = i
            break
    #lista datos mediana
    li = tabla[index][0]
    fi = tabla[index][2]
    Fi = 0 if index < 0 else tabla[index - 1][3]
    #calc mediana
    return li + (((temp - Fi) / fi) * a)
##------------------------------------------------------------------
#
# ----- MET. CALCULO - MODA ------
def calcModas(tabla, k, a):
    moda = 0
    for i in range(k):
        if tabla[i][2] > moda:
            moda = tabla[i][2]
    #
    for i in range(k):
        if tabla[i][2] == moda:
            d1 = tabla[i][2] - (0 if (i<=0) else tabla[i-1][2])
            d2 = tabla[i][2] - (0 if (i<=0) else tabla[i+1][2])
            if d1== 0 and d2 == 0:
                modas.append(tabla[i][0] + a)
                print(f"Alerta! como d1 y d2 = 0, (0/0+0) el valor de esta op. sera: 1")
            else:
                modas.append(tabla[i][0] + ((d1 / (d1+d2)) * a))
#------------------------------------------------------------------
# ______________________________________ MEDIDAS DE DISPERSION / VARIABILIDAD ____________________________________
# ----- MET. CALCULO - RANGO INTERCUARTIL------
def calcRangoInterq(q3, q1):
    return q3 - q1
#
#------------------------------------------------------------------
# ----- MET. CALCULO - INDICE DE ASIMETRIA------
def indiceAsime(xArit, Med, S):
    #Índice de asimetría; 
    #((3 * (xArit - Med)) / S ) 
    # Si As = 0, {o Si As !=0 then Si As > 0, Si As < 0
    aS = ((3 * (xArit - Med)) / S ) 
    """if aS==0:
        print(f"Indice de Asimetria: {aS}; Presenta distribuc. simetrica de los datos")
    elif aS>0:
        print(f"Indice de Asimetria: {aS}; Presenta distribuc. asimetrica de los datos; sesgo a la der")
    elif aS<0:
        print(f"Indice de Asimetria: {aS}; Presenta distribuc. simetrica de los datos; sesgo a la izq")
    else:
        print("hola")"""
    return aS
#------------------------------------------------------------------
#
# ----- MET. CALCULO - COEFICIENTE DE VARIACION------
def coefVariac(s, xArit):
    return s / xArit
#
#------------------------------------------------------------------
# ----- MET. CALCULO - VARIANZA ------
def varianza(n, fixi2, xAritmetica):
    if fixi2!=0 and n!=0 and xAritmetica!=0:
        s2 =  ((fixi2 / n) - (math.pow(xAritmetica, 2)))
        return s2
    else:
        print('Error! Datos vacios, revisar')
#------------------------------------------------------------------
# ----- MET. CALCULO - DESVIACION ESTANDAR------
def desvicEstandar(s2):
    return math.sqrt(s2)
#
# ----- MET. CALCULO - CUARTILES, DECILES Y PERCENTILES------
def quantiles(tablaDatos, tempk, denom, n,a):
    #sea denom = divisor de nk
    # tempk = k del quantil a calcular
    result = 0
    #
    nk = ((n * tempk)/ denom)
    #print(f"n: {n} + k: {tempk}, nk: {nk}, denom: {denom}")
    for posic, i in enumerate(tablaDatos):
        if i[3] >= nk:
            #print(i[3])
            lik = i[0]
            fi = i[2]
            Fik = 0 if posic==0 else tablaDatos[posic-1][3]
            result = lik + (((nk-Fik) / fi) * a)
            break
    #print(f" I [3]: {i[3]} , lik: {lik}, fi: {fi}, Fi - 1: {Fik}, A: {a}")
    return result
#
# ----- MET. CALCULO - CURTOSIS ------
def curtosis(p90, p75, p25, p10):
    return ((p75 - p25) /(p90 - p10)) * 0.5
#
# ______________________________________ METODOS PARA IMPRIMIR - MOSTRAR ____________________________________
# ----- MET. IMPRIMIR - MUESTRA ------
def printMuestra():
    print("Muestra con datos agrupados (200) no ordenados")
    print(datos)
#
# ----- MET. IMPRIMIR - MODAS------
def printModas():
    for i, mod in enumerate(medidasTC[2]):
        print(f"moda nro {i+1}: {mod}")
#
# ----- MET. IMPRIMIR - MTC------
#
def printMTC():
    print("----------------------------------------")
    print(f"Media aritmetica: {medidasTC[0]}")
    print(f"Mediana: {medidasTC[1]}")
    print(f"Modas:")
    printModas()
#
#
# ----- MET. IMPRIMIR - MDD------
def printMDD():
    print(f"Varianza: {medidasDV[0]}")
    print(f"Desviacion Estandar: {medidasDV[1]}")
    print("----------------------------------------")
    print(f"P65: {medidasDV[2]}")
    print(f"Q1: {medidasDV[3]}")
    print(f"Q3: {medidasDV[4]}")
    print(f"D3: {medidasDV[5]}")
    print(f"D8: {medidasDV[6]}")
    print("----------------------------------------")
    print(f"Rango Intercuartil: {medidasDV[7]}")
    print(f"Coeficiente de variacion: {medidasDV[9]}")
    print("----------------------------------------")
    print(f"Indice de Asimetria: {medidasDV[10]}")
    print("----------------------------------------")
    print(f"Curtosis: {medidasDV[8]}")
    print("----------------------------------------")

#
#
def printTable():
    # Calc tabla de distribuc. frecuencia
    tabla = tabla_frecuencia(datos)
    # Mostrar la tabla
    """
    print("tabla posic")
    print(tabla[0][0])"""
    print('-----------------------------------------')
    print('   TABLA DE DISTRIBUC. DE FRECUENCIAS ')
    print("----------------------------------------")
    print("Intervalos| fi | fa | xi | fi * xi |")
    print("----------------------------------------")
    
    for limInf, limSup, frecSim, frecAcum, puntoMedio, mediaPorInt in tabla:
        print(f"[{limInf} - {limSup}) | {frecSim} | {frecAcum} | {puntoMedio}| {mediaPorInt} |")
    print(' ')
    #printMTC()
    """
    print("----------------------------------------")
    print(f"Media aritmetica: {medidasTC[0]}")
    print(f"Mediana: {medidasTC[1]}")
    print(f"Modas:")
    printModas()"""

def menuOpc():
    #menu de opciones
    print(' ----------------- MENU-------------------')
    print(' Bienvenido! Elija una de las sig. opciones: ')
    print(' --------------------------------------------')
    print('0.) Mostrar la muestra dada')
    print('1.) Generar tabla de frecuencia con los datos de la muestra')
    print('2.) Mostrar las Medidas de Tendencia Central')
    print('3.) Mostrar las Medidas de Dispersion/Variabilidad')
    """print('4.) 4')
    print('5.) 5')"""
    print(' ---------------------------------------')
    resp = input('4.) Salir del menu\n')
    if resp == '0':
        printMuestra()
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuOpc()
        else:
            print('Cerrando...')
    elif resp == '1':
        printTable()
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuOpc()
        else:
            print('Cerrando...')
    elif resp == '2': 
        #se llama al met principal para q cargue los datos y calcule las MTC
        modas.clear()
        tabla = tabla_frecuencia(datos)
        #
        print('-----------------------------------------')
        print('   MTC - MEDIDAS DE TENDENCIA CENTRAL ')
        printMTC()
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuOpc()
        else:
            print('Cerrando...')
    elif resp == '3': 
        #varianza()
        tabla = tabla_frecuencia(datos)
        print('-----------------------------------------')
        print('      MDV - MEDIDAS DE VARIABILIDAD    ')
        printMDD()
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuOpc()
        else:
            print('Cerrando...')
    elif resp == '4': 
        print('Cerrando...')
    else: print('Err0r')
#
#main
def main():
    print('[______________________________________________________________]')
    print(' ')
    print('[_______ FREQUENCY DISTRIBUT. TABLE --- STATISTICS II _________]')
    print('[--- (TABLA DE DISTRIBUC. DE FRECUENC.) --- ESTADIST. II ---]')
    print('[______________________________________________________________]')
    menuOpc()
#
if __name__ == '__main__': 
    main()


"""
// ENUNCIADO ACT SEMANA 1 PARA DEFENDER (BAJO MUTUO ACUERDO) EL VIERNES DE LA SEMANA 3

Construir la tabla de distribución de frecuencias con los siguientes datos:

30	46	71	66	34	95	50	69	31	55	42	65	75	77	32	87	75	89	31	54
63	95	35	86	80	47	90	82	53	58	48	66	78	78	38	82	75	31	80	79
48	94	77	64	38	95	46	70	30	60	50	68	34	73	98	98	33	84	98	92
65	44	76	96	97	37	81	85	48	61	52	47	77	50	50	49	96	97	82	49
33	78	70	48	96	82	40	68	34	62	54	58	54	70	35	69	98	30	88	94
35	51	46	92	37	38	80	54	40	39	38	54	77	62	90	39	55	50	67	31
68	42	48	62	40	56	94	66	39	45	33	59	78	64	50	35	45	56	69	80
69	39	78	65	42	55	95	78	45	56	36	58	80	68	56	36	54	65	96	76
74	67	93	66	44	55	82	72	54	80	94	48	34	73	61	46	76	82	64	64
89	89	75	66	45	59	71	89	76	74	86	56	44	91	62	7a	8b	8c	7b	6a

Donde a,b,c son los tres últimos dígitos de tu cedula de identidad,
por ejemplo: 34.255.cba 997
En este caso: 30.416.997
A=9, B=9, C=7
LOS ULTIMOS 5 VALORES DE LA MUESTRA SERAN:
7a	8b	8c	7b	6a

-------------(DATA CON MI ABC)-------------
30	46	71	66	34	95	50	69	31	55	42	65	75	77	32	87	75	89	31	54
63	95	35	86	80	47	90	82	53	58	48	66	78	78	38	82	75	31	80	79
48	94	77	64	38	95	46	70	30	60	50	68	34	73	98	98	33	84	98	92
65	44	76	96	97	37	81	85	48	61	52	47	77	50	50	49	96	97	82	49
33	78	70	48	96	82	40	68	34	62	54	58	54	70	35	69	98	30	88	94
35	51	46	92	37	38	80	54	40	39	38	54	77	62	90	39	55	50	67	31
68	42	48	62	40	56	94	66	39	45	33	59	78	64	50	35	45	56	69	80
69	39	78	65	42	55	95	78	45	56	36	58	80	68	56	36	54	65	96	76
74	67	93	66	44	55	82	72	54	80	94	48	34	73	61	46	76	82	64	64
89	89	75	66	45	59	71	89	76	74	86	56	44	91	62	79	89	87	79	69
---------------------------

"""

#CALCULOS
"""
--------------------------------
(MTC - MEDIDAS DE TENDENCIA CENTRAL)
0.1 punto medio (mi = xi)
1.	media aritmética, 
2.	moda,
3.	 mediana,
-----------------------------------------
"""
"""
-----------------------------------------
(MDV - MEDIDAS DE VARIABILIDAD)
-----------------------------------------
4.	 varianza; ((sum(fi * xi2cuadrado) / n) - (xArit)2cuadrado) (done)
5.	 desviación típica; raiz de s2cuadrado (done)
6.	P65; li65 + ((((n * (k/100)) - (Fi - 1)) / fi) * A)
7.	P65, Q1, Q3; D3, D8; 
12.	Rango intercuartil; (Q3 - Q1)

13. CV; S / xArit (done)
14.	Índice de asimetría; ((3 * (xArit - Med)) / S ) Si As = 0, {o Si As !=0 then Si As > 0, Si As < 0 (done)
15.	Curtosis; ((P75 - P25) / (P90 - P10)) * 0.5 (done)
-----------------------------------------
"""