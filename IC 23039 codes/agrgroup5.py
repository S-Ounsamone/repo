import pandas as pd
import datetime as dt
import plotly.express as px

#keys 
#agegrp1 = 1:16-17/2:18-34/3:35-49/4:50-64/5:65+
df = pd.read_csv('survey.csv')
df = df[['agegrp1','stop_family','stop_friends','stop_pass',
         'stop_bt','stop_app','stop_block','stop_tix124','stop_tix240','stop_ins',
         'stop_work','stop_crash','stop_kill','stop_none']]

#agegroup 1 : 16-17
age5 = df[df['agegrp1']==5]
numage5 = len(age5)
    ##social influence (2 = no, 1 =yes):
socialyes= 0
for response in age5['stop_family']:
    if response == 1:
        socialyes +=1
for response in age5['stop_friends']:
    if response == 1:
        socialyes += 1
for response in age5['stop_pass']:
    if response ==1:
        socialyes += 1
socialyes = socialyes / 3
age5socialyes = socialyes / numage5
age5socialno = 1-age5socialyes
print("Social influence on age group 5:",age5socialyes,age5socialno)
    ##technology influence
techyes = 0
for response in age5['stop_bt']:
    if response == 1:
        techyes += 1
for response in age5['stop_app']:
    if response == 1:
        techyes +=1
for response in age5['stop_block']:
    if response == 1:
        techyes += 1
techyes = techyes /3
age5techyes = techyes / numage5
age5techno = 1 - age5techyes
print("Technology influence on age group 5:", age5techyes, age5techno)
    ## influence of tickets
ticketyes = 0
for response in age5['stop_tix124']:
    if response == 1:
        ticketyes +=1
for response in age5['stop_tix240']:
    if response == 1:
        ticketyes += 1
ticketyes = ticketyes / 2
age5ticketyes = ticketyes / numage5
age5ticketno = 1 - age5ticketyes
print("Influence of tickets on age group 5:", age5ticketyes, age5ticketno)
    ## insurance influence
insureyes = 0
for response in age5['stop_ins']:
    if response == 1:
        insureyes += 1
age5insureyes = insureyes / numage5
age5insureno = 1 - age5insureyes
print("Influence of insure on age group 5:", age5insureyes,age5insureno)
    ## previous incidents influence
previncyes = 0
for response in age5['stop_crash']:
    if response ==1:
        previncyes += 1
for response in age5['stop_kill']:
    if response == 1:
        previncyes += 1
previousyes = previncyes / 2
age5previncyes = previousyes / numage5
age5previncno = 1- age5previncyes
print("Influence of previous incidents on age group 5:", age5previncyes, age5previncno)


import plotly.graph_objects as go
stoppers = ['social', 'technology', 'insurance', 'tickets', 'previous incidents']
age5Ypercents = [age5socialyes,age5techyes,age5insureyes,age5ticketyes,age5previncyes]
age5Npercents = [age5socialno, age5techno, age5insureno, age5ticketno, age5previncno]
fig  = go.Figure(data=[
    go.Bar(name ='% Said It Would Stop Them', x= stoppers, y=age5Ypercents),
    go.Bar(name = '% Said It Would Not Stop Them', x = stoppers, y =age5Npercents)
])
fig.update_layout(barmode = 'group', title='Age Group 5 (65+)')
fig.update(layout_yaxis_range = [0.1,0.8])
fig.show()