import csv
import pandas as pd

df=pd.read_csv("final_data.csv")

Star_Name = []
Distance = []
Mass = []
Radius = []

for index,x in enumerate(df["Distance"]):
    if(float(x.replace(",",""))<=100):
        Star_Name.append(df["Star_name"][index])
        Distance.append(df["Distance"][index])
        Mass.append(df["Mass"][index])
        Radius.append(df["Radius"][index])



with open("final_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(["Star_name","Distance","Mass","Radius"])
    for index,x in enumerate(Star_Name):
        csvwriter.writerow([Star_Name[index],Distance[index],Mass[index],Radius[index]])