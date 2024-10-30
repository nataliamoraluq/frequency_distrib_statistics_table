#prueba lectura de datos db
import csv
import matplotlib.pyplot as plt
#
valores = []
edad = []
salarioW = []
horasW = []
#
def readDB():
    with open("DBdatosProyecto2024.csv", newline='') as csvFile:
        spamreader = csv.reader(csvFile, delimiter=' ', quotechar=' ')
        i = 0
        for row in spamreader:
            if i > 0:
                data = row[0].split(',')
                valores.append(data[1])
                edad.append(data[2])
                salarioW.append(data[4])
                horasW.append(data[5])
            i += 1
#
"""
plt.hist(valores)
print(valores)
plt.show()
"""
readDB()
plt.hist(edad)
print(edad)
plt.show()