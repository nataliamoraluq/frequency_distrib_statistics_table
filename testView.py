#vista data frama con panda
#no workin, no idea
import pandas as pd
# Columnas: features
data_0 = {'sexo': ['Masculino','Femenino','Otro'], 'codigo': [0,1,2], 'frecuencia': [5,6,2]}
pd_0 = pd.DataFrame(data=data_0)
pd_0

#para la curtosis - o algo asi; se define la fila y la columna q mostrara
#vista dataframe con matplotlib

"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
dias = ["L","M","M","J","V","S","D"]
temperaturas = {'BsAs': [28.5,30.5,31,30,28,27.5,30.5],'SantiagoDelEstero': [35,36,38,49,47,42,31]}
ax.plot(dias,temperaturas['BsAs'],color='tab:purple', label='Buenos Aires', marker="^")
ax.plot(dias,temperaturas['SantiagoDelEstero'],color='tab:green', marker='*',label='SantiagoDelEstero')

plt.show()"""