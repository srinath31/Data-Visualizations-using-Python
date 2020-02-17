"""
Created on Wed Mar 14 11:31:23 2018

@author: srinath.ramachandran
"""

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
print(resultdf)
racesdf=pd.read_csv('races.csv')
for i in range(len(racesdf)):
    if racesdf.iloc[i][1]==2007:
        racename.append((racesdf.iloc[i][4]))
        raceid.append(racesdf.iloc[i][0])
print(racename)
print(raceid)

#CALCULATION OF HAMILTON'S POINTS AFTER EVERY RACE
for i in range(len(resultdf)):
    if raceid.__contains__(resultdf.iloc[i][1]):
        if resultdf.iloc[i][2]==1:
            hamilton.append(resultdf.iloc[i][9])      
sum=0
for point in hamilton:
    sum=sum+point
    hamiltonpt.append(sum)
print(hamiltonpt) 

#CALCULATION OF ALONSO'S POINTS AFTER EVERY RACE
for i in range(len(resultdf)):
    if raceid.__contains__(resultdf.iloc[i][1]):
        if resultdf.iloc[i][2]==4:
            alonso.append(resultdf.iloc[i][9])
sum=0
for point in alonso:
    sum=sum+point
    alonsopt.append(sum)
print(alonsopt)

#CALCULATION OF RAIKKONEN'S POINTS AFTER EVERY RACE
for i in range(len(resultdf)):
    if raceid.__contains__(resultdf.iloc[i][1]):
        if resultdf.iloc[i][2]==8:
            raikkonen.append(resultdf.iloc[i][9])
sum=0
for point in raikkonen:
    sum=sum+point
    raikkonenpt.append(sum)
print(raikkonenpt)


for race in racename:
    tempname=str.replace(race,"Grand Prix","GP")
    newname.append(tempname)
print(newname)


#GRAPH PLOTTING
f, ax = plt.subplots(1, 1)
a=np.array(hamiltonpt)
b=np.array(alonsopt)
c=np.array(raikkonenpt)
df1=pd.DataFrame({"Races":newname,"Cumulative Points":a})
df2=pd.DataFrame({"Races":newname,"Cumulative Points":b})
df3=pd.DataFrame({"Races":newname,"Cumulative Points":c})

df1['2007 Contenders'] = 'Lewis Hamilton'
df2['2007 Contenders'] = 'Fernando Alonso'
df3['2007 Contenders'] = 'Kimi Raikkonen'

df = pd.concat([df1,df2,df3])
print(df.head())
sns.pointplot(ax=ax,x=df['Races'],y=df['Cumulative Points'],data=df,hue='2007 Contenders')
plt.xticks(rotation=90)
plt.yticks(np.arange(0,120,10))
plt.show()


#%%
