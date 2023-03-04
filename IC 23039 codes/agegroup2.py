import pandas as pd
import datetime as dt
import plotly.express as px

#keys 
#agegrp1 = 1:16-17/2:18-34/3:35-49/4:50-64/5:65+
df = pd.read_csv('survey.csv')
df = df[['agegrp1','stop_family','stop_friends','stop_pass',
         'stop_bt','stop_app','stop_block','stop_tix124','stop_tix240','stop_ins',
         'stop_work','stop_crash','stop_kill']]

#agegroup 1 : 16-17
age2 = df[df['agegrp1']==2]
numage2 = len(age2)
    ##social influence (2 = no, 1 =yes):
socialyes= 0
for response in age2['stop_family']:
    if response == 1:
        socialyes +=1
for response in age2['stop_friends']:
    if response == 1:
        socialyes += 1
for response in age2['stop_pass']:
    if response ==1:
        socialyes += 1
socialyes = socialyes / 3
age2socialyes = socialyes / numage2
age2socialno = 1-age2socialyes
print("Social influence on age group 2:",age2socialyes,age2socialno)
    ##technology influence
techyes = 0
for response in age2['stop_bt']:
    if response == 1:
        techyes += 1
for response in age2['stop_app']:
    if response == 1:
        techyes +=1
for response in age2['stop_block']:
    if response == 1:
        techyes += 1
techyes = techyes /3
age2techyes = techyes / numage2
age2techno = 1 - age2techyes
print("Technology influence on age group 2:", age2techyes, age2techno)
    ## influence of tickets
ticketyes = 0
for response in age2['stop_tix124']:
    if response == 1:
        ticketyes +=1
for response in age2['stop_tix240']:
    if response == 1:
        ticketyes += 1
ticketyes = ticketyes / 2
age2ticketyes = ticketyes / numage2
age2ticketno = 1 - age2ticketyes
print("Influence of tickets on age group 2:", age2ticketyes, age2ticketno)
    ## insurance influence
insureyes = 0
for response in age2['stop_ins']:
    if response == 1:
        insureyes += 1
age2insureyes = insureyes / numage2
age2insureno = 1 - age2insureyes
print("Influence of insure on age group 2:", age2insureyes,age2insureno)
    ## previous incidents influence
previncyes = 0
for response in age2['stop_crash']:
    if response ==1:
        previncyes += 1
for response in age2['stop_kill']:
    if response == 1:
        previncyes += 1
previousyes = previncyes / 2
age2previncyes = previousyes / numage2
age2previncno = 1- age2previncyes
print("Influence of previous incidents on age group 2:", age2previncyes, age2previncno)

import plotly.graph_objects as go
stoppers = ['social', 'technology', 'insurance', 'tickets', 'previous incidents']
age2Ypercents = [age2socialyes,age2techyes,age2insureyes,age2ticketyes,age2previncyes]
age2Npercents = [age2socialno, age2techno, age2insureno, age2ticketno, age2previncno]
fig  = go.Figure(data=[
    go.Bar(name ='% Sait It Would Stop Them', x= stoppers, y=age2Ypercents),
    go.Bar(name = '% Sait It Not Stop Them', x = stoppers, y =age2Npercents)
])
fig.update_layout(barmode = 'group', title='Age Group 2 (18-34)')
fig.update(layout_yaxis_range = [0.35,0.65])
fig.show()