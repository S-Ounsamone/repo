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
age3 = df[df['agegrp1']==3]
numage3 = len(age3)
    ##social influence (2 = no, 1 =yes):
socialyes= 0
for response in age3['stop_family']:
    if response == 1:
        socialyes +=1
for response in age3['stop_friends']:
    if response == 1:
        socialyes += 1
for response in age3['stop_pass']:
    if response ==1:
        socialyes += 1
socialyes = socialyes / 3
age3socialyes = socialyes / numage3
age3socialno = 1-age3socialyes
print("Social influence on age group 3:",age3socialyes,age3socialno)
    ##technology influence
techyes = 0
for response in age3['stop_bt']:
    if response == 1:
        techyes += 1
for response in age3['stop_app']:
    if response == 1:
        techyes +=1
for response in age3['stop_block']:
    if response == 1:
        techyes += 1
techyes = techyes /3
age3techyes = techyes / numage3
age3techno = 1 - age3techyes
print("Technology influence on age group 3:", age3techyes, age3techno)
    ## influence of tickets
ticketyes = 0
for response in age3['stop_tix124']:
    if response == 1:
        ticketyes +=1
for response in age3['stop_tix240']:
    if response == 1:
        ticketyes += 1
ticketyes = ticketyes / 2
age3ticketyes = ticketyes / numage3
age3ticketno = 1 - age3ticketyes
print("Influence of tickets on age group 3:", age3ticketyes, age3ticketno)
    ## insurance influence
insureyes = 0
for response in age3['stop_ins']:
    if response == 1:
        insureyes += 1
age3insureyes = insureyes / numage3
age3insureno = 1 - age3insureyes
print("Influence of insure on age group 3:", age3insureyes,age3insureno)
    ## previous incidents influence
previncyes = 0
for response in age3['stop_crash']:
    if response ==1:
        previncyes += 1
for response in age3['stop_kill']:
    if response == 1:
        previncyes += 1
previousyes = previncyes / 2
age3previncyes = previousyes / numage3
age3previncno = 1- age3previncyes
print("Influence of previous incidents on age group 3:", age3previncyes, age3previncno)

import plotly.graph_objects as go
stoppers = ['social', 'technology', 'insurance', 'tickets', 'previous incidents']
age3Ypercents = [age3socialyes,age3techyes,age3insureyes,age3ticketyes,age3previncyes]
age3Npercents = [age3socialno, age3techno, age3insureno, age3ticketno, age3previncno]
fig  = go.Figure(data=[
    go.Bar(name ='% Sait It Would Stop Them', x= stoppers, y=age3Ypercents),
    go.Bar(name = '% Said It Would Not Stop Them', x = stoppers, y =age3Npercents)
])
fig.update_layout(barmode = 'group', title='Age Group 3 (35-49)')
fig.update(layout_yaxis_range = [0.35,0.65])
fig.show()