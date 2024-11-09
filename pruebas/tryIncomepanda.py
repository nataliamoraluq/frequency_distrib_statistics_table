import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

