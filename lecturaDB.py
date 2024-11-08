#prueba lectura de datos db
import csv
import matplotlib.pyplot as plt
import pandas as pd
from repository import Graphics
import seaborn as sns
#
# DE VARS CUANTITATIVAS
ageList = []
incomeList = []
hoursWkList = []
# VARS CUALITATIVAS
sexList = []
marriedList = []
raceList = []
citizenUSList = []
healthInsuranceList = []
languageList = []
#
def readDB():
    with open("DBdatosProyecto2024.csv", newline='') as csvFile:
        spamreader = csv.reader(csvFile, delimiter=' ', quotechar=' ')
        i = 0
        for row in spamreader:
            if i > 0:
                data = row[0].split(',')
                sexList.append(int(data[0]))
                ageList.append(int(data[1]))
                marriedList.append(data[2])
                incomeList.append(float(data[3]))
                hoursWkList.append(float(data[4]))
                raceList.append(data[5])
                citizenUSList.append(int(data[6]))
                healthInsuranceList.append(int(data[7]))
                languageList.append(int(data[8]))
            i += 1
    #print(len(sexList))   
    #print(min(ageList))  
    """
    print(sexList)
    print(ageList)
    print(marriedList)
    print(incomeList)
    print(hoursWkList)
    print(raceList)
    print(citizenUSList)
    print(healthInsuranceList)
    print(languageList)"""
#
readDB()
"""
graficos = Graphics(ageList, incomeList, hoursWkList, sexList, marriedList, raceList, citizenUSList, healthInsuranceList, languageList)
#graficos.graphicGender()
graficos.graphicRace()"""
#------------------------------------------------------
sexM = []
sexF = []
global countF, countM
def graphicGender():
    countF = 0
    countM = 0
    for sex in sexList:  
        if(sex==0):
            countF+=1
            sexF.append(sexList[sex])
        else:
            countM+=1
            sexM.append(sexList[sex])
        print(countF, "x" ,countM)
    bins = [-0.1, 0,1.1]
    colors = ['#f19f3c', '#de3cf1']
    plt.hist([sexM, sexF], bins= bins, color=colors)
    plt.title("Grafica de la Variable Sexo")
    plt.xlabel("0 = Masculino, 1 = Femenino")
    plt.ylabel("Cantidad de personas")
    plt.show()



def graphicGender2():
    countF = 0
    countM = 0
    for sex in sexList:  
        if(sex==0):
            countF+=1
            sexF.append(sexList[sex])
        else:
            countM+=1
            sexM.append(sexList[sex])
        print(countF, "x" ,countM)
    bins = [-0.1, 0,1.1]
    colors = ['#f19f3c', '#de3cf1']
    """
    cm = plt.get_cmap('turbo')

    patches = plt.hist(sexList)

    for j, p in enumerate(patches):
        print(f'setting color on bar {j} ')
        p.set_facecolor(cm(j / len(patches)))"""

    etiquetas = ['M', 'F']
    listx = []
    listx.append(countM)
    listx.append(countF)

    print(listx)

    #plt.bar(etiquetas, listx)
    #plt.show()
    plt.figure()
    ax = sns.barplot(y=etiquetas, x=listx)
    #plt.bar(etiquetas, listx)
    #sns.barplot(etiquetas, listx)
    #plt.bar(etiquetas, raceList)
    
    #plt.show()
#---------------------------------------------------------
def show_barplot(show=True):
    countF = 0
    countM = 0
    for sex in sexList:  
        if(sex==0):
            countF+=1
            sexF.append(sexList[sex])
        else:
            countM+=1
            sexM.append(sexList[sex])
        print(countF, "x" ,countM)
    #
    etiquetas = ['F','M']
    listx = []
    listx.append(countF)
    listx.append(countM)
    #
    y = etiquetas
    x = listx
    #
    sns.set_style('whitegrid', {'grid.linestyle': '--'})
    ax = sns.barplot(y=x, x=y, palette = "husl", edgecolor = "black")
    
    if show:
        plt.xlabel(f"| 1 = Femenino --- {countF}  || 0 = Masculino --- {countM} |")
        plt.show(block=False)
        plt.pause(400.01)

#graphicGender2()

show_barplot()

#-------------------------------------------------------
#graphicGender()
#-------------------------------------------------------
"""
plt.hist(valores)
print(valores)
plt.show()
"""
"""
readDB()
plt.hist(edad)
print(edad)
plt.show()
"""