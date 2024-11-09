import scipy.stats as stats

#
"""
def metDataCalcs(listData, xArit, s):
    #hours, medidasTC[xArit], medidasDV[sDesv]
    n = len(listData)
    medArit =  xArit
    desvEst = s
    dataProb.append(n)
    dataProb.append(medArit)
    dataProb.append(desvEst)
    return dataProb
#luego
#en mets aparte de prob para c/u
#CALC PROB PARA INCOME > 44

#(fuera de esto en el menu) ----> dataC = metXcalc(hours, medidasTC[xArit], medidasDV[sDesv])
    #para datacalc:
    # n = dataCalc[0]
    # miu = dataCalc[1]
    # sigma = dataCalc[2]
    #luego para este met
    #segun la probabilidad de la variable a calcular, se tomara el valor de esa prop como X 
    #es decir (por ejemplo si P(X > 44) then prob = 44)

#

def probabIncome(dataCalc, prob):
    #vers corregida beta2 PERO en este caso part de prob, dan valores muy altos
    #por lo q se colocara cualquier valor para z solo para mostrar algo ok?
    
    varToZ = ((prob - (float(dataCalc[1]))) / (float(format(dataCalc[2],'.2f')) / (math.sqrt(float(dataCalc[0]) ) )))
    #OJO vartoZ con 4 decimales
    print(f" --------------- Calculo de probabilidad de SALARIO con: --------------------------------------")
    print(f"[ (X - μ ) / (σ / raiz de (n) ) ]")
    print(f"-----------------------------------------------------------------------------------------------")
    print(f" A) Probabilidad de que el salario de una persona sea mayor que 44: ")
    print(f" Resultado del calc. de probabilidad con TLC: {format(varToZ, '.4f')}")
    print(f"-----------------------------------------------------------------------------------------------")
    print(f"AVISO!!!")
    print(f"En este caso particular, el valor a buscar de z en la tabla es MUY alto")
    print(f"por ello, a fin de calcular la Prob de P (X > 44)")
    print(f"se tomara en cuenta valores de la web q se asimilen a los de la tabla dada en clase")
    zValueTable = input('Ingrese el valor de equivalente en la tabla\n')
    #zValue se se multipl por 100 para tener el valor porcentual
    z = (float(zValueTable))
    zValue = 1.0 - z
    print(f" zValue: {zValue}")
    print(f" value format: {format(zValue,'.4f')}")
    #dataProb.append(100)
    print(f"-----------------------------------------------------------------------------------------------")
    print(f"---------------------- VALORES -----------------")
    print(f" n: {dataCalc[0]}")
    print(f"miu (med. arit.): {dataCalc[1]}")
    print(f" sigma (desviac. estand.): {dataCalc[2]}")
    print(f"Porcentaje de prop. : {dataCalc[3]} %")
    print(f"(valor )")
    print(f" ")
"""


"""def probabilidad_mayor_que_x(parametros, x):

  n, media, desviacion_estandar = parametros

  # Calcula el valor z
  z = (x - media) / (desviacion_estandar / n**0.5)

  # Calcula la probabilidad usando la distribución normal estándar
  probabilidad = 1 - stats.norm.cdf(z)

  return probabilidad

# Salidas
parametros = [2000, 40.20, 43.98 ]  # n = 100, media = 40, desviacion_estandar = 2
x = 44
probabilidad = probabilidad_mayor_que_x(parametros, x)
print(f"La probabilidad de que un valor generado sea mayor que {x} es: {probabilidad:.4f}")"""

#---------------------------------------------------------------------------------------------------
"""
version beta con errores
def probX(dataCalc, prob):
    #(fuera de esto en el menu) ----> dataC = metXcalc(hours, medidasTC[xArit], medidasDV[sDesv])
    #para datacalc:
    # n = dataCalc[0]
    # miu = dataCalc[1]
    # sigma = dataCalc[2]
    #luego para este met
    #segun la probabilidad de la variable a calcular, se tomara el valor de esa prop como X 
    #es decir (por ejemplo si P(X > 44) then prob = 44)
    varToZ = ((prob - (int(dataCalc[1]))) / (dataCalc[2] / (math.sqrt(dataCalc[0]))))
    #OJO vartoZ con 4 decimales
    print(f"-----------------------------------------------------------------------------------------------")
    print(f" Resultado del calc. de probabilidad con TLC: {format(varToZ, '.4f')}")
    zValue = input('Ingrese el valor de equivalente en la tabla\n')
    #zValue se se multipl por 100 para tener el valor porcentual
    dataProb.append([(zValue*100)])
    print(f"-----------------------------------------------------------------------------------------------")
    print(f" n: {dataCalc[0]}")
    print(f"miu (med. arit.): {dataCalc[1]}")
    print(f" sigma (desviac. estand.): {dataCalc[2]}")
    print(f"Porcentaje de prop. : {dataCalc[3]} %")
    print(f" ")
"""
