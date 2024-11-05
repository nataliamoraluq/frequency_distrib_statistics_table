#prueba lectura de datos db
import csv
import matplotlib.pyplot as plt
import pandas as pd
#
# DE VARS CUANTITATIVAS
ageList = []
incomeList = []
hoursWkList = []
# VARS CUALITATIVAS
#Race,USCitizen,HealthInsurance,Language
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
    print(len(sexList))   
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
sexM = []
sexF = []
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

plt.hist([sexM, sexF], bins= bins, color={'pink','blue'})
plt.title("Grafica de la Variable Sexo")
plt.xlabel("0 = Masculino, 1 = Femenino")
plt.ylabel("Cantidad de personas")
plt.show()


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