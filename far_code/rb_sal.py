import pandas as pd

cols = ['player', 'player_id', "position", "team_name", "grades_offense", "total_touches"]
nfl_2012 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/rbs/Runningbacks_2012.csv", usecols=cols)
nfl_2013 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/rbs/Runningbacks_2013.csv", usecols=cols)
nfl_2014 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/rbs/Runningbacks_2014.csv", usecols=cols)
nfl_2015 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/rbs/Runningbacks_2015.csv", usecols=cols)
nfl_2016 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/rbs/Runningbacks_2016.csv", usecols=cols)
nfl_2017 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/rbs/Runningbacks_2017.csv", usecols=cols)
nfl_2018 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/rbs/Runningbacks_2018.csv", usecols=cols)
nfl_2019 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/rbs/Runningbacks_2019.csv", usecols=cols)
nfl_2020 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/rbs/Runningbacks_2020.csv", usecols=cols)
nfl_2021 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/rbs/Runningbacks_2021.csv", usecols=cols)
all_sheets = [nfl_2021, nfl_2020, nfl_2019, nfl_2018, nfl_2017, nfl_2016, nfl_2015, nfl_2014, nfl_2013, nfl_2012]

for count, i in enumerate(all_sheets):
    all_sheets[count] = i[(i['position'] == "HB")]

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.drop_duplicates(subset=['player'])

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.sort_values(['team_name', 'total_touches'], ascending=[True, False]).groupby('team_name').head(2)

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.sort_values(['grades_offense'], ascending=[False])

for count, i in enumerate(all_sheets):
    all_sheets[count]["rank"] = i["grades_offense"].rank(method='min', ascending=False)

years = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
for year, i in enumerate(all_sheets):
    i['Year'] = years[year]

running = pd.concat(all_sheets)
running["team_name"] = running["team_name"].replace(to_replace=r'OAK', value=r'LV', regex=True)
running["team_name"] = running["team_name"].replace(to_replace=r'SL', value=r'LA', regex=True)
running["team_name"] = running["team_name"].replace(to_replace=r'SD', value=r'LAC', regex=True)
# running.to_csv(f"running.csv", index=False) ##

sal_cols = ['player-name', 'year signed', 'age', 'year 2', 'value', 'average/year']
sal_2007 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2007.csv", usecols=sal_cols)
sal_2008 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2008.csv", usecols=sal_cols)
sal_2009 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2009.csv", usecols=sal_cols)
sal_2010 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2010.csv", usecols=sal_cols)
sal_2011 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2011.csv", usecols=sal_cols)
sal_2012 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2012.csv", usecols=sal_cols)
sal_2013 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2013.csv", usecols=sal_cols)
sal_2014 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2014.csv", usecols=sal_cols)
sal_2015 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2015.csv", usecols=sal_cols)
sal_2016 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2016.csv", usecols=sal_cols)
sal_2017 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2017.csv", usecols=sal_cols)
sal_2018 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2018.csv", usecols=sal_cols)
sal_2019 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2019.csv", usecols=sal_cols)
sal_2020 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2020.csv", usecols=sal_cols)
sal_2021 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/rb/rb2021.csv", usecols=sal_cols)
all_sal = [sal_2021, sal_2020, sal_2019, sal_2018, sal_2017, sal_2016, sal_2015, sal_2014, sal_2013, sal_2012, sal_2011, sal_2010, sal_2009, sal_2008, sal_2007]

for count, i in enumerate(all_sal):
    all_sal[count] = i.sort_values(['player-name', 'year 2'], ascending=[True, False])

for count, i in enumerate(all_sal):
    all_sal[count] = i.drop_duplicates(subset=['player-name'])

salary = pd.concat(all_sal)

# drop rookie contracts
salary["age"] = salary["age"].replace(to_replace=r'-', value=r'0', regex=True)
salary['age'] = salary['age'].astype('int')
salary = salary[(salary['age'] > 23)]

salary["year signed"] = salary["year signed"].replace(to_replace=r'([0-9]{4})-([0-9]{4}) \(FA: [0-9]*\)', value=r'\1', regex=True)
salary['year signed'] = salary['year signed'].astype('int')

salary = salary.rename({"year signed": "year_signed", "year 2": "contract_length", 'player-name':'player_name'}, axis='columns')

salary["player_name"] = salary["player_name"].replace(to_replace=r"D'Ernest Johnson", value=r"D'Ernest Johnson", regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Melvin Gordon', value=r'Melvin Gordon III', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Mark Ingram', value=r'Mark Ingram II', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Ronald Jones II', value=r'Ronald Jones', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Jeff Wilson', value=r'Jeff Wilson Jr.', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Christopher Carson', value=r'Chris Carson', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'JK Dobbins', value=r'J.K. Dobbins', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r"Tre'quan Smith", value=r"Tre'Quan Smith", regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Duke Johnson', value=r'Duke Johnson Jr.', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Josh Kelley', value=r'Joshua Kelley', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Todd Gurley', value=r'Todd Gurley II', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Bobby Rainey', value=r'Bobby Rainey Jr.', regex=True)

new_salary = pd.DataFrame(columns = ['index', 'player_name', 'year_signed', 'age', 'contract_length', 'value', 'average/year'])
for count, data in enumerate(salary.iterrows()):
    index, row = data[0], data[1]
    years = row['contract_length']
    for j in range(years):
        new_salary.loc[len(new_salary.index)] = [count, row['player_name'], row['year_signed'] + j, row['age'] + j, row['contract_length'], row['value'], row['average/year']]

new_salary["average/year"] = new_salary["average/year"].replace(to_replace=r'\$', value=r'', regex=True)
new_salary["average/year"] = new_salary["average/year"].replace(to_replace=r',', value=r'', regex=True)
new_salary['average/year'] = new_salary['average/year'].astype('int')

new_salary = new_salary.drop_duplicates(subset = ['player_name', 'year_signed'])
new_salary.to_csv(f"rb_sal1.csv", index=False) ##

full = running.merge(new_salary, how = 'inner', left_on=['player', 'Year'], right_on=['player_name', 'year_signed'])
full.to_csv(f"rb_sal2.csv", index=False) ##

# find number of valid receivers for each year
numbers = full['Year'].value_counts()
# print(numbers.mean())

avg = full.copy()
# avg.to_csv(f"rb_test.csv", index=False) ##

average = pd.DataFrame(columns = ['position','player_name', 'team_name', 'grades_offense', 'total_touches', 'rank','Year', 'player_name', 'year_signed', 'age', 'average/year', 'sim_sal'])
end_year = 2021
countem = -1

for count, data in enumerate(avg.iterrows()):
    index, row = data[0], data[1]
    end = numbers.loc[row['Year']] - 1
    if end_year != row['Year']:
        countem = -1
        end_year = row['Year']
    countem += 1
    # change this to change band of numbers, the min is 3, max is 6
    if countem == 0:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                           row['total_touches'], row['rank'], row['Year'], row['player_name'],
                                           row['year_signed'], row['age'], row['average/year'],
                                           avg.iloc[count:count + 3, 14].mean()]
        continue
    if countem == 1:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                       row['total_touches'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count - 1:count + 3, 14].mean()]
        continue
    if countem == 2:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                       row['total_touches'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count - 2:count + 3, 14].mean()]
        continue
    else:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                           row['total_touches'], row['rank'], row['Year'], row['player_name'],
                                           row['year_signed'], row['age'], row['average/year'],
                                           avg.iloc[count-3:count+3, 14].mean()]

average['diff'] = average['average/year'] - average['sim_sal']

average.to_csv(f"rb_something.csv", index=False) ##

teams = average.copy()
end = teams.groupby(['team_name', 'Year'], as_index=False).agg(avg_diff_rb=('diff', 'mean'))
end.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/final/rb_end.csv', index=False)
