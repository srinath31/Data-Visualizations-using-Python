'''
@author: srinath.ramachandran

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('matches.csv')
countbatfirst=[]
countbatsecond=[]
iplyears=[]
width = 0.35
stat=["Team Batting First","Team Batting Second"]
iplyear=2008

#Function to calculate the number of matches won by batting first and second.
def matchcount(df,iplyear,countbatfirst,countbatsecond,iplyears):
    count=0
    counttie=0
    cbf=0
    cbs=0
    for row in df.iterrows():
        if row[1][1]==iplyear:
            count=count+1
            if row[1][8]=="tie":
                counttie=counttie+1
            elif row[1][8]=="normal":
                if row[1][11]!=0:
                    cbf=cbf+1
                elif row[1][12]!=0:
                    cbs=cbs+1
    countbatfirst.append(cbf)
    countbatsecond.append(cbs)
    iplyears.append(iplyear)
    iplyear=iplyear+1
    if iplyear==2018:
        return
    else:
        matchcount(df,iplyear,countbatfirst,countbatsecond,iplyears)

matchcount(df,iplyear,countbatfirst,countbatsecond,iplyears)        
    
position=np.arange(10)
p1=plt.bar(position,countbatfirst,width,color='#ffcc00')
p2=plt.bar(position+width,countbatsecond,width,color='#e63900')
plt.yticks(np.arange(0, 81, 10),color='#800000',fontweight='bold')
plt.xticks(position+width/2,iplyears,color='#800000',fontweight='bold')
plt.xlabel("Years",size=12,color='#e63900',fontweight='bold')
plt.ylabel("Number of Matches Won",color='#e63900',fontweight='bold',size=12)
plt.title("IPL STATS OVER THE YEARS",fontweight='bold',size=14)
plt.legend(stat,loc=2)
plt.show()       