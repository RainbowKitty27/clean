import csv 
import pandas as pd
df=pd.read_csv("merge.csv")

del df["Luminosity"]
del df["Mass"]
del df["Radius"]
del df["Distance"]
del df["Star_name"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]

df = df.rename({
            }, axis='columns')
df.to_csv("final.csv")