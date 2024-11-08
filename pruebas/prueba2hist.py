
import matplotlib.pyplot as plt
import numpy as np

# Crea un arreglo con 300 valores de 1 y 200 valores de 0
#data = np.concatenate((np.ones(300), np.zeros(200)))
data1 = np.ones(300)
data2 = np.zeros(200)

print(data1)
print(data2)


# Crea el histograma con colores personalizados
plt.hist([data1, data2], edgecolor='black', color={'blue','pink'})

# Configura las etiquetas de los ejes
plt.xlabel("Valor")
plt.ylabel("Frecuencia")

# Configura el título del gráfico
plt.title("Histograma de dos barras")

# Muestra el gráfico
plt.show()

"""

import matplotlib.pyplot as plt
 
valoresA = [23,22,28,32,24,28,32,15,26,22,24,24,26,28,32,41,20,39,51,18,23,28,26,34,17]
valoresB = [23,20,30,15,10,25,30,36,20,21,20,23,34,15,14,38,34,17,38,5,34,20,21,30,10]
fig, ax = plt.subplots()
plt.hist([valoresA,valoresB], color={'pink','blue'})
plt.show()"""
