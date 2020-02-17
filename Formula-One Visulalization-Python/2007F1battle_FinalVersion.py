# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 11:52:56 2018

@author: srinath.ramachandran
"""
#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
racename=[]
hamilton=[]
hamiltonpt=[]
alonso=[]
alonsopt=[]
raikkonen=[]
raikkonenpt=[]
raceid=[]
newname=[]

resultdf = pd.read_csv('results.csv')
racesdf=pd.read_csv('races.csv')
for i in range(len(racesdf)):
    if racesdf.iloc[i][1]==2007:
        racename.append((racesdf.iloc[i][4]))
        raceid.append(racesdf.iloc[i][0])

#CALCULATION OF ALL THE THREE DRIVERS' POINTS AFTER EVERY RACE
for i in range(len(resultdf)):
    if raceid.__contains__(resultdf.iloc[i][1]):
        if resultdf.iloc[i][2]==1:
            hamilton.append(resultdf.iloc[i][9]) 
        elif resultdf.iloc[i][2]==4:
            alonso.append(resultdf.iloc[i][9])
        elif resultdf.iloc[i][2]==8:
            raikkonen.append(resultdf.iloc[i][9])
hamiltonpt=np.cumsum(hamilton)
alonsopt=np.cumsum(alonso)
raikkonenpt=np.cumsum(raikkonen)

for race in racename:
    tempname=str.replace(race,"Grand Prix","GP")
    newname.append(tempname)

#PLOTTING OF THE GRAPH
a4_dims = (18, 18)
f, ax = plt.subplots(figsize=a4_dims)
df1=pd.DataFrame({"GRAND PRIXS":newname,"CHAMPIONSHIP POINTS":hamiltonpt,"2007 Contenders":"Lewis Hamilton"})
df2=pd.DataFrame({"GRAND PRIXS":newname,"CHAMPIONSHIP POINTS":alonsopt,"2007 Contenders":"Fernando Alonso"})
df3=pd.DataFrame({"GRAND PRIXS":newname,"CHAMPIONSHIP POINTS":raikkonenpt,"2007 Contenders":"Kimi Raikkonen"})
df = pd.concat([df1,df2,df3])
print(df.head())
g=sns.pointplot(ax=ax,x=df['GRAND PRIXS'],y=df['CHAMPIONSHIP POINTS'],data=df,hue='2007 Contenders',palette={"Lewis Hamilton":"#0000FF","Fernando Alonso":"#00FF00","Kimi Raikkonen":"#FF0000"},markers=["^", "o","*"])              
ax.xaxis.label.set_size(25)
ax.yaxis.label.set_size(25)
plt.xticks(rotation=90,fontweight='bold',color='#6C3483',fontsize=14)
plt.yticks(np.arange(0,120,5),fontname="Arial", fontsize=16,fontweight='bold',color='#4A235A')
plt.title("THREEWAY BATTLE FOR 2007 FIA FORMULA ONE DRIVER'S CHAMPIONSHIP",fontsize=24,fontweight='bold',color='red')
plt.show()
#%%