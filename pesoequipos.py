import pandas as pd

nacional=[84,88,84,87,80,83,84,90,78,82,84,90,75,78,98,100,78,65,80,20]

medellin=[90,78,68,87,102,90,80,80,81,78,79,81,83,84.5,90,101,60,70,80,87]

dataframe1=pd.DataFrame(nacional)
dataframe2=pd.DataFrame(medellin)

analisis1=dataframe1.describe()
analisis2=dataframe2.describe()

print(analisis1)
print(analisis2)