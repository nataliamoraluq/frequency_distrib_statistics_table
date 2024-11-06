import csv
import matplotlib.pyplot as plt
from pprint import pprint
from matplotlib import cm, colormaps
import random
#-------------------------------------------------------
class Graphics:

    #------------------------------------------------------
    def __init__(self, ageList, incomeList, hoursWkList, sexList, marriedList, raceList, citizenUSList, healthInsuranceList, languageList):
        #all read vazrs from DB list 
        self.age = ageList
        self.income = incomeList
        self.hours = hoursWkList
        self.gender = sexList
        self.civilStat = marriedList
        self.race = raceList
        self.citizen = citizenUSList
        self.healthIn = healthInsuranceList
        self.language = languageList
        #qualitative vars
        self.ageL = []
        self.incomeL = []
        self.hoursL = []
        #quantitative vars
        #sex
        self.sexM = []
        self.sexF = []
        self.countF=0 
        self.countM=0
        #race
        self.asianR = []
        self.blackR = []
        self.otherR = []
        self.whiteR = []
        self.countA=0 
        self.countB=0
        self.countO=0 
        self.countW=0
        #

    def graphicGender(self):
        """for sex in self.gender:  
            if(sex==0):
                self.countF+=1
                self.sexF.append(self.gender[sex])
            else:
                self.countM+=1
                self.sexM.append(self.gender[sex])
            #print(self.countF, "x" ,self.countM)
        # bins; to define the range of the "intervals" of the value to compare
        bins = [-0.1, 0,1.1]
        #
        plt.hist([self.sexM, self.sexF], bins= bins, color={'pink','blue'})
        plt.title("Grafica de la Variable Sexo")
        plt.xlabel("0 = Masculino, 1 = Femenino")
        plt.ylabel("Cantidad de personas")
        plt.show()"""
        plt.hist(self.gender)
        plt.xlabel("0 = Masculino, 1 = Femenino")
        plt.ylabel("Cantidad de personas")
        plt.show()

    def graphicRace(self):
        # pprint(self.race)
        for rac in self.race:  
            #asian,black,other,white
            if(rac=='asian'):
                self.countA+=1
                #self.asianR.append(self.gender[rac])
            elif(rac=='black'):
                self.countB+=1
                #self.blackR.append(self.gender[rac])
            elif(rac=='other'):
                self.countO+=1
                #self.otherR.append(self.gender[rac])
            elif(rac=='white'):
                self.countW+=1
                #self.whiteR.append(self.gender[rac])
            else:
               print("error! in reading the race")
            #print(self.countF, "x" ,self.countM)
        self.asianR.append(self.countA)
        self.blackR.append(self.countB)
        self.otherR.append(self.countO)
        self.whiteR.append(self.countW)

        print(f"Asian: {self.asianR}")
        print(f"Black: {self.blackR}")
        print(f"Other: {self.otherR}")
        print(f"White: {self.whiteR}")
        # bins; to define the range of the "intervals" of the value to compare
        #
        """plt.hist([self.asianR, self.blackR, self.otherR, self.whiteR], 
                 bins= bins, color={'gray','orange', 'cyan', 'blue'})"""
        paleta = random.choice(list(colormaps))
        pprint(paleta)
        paletero = plt.get_cmap(paleta)
        pprint(paletero)
        # C = [paleta(((x-X.min())/x_span)) for x in X]
        # plot_color_gradients('Sequential (2)',
        #              ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
        #               'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
        #               'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper'])
        #color=paletero.
        plt.hist(self.race)
        

        plt.title("Grafica de la Variable Raza")
        plt.xlabel("Asian, Black, Other, White")
        plt.ylabel("Cantidad de personas")
        plt.show()
#-------------------------------------------------------
"""
graphics = Graphics()
graphics.graphicGender()
graphics.graphicRace()
""" 
#-------------------------------------------------------

