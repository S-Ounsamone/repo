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
age4 = df[df['agegrp1']==4]
numage4 = len(age4)
    ##social influence (2 = no, 1 =yes):
socialyes= 0
for response in age4['stop_family']:
    if response == 1:
        socialyes +=1
for response in age4['stop_friends']:
    if response == 1:
        socialyes += 1
for response in age4['stop_pass']:
    if response ==1:
        socialyes += 1
socialyes = socialyes / 3
age4socialyes = socialyes / numage4
age4socialno = 1-age4socialyes
print("Social influence on age group 4:",age4socialyes,age4socialno)
    ##technology influence
techyes = 0
for response in age4['stop_bt']:
    if response == 1:
        techyes += 1
for response in age4['stop_app']:
    if response == 1:
        techyes +=1
for response in age4['stop_block']:
    if response == 1:
        techyes += 1
techyes = techyes /3
age4techyes = techyes / numage4
age4techno = 1 - age4techyes
print("Technology influence on age group 4:", age4techyes, age4techno)
    ## influence of tickets
ticketyes = 0
for response in age4['stop_tix124']:
    if response == 1:
        ticketyes +=1
for response in age4['stop_tix240']:
    if response == 1:
        ticketyes += 1
ticketyes = ticketyes / 2
age4ticketyes = ticketyes / numage4
age4ticketno = 1 - age4ticketyes
print("Influence of tickets on age group 4:", age4ticketyes, age4ticketno)
    ## insurance influence
insureyes = 0
for response in age4['stop_ins']:
    if response == 1:
        insureyes += 1
age4insureyes = insureyes / numage4
age4insureno = 1 - age4insureyes
print("Influence of insure on age group 4:", age4insureyes,age4insureno)
    ## previous incidents influence
previncyes = 0
for response in age4['stop_crash']:
    if response ==1:
        previncyes += 1
for response in age4['stop_kill']:
    if response == 1:
        previncyes += 1
previousyes = previncyes / 2
age4previncyes = previousyes / numage4
age4previncno = 1- age4previncyes
print("Influence of previous incidents on age group 4:", age4previncyes, age4previncno)

import plotly.graph_objects as go
stoppers = ['social', 'technology', 'insurance', 'tickets', 'previous incidents']
age4Ypercents = [age4socialyes,age4techyes,age4insureyes,age4ticketyes,age4previncyes]
age4Npercents = [age4socialno, age4techno, age4insureno, age4ticketno, age4previncno]
fig  = go.Figure(data=[
    go.Bar(name ='% Said It Would Stop Them', x= stoppers, y=age4Ypercents),
    go.Bar(name = '% Said It Would Not Stop Them', x = stoppers, y =age4Npercents)
])
fig.update_layout(barmode = 'group', title='Age Group 4 (50-64)')
fig.update(layout_yaxis_range = [0.3,0.65])
fig.show()
