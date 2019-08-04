# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
# %matplotlib inline
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names, births))
# print(BabyDataSet)
#
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
# print(df.tail(3))
#
df.to_csv('births1880.csv',index=True, header=False)

Location = r'C:\Users\test\PycharmProjects\sonu\pandas\births1880.csv'
df = pd.read_csv(Location, names=['Names','Births'])
print(df.dtypes)

Sorted = df.sort_values(['Births'], ascending=False)
print(Sorted.head(1))
print(df['Births'].max())
print(df['Births'].plot())
# Create graph
df['Births'].plot()

# Maximum value in the data set
MaxValue = df['Births'].max()

# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0),
                 xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular name")
print([df['Births'] == df['Births'].max()])
#Sorted.head(1) can also be used