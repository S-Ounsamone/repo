import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

survey = pd.read_csv('survey.csv')

yrlist = [2018,2019,2021,2022]
dflist = []

age1 = survey[survey['agegrp1'] == 1]
age2 = survey[survey['agegrp1'] == 2]
age3 = survey[survey['agegrp1'] == 3]
age4 = survey[survey['agegrp1'] == 4]
age5 = survey[survey['agegrp1'] == 5]

dflist.append(age1)
dflist.append(age2)
dflist.append(age3)
dflist.append(age4)
dflist.append(age5)

frames = {}
groups = [1,2,3,4,5]
for grp in groups:   
    frames[grp] = survey[survey['agegrp1'] == grp] # assigning data frame from list to key in dictionary
    
frames['Age Group 16-17'] = frames[1]
frames['Age Group 18-34'] = frames[2]
frames['Age Group 35-49'] = frames[3]
frames['Age Group 50-64'] = frames[4]
frames['Age Group 65+'] = frames[5]

del frames[1]
del frames[2]
del frames[3]
del frames[4]
del frames[5]


agelist = []
yearlist = []
scoreslist = []

for key,df in frames.items():
    for yr in yrlist:
        scorelist = []
        for _,row in df[(df['year'] == yr)].iterrows():
            score = 0
            if row['beh_read'] <= 2:
                score += 1
            if row['beh_type'] <= 2:
                score += 1
            if row['beh_handheld'] <= 2:
                score += 1
            if row['beh_handfree'] <= 2:
                score += 1
            if row['beh_app'] <= 2:
                score += 1
            
            avg = score /5
            
            scorelist.append(avg)
            scoreavg = sum(scorelist)/len(scorelist)

        print('Year:',yr, "Score:", scoreavg,'\t', key)
        yearlist.append(yr)
        scoreslist.append(scoreavg)
        agelist.append(key)
            

ndf = pd.DataFrame()
yrlist = [2018,2019,2021,2022]
ndf['Age Group'] = agelist
ndf['Year'] = yearlist
ndf['Score'] = scoreslist

print(ndf)

fig = go.Figure()
fig = px.line(ndf, x="Year", y="Score", color='Age Group', title='"Last 30 Days" Questions Scores by Age Group (for "Regularly" and "Fairly Often" Responses Only)')
fig.update_xaxes(type='category')
fig.show()
    