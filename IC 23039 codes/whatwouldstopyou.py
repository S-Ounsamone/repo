import pandas as pd

survey = pd.read_csv('survey.csv')

numberpeople = len(survey)

#social factors
stopfamily = survey['stop_family']
stopfriends = survey['stop_friends']
stoppass = survey['stop_pass']
nfam = 0
yfam = 0
for response in stopfamily:
    if response == 2:
        nfam += 1
    if response == 1:
        yfam += 1
yesfam = yfam / numberpeople
nofam = nfam / numberpeople

yfriends = 0
nfriends = 0
for response in stopfriends:
    if response == 2:
        nfriends += 1
    if response == 1:
        yfriends += 1
yesfriends = yfriends /numberpeople
nofriends = nfriends / numberpeople

ypass = 0
npass = 0
for response in stoppass:
    if response == 2:
        npass += 1
    if response == 1:
        ypass += 1
yespass = ypass / numberpeople
nopass = npass / numberpeople
totalyes = yesfam + yesfriends + yespass
totalno = nofam + nofriends + nopass
yessocial = totalyes / 3
nosocial = totalno / 3
## percent of people influenced (and not influenced) by social factors
print("influence of social factors: ", yessocial, nosocial)
### .49 to .51 -- having a family or friend tell you to top using phone doesnt have high hold on you to stop


#regulations / outside factors
stopbluetooth = ['stop_bt']
stoptix124 = ['stop_tix124']
stoptix240 = ['stop_tix240']
rep2insu = ['stop_ins']
workpol = ['stop_work']
apprespond = ['stop_app']
blocksig = ['stop_block']

#previous incidents
crashcar = survey['stop_crash']
killed = survey['stop_kill']
ncrash = 0
ycrash = 0
for response in crashcar:
    if response == 2:
        ncrash += 1
    if response == 1:
        ycrash += 1
yescrash = ycrash/ numberpeople
nocrash = ncrash / numberpeople
ykilled = 0
nkilled = 0
for response in killed:
    if response == 1:
        ykilled += 1
    if response == 2:
        nkilled += 1
yeskilled = ykilled / numberpeople
nokilled = nkilled / numberpeople
totaly = yescrash+yeskilled
totaln = nocrash +nokilled
## percent influence of haviong previous incidents being a factor
yesprevinc = totaly / 2
noprevinc = totaln / 2
print("influence of previous incidents:", yesprevinc, noprevinc)

#won't stop
nothing = survey['stop_none']

social = survey[['stop_family', 'stop_friends', 'stop_pass']]
regulation = survey[['stop_bt', 'stop_tix124', 'stop_tix240', 'stop_ins', 'stop_work', 'stop_app', 'stop_block']]
##influence that tech has
yesblt = 0
noblt = 0
for response in regulation['stop_bt']:
    if response == 1:
        yesblt += 1
    if response == 2:
        noblt += 1
yesapp = 0
noapp = 0
for response in regulation['stop_app']:
    if response == 1:
        yesapp += 1
    if response == 2:
        noapp += 1
yesblock =0 
noblock = 0
for response in regulation['stop_block']:
    if response == 1:
        yesblock += 1
    if response == 2:
        noblock += 1
ytech = yesblt + yesapp + yesblock
ytech = ytech / 3
techworks = ytech / numberpeople
technowork = 1- techworks
print("influence of technology:", techworks, technowork)
#influence that tickets hold
yticket = 0
nticket = 0
for response in regulation['stop_tix124']:
    if response == 1:
        yticket += 2
    if response == 1:
        nticket += 1
for respinse in regulation['stop_tix240']:
    if response == 1:
        yticket += 2
    if response == 1:
        nticket += 1
yticket = yticket / 2
nticket = nticket / 2
ticketswork = yticket / numberpeople
ticketsnowork = nticket / numberpeople
print("influence of tickets:", ticketswork, ticketsnowork)

yesinsure = 0
noinsure = 0
for response in regulation['stop_ins']:
    if response == 1:
        yesinsure += 1
    else:
        noinsure += 1
insuranceworks = yesinsure / numberpeople
insurenowork = noinsure / numberpeople
print('influence of insurance:', insuranceworks, insurenowork)

import plotly.graph_objects as go
stoppers = ['social', 'technology', 'insurance', 'tickets', 'previous incidents']
Ypercents = [yessocial,techworks,insuranceworks,ticketswork,yesprevinc]
Npercents = [nosocial,technowork,insurenowork,ticketsnowork,noprevinc]
fig  = go.Figure(data=[
    go.Bar(name ='% Sait It Would Stop Them', x= stoppers, y=Ypercents),
    go.Bar(name = '% Said It Would Not Stop Them', x = stoppers, y=Npercents)
])
fig.update_layout(barmode = 'group', title='Overall Leading Factors For All Age Groups')
fig.update(layout_yaxis_range = [0,0.7])
fig.show()