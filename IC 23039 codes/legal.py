import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime as dt

#keys #agegrp1 = 1:16-17/2:18-34/3:35-49/4:50-64/5:65+

df = pd.read_csv('survey.csv')

def Average(lst):
    return sum(lst) / len(lst)


yrlist = [2018,2019,2021,2022]

dflist = []

age1 = df[df['agegrp1'] == 1]
age2 = df[df['agegrp1'] == 2]
age3 = df[df['agegrp1'] == 3]
age4 = df[df['agegrp1'] == 4]
age5 = df[df['agegrp1'] == 5]

dflist.append(age1)

dflist.append(age2)

dflist.append(age3)

dflist.append(age4)

dflist.append(age5)

frames = {}
groups = [1,2,3,4,5]


for grp in groups:   
    frames[grp] = df[df['agegrp1'] == grp] # assigning data frame from list to key in dictionary
    
frames['16-17'] = frames[1]
frames['18-34'] = frames[2]
frames['35-49'] = frames[3]
frames['50-64'] = frames[4]
frames['65+'] = frames[5]

del frames[1]
del frames[2]
del frames[3]
del frames[4]
del frames[5]

headers = ['Age Group','Year','Score']

agelist = []
yearlist = []
scoreslist = []


for key,df in frames.items():
    for yr in yrlist:
        scorelist = []
        for _,row in df[(df['year'] == yr)].iterrows():
            score = 0
            if row['legal_gps1819'] == 2:
                score += 1
            if row['legal_gps2122'] == 2:
                score += 1
            if row['legal_handheld'] == 2:
                score += 1
            if row['legal_handheldstop'] == 2:
                score += 1
            if row['legal_handheldspkr'] == 2:
                score += 1
            if row['legal_911'] == 1:
                score += 1
            if row['legal_camera'] == 2:
                score += 1
            if row['legal_music1819'] == 2:
                score += 1
            if row['legal_music2122'] == 2:
                score += 1
            if row['legal_readstop'] == 2:
                score += 1
            if row['legal_typestop'] == 2:
                score += 1
            if row['legal_handfree'] == 1:
                score += 1
            if row['legal_app1819'] == 2:
                score += 1
            if row['legal_app2122'] == 2:
                score += 1
            if row['legal_video'] == 2:
                score += 1


            scorelist.append(score)
            correctavg = (Average(scorelist)/16) * 100

        yearlist.append(yr)
        scoreslist.append(round(correctavg, 2))
        agelist.append(key)

ndf = pd.DataFrame()

ndf['Age Group'] = agelist
ndf['Year'] = yearlist
ndf['Score'] = scoreslist

print(ndf)

fig = go.Figure()
fig = px.line(ndf, x="Year", y="Score", color='Age Group', labels= {'Year':'2018-2022 (Omitting 2020)','Score':'Score in Percentage'}, title='Knowledge of Law by Age Group')
fig.update_xaxes(type='category')
fig.update_layout(
    font_family="Roboto",
    font_color="Navy",
    title_font_family="Roboto",
    title_font_color="navy",
    legend_title_font_color="Navy",
    font=dict(
        family="Roboto, monospace",
        size=40,
        color="Black"
    )
    )
fig.show()