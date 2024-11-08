"""#prueba lectura de datos db
import csv
import matplotlib.pyplot as plt
import pandas as pd
from repository import Graphics
import seaborn as sns

with open("DBdatosProyecto2024.csv", newline='') as csvFile:
        spamreader = csv.reader(csvFile, delimiter=' ', quotechar=' ')
        
        data = sns.load_dataset('spamreader')

        data.head()"""

import matplotlib.pyplot as plt
import numpy as np
import csv
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
readDB()

#-----------------------------------------
# ------------------- PIE CHART RACE -------------------
def pieChartRace(raceList):
        #count each race
        countA=0
        countB=0
        countO=0
        countW=0
        for rac in raceList:  
            #on the (race) List done
            #asian,black,other,white
            if(rac=='asian'):countA+=1
            elif(rac=='black'):countB+=1
            elif(rac=='other'):countO+=1
            elif(rac=='white'):countW+=1
            else: print("error! in reading the race")
        #definimos el grafico de pastel; y tendra los valores
        #a evaluar y comparar, labels el nombre de los "intervalos" a evaluar con los valores
        #y todo lo demas ya es estetica; espacios, colores
        y = np.array([countA, countB, countO, countW])
        mylabels = ["Asian", "Black", "Other", "White"]
        myexplode = [0.025, 0.025, 0.025, 0.05]
        #fae350 pretty purple: #A39ED1
        mycolors = ["blue", "#6CDA63", "hotpink","#FAE350"]
        #plt.pie para crear el pie con todos los elementos previamente definidos
        plt.pie(y, labels = mylabels, explode = myexplode, colors = mycolors)
        ##
        #print(f"asian:{countA}")
        """format((countA/len(raceList)) *100, '.2f')
        format((countB/len(raceList)) *100, '.2f')
        format((countO/len(raceList)) *100, '.2f')
        format((countW/len(raceList)) *100, '.2f')"""

        plt.xlabel(f" Asian: {format((countA/len(raceList)) *100, '.2f')} %, Black: {format((countB/len(raceList)) *100, '.2f')} %, Other: {format((countO/len(raceList)) *100, '.2f')} %, White: {format((countW/len(raceList)) *100, '.2f')} % ")
        plt.legend() #legenda para q muestre de nuevo los valores q se estane valuando
        plt.show()
#pieChartRace(raceList=raceList)

#-----------------------------------------
# ------------------- PIE CHART LANGUAGE -------------------

def pieChartLanguage(languageList):
        #count each language
        countO=0
        countE=0
        for lag in languageList:  
            if(lag==0):countO+=1
            elif(lag==1):countE+=1
            else: print("error! in reading the language")
        y = np.array([countO, countE])
        mylabels = ["Other language spoken at home", "English spoken at home"]
        myexplode = [0.025, 0.025]
        #fae350 pretty purple: #A39ED1
        mycolors = ["#A39ED1", "#FAE350"]
        plt.pie(y, labels = mylabels, explode = myexplode, colors = mycolors)
        ##
        plt.xlabel(f" Other: {format((countO/len(languageList)) *100, '.2f')} %, English: {format((countE/len(languageList)) *100, '.2f')} %")
        plt.legend() #legenda para q muestre de nuevo los valores q se estane valuando
        plt.show()
pieChartLanguage(languageList=languageList)

"""
def pieChartGender(sexList):
        #count each race
        countF = 0
        countM = 0
        for sex in sexList:  
            if(sex==0):countF+=1
            else:countM+=1
            #print(countF, "x" ,countM)
        #definimos el grafico de pastel; y tendra los valores
        #a evaluar y comparar, labels el nombre de los "intervalos" a evaluar con los valores
        #y todo lo demas ya es estetica; espacios, colores
        y = np.array([countF, countM])
        mylabels = ["Female", "Male"]
        myexplode = [0.05, 0.05]
        #fae350 pretty purple: #A39ED1
        mycolors = ["hotpink", "blue"]
        #plt.pie para crear el pie con todos los elementos previamente definidos
        plt.pie(y, labels = mylabels, explode = myexplode, colors = mycolors)
        plt.legend() #legenda para q muestre de nuevo los valores q se estane valuando
        plt.show()
pieChartGender(sexList=sexList)"""