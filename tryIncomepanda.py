import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DBdatosProyecto2024.csv') 

#print(df.min())
print(df.max())

plt.hist(df['Income'], bins=12)  
plt.xlim(0.0, 566.0) 

plt.xlabel('Income')
plt.ylabel('Frequency')
plt.title('Histogram of Income')
plt.show()

