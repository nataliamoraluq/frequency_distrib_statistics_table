import pandas as pd
import seaborn as sns
import numpy as np
 
# read the dataset using pandas read_csv 
# function
data = pd.read_csv(r"path to .\"DBdatosProyecto2024.csv")
 
data.head()
 
# create a bar plot by specifying
# x and y axis and the data to be used.
ax = sns.barplot(x='sex', y='race',
                 hue='sex', data=data,
                 errwidth=0)
 
# sns.barplot method will return a list of 
# sub methods use containers method to access 
# the text label of each bar by passing it 
# through the ax.bar_label function use for
# loop to iterate through the list of
# labels and assign each bar to a different 
# label.
for i in ax.containers:
    ax.bar_label(i,)