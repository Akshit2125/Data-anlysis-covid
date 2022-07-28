#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = pd.read_csv("covid_19_india.csv")
df = data.dropna(axis='columns',how='all')
global dfOg 
dfOg = df


# In[2]:


pd.set_option("display.max_rows", None, "display.max_columns", None)
df = df.drop(columns=['Sno','Time','ConfirmedIndianNational','ConfirmedForeignNational','Date'])


# In[ ]:





# In[3]:


import pandas as pd
import numpy as np

state = df['State/UnionTerritory']
sp = state.str.contains('Tel')
df['State/UnionTerritory'] = np.where(sp,'Telengana',state.str.replace('Telangana','Telengana'))

df.insert(4,'ActiveP',df['Confirmed']-df['Deaths']-df['Cured'])


# In[4]:



Andman = df[df['State/UnionTerritory']=='Andaman and Nicobar Islands'].max()
Andhrap = df[df['State/UnionTerritory']=='Andhra Pradesh'].max()
ArunachalP = df[df['State/UnionTerritory']=='Arunachal Pradesh'].max()
Assam = df[df['State/UnionTerritory']=='Assam'].max()
Bihar = df[df['State/UnionTerritory']=='Bihar'].max()
Chandigarh = df[df['State/UnionTerritory']=='Chandigarh'].max()
Chhatis = df[df['State/UnionTerritory']=='Chhattisgarh'].max()
Dadar = df[df['State/UnionTerritory']=='Dadar Nagar Haveli'].max() 
Daman = df[df['State/UnionTerritory']=='Daman & Diu'].max()
DadarDaman = df[df['State/UnionTerritory']=='Dadra and Nagar Haveli and Daman and Diu'].max()
Delhi = df[df['State/UnionTerritory']=='Delhi'].max()
Goa = df[df['State/UnionTerritory']=='Goa'].max()
Gujarat  = df[df['State/UnionTerritory']=='Gujarat'].max()
Haryana = df[df['State/UnionTerritory']=='Haryana'].max()
HP = df[df['State/UnionTerritory']=='Himachal Pradesh'].max()
Jk = df[df['State/UnionTerritory']=='Jammu and Kashmir'].max()
Jharkhand  = df[df['State/UnionTerritory']=='Jharkhand'].max()
Karnataka  = df[df['State/UnionTerritory']=='Karnataka'].max()
kerala  = df[df['State/UnionTerritory']=='Kerala'].max()
Ladakh = df[df['State/UnionTerritory']=='Ladakh'].max()
Mp = df[df['State/UnionTerritory']=='Madhya Pradesh'].max()
Maha = df[df['State/UnionTerritory']=='Maharashtra'].max()
Manipur = df[df['State/UnionTerritory']=='Manipur'].max()
Megh = df[df['State/UnionTerritory']=='Meghalaya'].max()
miz = df[df['State/UnionTerritory']=='Mizoram'].max()
Naga = df[df['State/UnionTerritory']=='Nagaland'].max()
Orrisa = df[df['State/UnionTerritory']=='Odisha'].max()
Pondi = df[df['State/UnionTerritory']=='Puducherry'].max()
punjab = df[df['State/UnionTerritory']=='Punjab'].max()
Raj = df[df['State/UnionTerritory']=='Rajasthan'].max()
sikkim = df[df['State/UnionTerritory']=='Sikkim'].max()
Tn = df[df['State/UnionTerritory']=='Tamil Nadu'].max()
Tel = df[df['State/UnionTerritory']=='Telengana'].max()
Tripura = df[df['State/UnionTerritory']=='Tripura'].max()
Up = df[df['State/UnionTerritory']=='Uttar Pradesh'].max()
Uk = df[df['State/UnionTerritory']=='Uttarakhand'].max()
Wb = df[df['State/UnionTerritory']=='West Bengal'].max()


# In[5]:


state = [Andman, Andhrap, ArunachalP, Assam, Bihar, Chandigarh , Chhatis, Dadar, Daman, DadarDaman, Delhi, Goa, Gujarat, Haryana, HP, Jk, Jharkhand, Karnataka, kerala,Maha, Ladakh, Mp, Manipur, Megh, miz, Naga, Orrisa,Pondi, punjab,Raj,sikkim, Tn, Tel,Tripura, Up, Uk,Wb]   
maxi = 0

i=1
for i in range(37):
    if ((state[i][3]-state[i][2]-state[i][1])>maxi):
        maxi = state[i][3]-state[i][2]-state[i][1]
        s = state[i][0]
        
print("%s has maximum active cases with a count of %d"%(s,maxi))

mini = 0
j=1

mini = state[0][4]

for i in range(37):
    if (state[i][4]<mini):
        mini = state[i][3]-state[i][2]-state[i][1]
        sa = state[i][0]

print("%s has minimum active cases with a count of %d"%(sa,mini))


# In[6]:


state = [Andman, Andhrap, ArunachalP, Assam, Bihar, Chandigarh , Chhatis, Dadar, Daman, DadarDaman, Delhi, Goa, Gujarat, Haryana, HP, Jk, Jharkhand, Karnataka, kerala,Maha, Ladakh, Mp, Manipur, Megh, miz, Naga, Orrisa,Pondi, punjab,Raj,sikkim, Tn, Tel,Tripura, Up, Uk,Wb]   

Death=0
Cured=0
for i in range(37):
    Death+=(state[i][2])
i=0
for i in range(37):
    Cured+=(state[i][1])



ratio = Death/Cured
print("The current death to cure ratio is %f"%(ratio))

maxStateRatio = state[0][2]/state[0][1]

for i in range(37):
    if(state[i][1]!=0):
        sr = state[i][2]/state[i][1]
        if(sr>maxStateRatio):
            maxStateRatio = sr
            sta = state[i][0]
print("%s has maximum death to cure ratio of %f"%(sta,maxStateRatio))   

minStateRatio = state[0][2]/state[0][1]

for i in range(37):
    if(state[i][1]!=0):
        src = state[i][2]/state[i][1]
        if(src<minStateRatio):
            minStateRatio = src
            stat = state[i][0]
print("%s has minimum death to cure ratio of %f"%(stat,minStateRatio))   


# In[ ]:





# In[58]:





dfUpdate = dfOg.drop(columns=['Sno','ConfirmedIndianNational','ConfirmedForeignNational','Time'])
df.reset_index()
dfUpdate = dfUpdate.set_index('State/UnionTerritory')
dfUpdate.insert(4,'Active',dfUpdate['Confirmed']-dfUpdate['Deaths']-dfUpdate['Cured'])

Delhi = dfUpdate.loc['Delhi']
Maha = dfUpdate.loc['Maharashtra']
ax = Delhi.plot(x='Date',y=['Active','Cured','Deaths'],kind = 'line',grid='True',title="Delhi")

plt.xticks(rotation=45)
plt.ylabel('No. of Patients')

Maha.plot(x='Date',y=['Active','Cured','Deaths'],kind = 'line',grid='True',title="Delhi vs Maharashtra",ax=ax)

ax.legend(['Delhi Active','Delhi Cured','Delhi Deaths','Maharashtra Active','Maharashtra Cured','Maharashtra Deaths'])
plt.xticks(rotation=45)
plt.ylabel('No. of Patients')

#  From the plot we can infer that from mid june to mid July daily active cases reports declined in Delhi while they continued to increase in Maharashtra.
# The number of deaths reported in Delhi has a minimal rise while there is a steep increase in Maharashtra
#Overall, condition wise Delhi did a much better job in handling Covid than Maharashtra which maybe due to various factors such as their size, age group of people etc.


# In[60]:


dfUpdate = dfUpdate.reset_index()
dfUpdate = dfUpdate.set_index('Date')

dfUpdate = dfUpdate.loc['28/07/20']
dfUpdate = dfUpdate.reset_index()
dfUpdate = dfUpdate.set_index('State/UnionTerritory')


# In[138]:


import matplotlib.pyplot as plt
Delhi = dfUpdate.loc['Delhi']
cured = Delhi['Cured']
active = Delhi['Active']
dead= Delhi['Deaths'] 
explode = (0.1,0.1,0.1)
labels = "Cured","Deaths","Active"
numbers = cured, active, dead
fig1, ax1 = plt.subplots(figsize=(5, 5))

ax1.pie(numbers,explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.set_title("Delhi as of 28/07/20")

Maha = dfUpdate.loc['Maharashtra']
cured1 = Maha['Cured']
active1 = Maha['Active']
dead1= Maha['Deaths'] 
labels = "Cured","Deaths","Active"
numbers = cured1, active1, dead1
fig2, ax2 = plt.subplots(figsize=(5, 5))

ax2.pie(numbers,explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=90)
ax2.set_title("Maharashtra as of 28/07/20")


# While in Delhi close to 89% of the patients have been cured, the condition remains critical in Maharastra as approximately only 58% of the cases were cured
#Death percentage in both states also portray a large difference implying the fatality rate is much in Maharashtra, again due to various factors

