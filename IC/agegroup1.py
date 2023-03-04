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
age1 = df[df['agegrp1']==1]
numage1 = len(age1)
    ##social influence (2 = no, 1 =yes):
socialyes= 0
for response in age1['stop_family']:
    if response == 1:
        socialyes +=1
for response in age1['stop_friends']:
    if response == 1:
        socialyes += 1
for response in age1['stop_pass']:
    if response ==1:
        socialyes += 1
socialyes = socialyes / 3
age1socialyes = socialyes / numage1
age1socialno = 1-age1socialyes
print("Social influence on age group 1:",age1socialyes,age1socialno)
    ##technology influence
techyes = 0
for response in age1['stop_bt']:
    if response == 1:
        techyes += 1
for response in age1['stop_app']:
    if response == 1:
        techyes +=1
for response in age1['stop_block']:
    if response == 1:
        techyes += 1
techyes = techyes /3
age1techyes = techyes / numage1
age1techno = 1 - age1techyes
print("Technology influence on age group 1:", age1techyes, age1techno)
    ## influence of tickets
ticketyes = 0
for response in age1['stop_tix124']:
    if response == 1:
        ticketyes +=1
for response in age1['stop_tix240']:
    if response == 1:
        ticketyes += 1
ticketyes = ticketyes / 2
age1ticketyes = ticketyes / numage1
age1ticketno = 1 - age1ticketyes
print("Influence of tickets on age group 1:", age1ticketyes, age1ticketno)
    ## insurance influence
insureyes = 0
for response in age1['stop_ins']:
    if response == 1:
        insureyes += 1
age1insureyes = insureyes / numage1
age1insureno = 1 - age1insureyes
print("Influence of insure on age group 1:", age1insureyes,age1insureno)
    ## previous incidents influence
previncyes = 0
for response in age1['stop_crash']:
    if response ==1:
        previncyes += 1
for response in age1['stop_kill']:
    if response == 1:
        previncyes += 1
previousyes = previncyes / 2
age1previncyes = previousyes / numage1
age1previncno = 1- age1previncyes
print("Influence of previous incidents on age group 1:", age1previncyes, age1previncno)

import plotly.graph_objects as go
stoppers = ['social', 'technology', 'insurance', 'tickets', 'previous incidents']
age1Ypercents = [age1socialyes,age1techyes,age1insureyes,age1ticketyes,age1previncyes]
age1Npercents = [age1socialno, age1techno, age1insureno, age1ticketno, age1previncno]
fig  = go.Figure(data=[
    go.Bar(name ='% Said It Would Stop Them', x= stoppers, y=age1Ypercents),
    go.Bar(name = '% Said It Would Not Stop Them', x = stoppers, y =age1Npercents)
])
fig.update_layout(barmode = 'group', title='Age Group 1 (16-17)')
fig.update(layout_yaxis_range = [0.2,0.7])
fig.show()