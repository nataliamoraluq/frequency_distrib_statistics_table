#prueba lectura de datos db
import csv
import matplotlib.pyplot as plt
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
plt.hist(ageList)
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