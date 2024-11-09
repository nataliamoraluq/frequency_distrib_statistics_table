#import
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
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
# --------------------------- QUALITATIVE  VARS ---------------------------------------
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

        plt.xlabel(f" Asian: {format((countA/len(raceList)) *100, '.2f')} %, Black: {format((countB/len(raceList)) *100, '.2f')} %, Other: {format((countO/len(raceList)) *100, '.2f')} %, White: {format((countW/len(raceList)) *100, '.2f')} % ")
        plt.title('Race in USA - Pie chart')
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
        mycolors = ["#90DCFF", "#FAE350"]
        plt.pie(y, labels = mylabels, explode = myexplode, colors = mycolors)
        ##
        #format(nro, '.2f')
        plt.xlabel(f" Other: {format((countO/len(languageList)) *100, '.2f')} %, English: {format((countE/len(languageList)) *100, '.2f')} %")
        plt.legend() #legenda para q muestre de nuevo los valores q se estane valuando
        plt.title('Language in the USA - Pie chart')
        plt.show()
        plt.close()
#pieChartLanguage(languageList=languageList)
#-----------------------------------------
# ------------------- BAR PLOT GENDER -------------------
#---------------------------------------------------------
def genderBar(sexList, show=True):
    countF = 0
    countM = 0
    for sex in sexList:  
        if(sex==0):countF+=1
        else:countM+=1
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

        plt.xlabel(f" Feminine: {format((countF/len(sexList)) *100, '.2f')} %,  Masculine: {format((countM/len(sexList)) *100, '.2f')} %") 
        plt.ylabel('Frequency')
        plt.title('Gender - Histogram')
        plt.show()
        plt.pause(400.01)
#

#------------------------------ CIVIL STATUS BARS ---------------------------
def marriedBar():
    df = pd.read_csv('DBdatosProyecto2024.csv') 

    sns.set_style('darkgrid', {'grid.linestyle': '--'})
    plt.hist(df['HealthInsurance'], bins=12, color="skyblue")  
    plt.xlim(0.0, 1.0) 

    
    plt.xlabel(f" Not married: 0,  Married: 1") 
    plt.ylabel('Frequency')
    plt.title('Civil status - Histogram')
    plt.show()
#
#marriedBar()
# ---------------------------- USCitizen BARS --------------------
def barsUSA():
    df = pd.read_csv('DBdatosProyecto2024.csv') 

    sns.set_style('whitegrid', {'grid.linestyle': '--'})
    plt.hist(df['USCitizen'], bins=12, color="purple")  
    plt.xlim(0.0, 1.0) 

    plt.xlabel('USCitizen - 0: Non citizen, 1:Citizen')
    plt.ylabel('Frequency')
    plt.title('USCitizen - Histogram')
    plt.show()
#

# ---------------------------- Health Insura. BARS --------------------
def healthBars():
    df = pd.read_csv('DBdatosProyecto2024.csv') 

    sns.set_style('darkgrid', {'grid.linestyle': '--'})
    plt.hist(df['HealthInsurance'], bins=12, color="skyblue")  
    plt.xlim(0.0, 1.0) 

    plt.xlabel('Health Insurance - 0: No Health Insur., 1:Have Health Insur')
    plt.ylabel('Frequency')
    plt.title('HealthInsurance - Histogram')
    plt.show()
#

# --------------------------------------- QUANTITATIVES VARS ---------------------------------------
# ---------------------------- INCOME BARS --------------------
def incomeBars():
    df = pd.read_csv('DBdatosProyecto2024.csv') 

    print(df['Income'].min())
    print(df['Income'].max())

    sns.set_style('whitegrid', {'grid.linestyle': '--'})
    plt.hist(df['Income'], bins=12, color="orange")  
    plt.xlim(0.0, 566.0) 

    plt.xlabel('Income')
    plt.ylabel('Frequency')
    plt.title('Income - Histogram')
    plt.show()
# ---------------------------- HOURS BARS --------------------
def hoursWorkBars():
    df = pd.read_csv('DBdatosProyecto2024.csv') 

    print(df['HoursWk'].min())
    print(df['HoursWk'].max())

    sns.set_style('whitegrid', {'grid.linestyle': '--'})
    plt.hist(df['HoursWk'], bins=12, color="hotpink")  
    plt.xlim(df['HoursWk'].min(), df['HoursWk'].max()) 

    plt.xlabel('Hours')
    plt.ylabel('Frequency')
    plt.title('Hours of Work - Histogram')
    plt.show()
# ---------------------------- AGE BARS --------------------
def ageBars():
    df = pd.read_csv('DBdatosProyecto2024.csv')

    print(df['Age'].min())
    print(df['Age'].max())

    sns.set_style('whitegrid', {'grid.linestyle': '--'})
    plt.hist(df['Age'], color='green') 
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Age- Histogram')
    plt.show()

