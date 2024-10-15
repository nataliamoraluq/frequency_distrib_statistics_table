#MAIN CLASS
frecuencyTable = []
orderedData = []
disorderedData = []

seeking = True 
#variable boolean q usaremos para recorrer o "buscar" (leer) los valores a contar y ordenar

#elementos varios
n = 0
xMax = 0
xMin = 0
rangeG = 0
amplitude = 0
logBase10 = 0 #mientras averiguo como traerme el log de base 10
valueOfK = 0

"""
def startingCalcs():
    #
    rangeG = xMax - xMin
    #
    valueOfK = 1 + (3.3 * (logBase10 * (n)))
    #
    amplitude = rangeG / valueOfK
    print(amplitude)
"""

inicialData = [
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

#Contar cada uno de los valores en la muestra y su fi (frecuencia absoluta / frecuencia simple)
def countValues():
    #using empty dictionary - frecuencia POR CADA VALOR
    freq={}
    for item in inicialData:
        if(item in freq):
            freq[item]+=1
        else:
            freq[item]=1
    for valueNumber,fi in freq.items():
        print(f"Valor: {valueNumber}, fs:{fi}")
countValues()

#DATOS TABULADOS (SIN ORDENAR)#

#INTERVALOS GENERADOS POR CLASE

#(PRUEBA - DESPUES DE Q SE ORDENAN, PARA CONTARLOS POR INTERVALO)
"""while seeking==True:
    for valueX in orderedData:
        #sea intervalX el intervalo definido
        A = 45,
        B= 53
        intervalX = [(A), (B)]
        if valueX in range(intervalX[0], intervalX[1]):
            print("")
        else:
            print("")"""

#CALCULOS
"""
--------------------------------
(MTC - MEDIDAS DE TENDENCIA CENTRAL)
1.	media aritmética, 
2.	moda,
3.	 mediana,
4.	 varianza,
5.	 desviación típica.
6.	P65
7.	Q3
8.	D3
9.	D8
10.	Q1
-----------------------------------------
"""

"""
-----------------------------------------
(MDV - MEDIDAS DE VARIABILIDAD)
11.	CV
12.	Rango intercuartil
13.	Índice de asimetría
14.	Curtosis
-----------------------------------------
"""