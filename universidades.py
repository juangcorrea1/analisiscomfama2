#1. importo a pandas
import pandas as pd

#2. traigo la fuentes de datos
edadescasa1=[25,25,25,25,25]

edadescasa2=[1,4,24,26,70]

#3. genero ls dataframes
dataframe1=pd.DataFrame(edadescasa1)
dataframe2=pd.DataFrame(edadescasa2)

#4. analisis descriptivo de los datos
analisis1=dataframe1.describe()
analisis2=dataframe2.describe()

#5. imprimir 
print(analisis1)
print(analisis2)
