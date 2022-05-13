import pandas as pd

cols = ['player', 'player_id', "position","team_name", "grades_defense", "snap_counts_pass_play" ]
nfl_2012 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/pass_defense/Coverage_2012.csv", usecols= cols)
nfl_2013 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/pass_defense/Coverage_2013.csv", usecols= cols)
nfl_2014 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/pass_defense/Coverage_2014.csv", usecols= cols)
nfl_2015 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/pass_defense/Coverage_2015.csv", usecols= cols)
nfl_2016 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/pass_defense/Coverage_2016.csv", usecols= cols)
nfl_2017 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/pass_defense/Coverage_2017.csv", usecols= cols)
nfl_2018 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/pass_defense/Coverage_2018.csv", usecols= cols)
nfl_2019 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/pass_defense/Coverage_2019.csv", usecols= cols)
nfl_2020 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/pass_defense/Coverage_2020.csv", usecols= cols)
nfl_2021 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/pass_defense/Coverage_2021.csv", usecols= cols)
all_sheets = [nfl_2021, nfl_2020, nfl_2019, nfl_2018, nfl_2017, nfl_2016, nfl_2015, nfl_2014, nfl_2013, nfl_2012]

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.loc[i["position"].isin(["CB","S"])]

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.drop_duplicates(subset=['player'])

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.sort_values(['team_name', 'snap_counts_pass_play'], ascending=[True, False]).groupby('team_name').head(5)

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.sort_values(['grades_defense'], ascending=[False])

for count, i in enumerate(all_sheets):
    all_sheets[count]["rank"] = i["grades_defense"].rank(method ='min' ,ascending=False)

years = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
for year, i in enumerate(all_sheets):
    i['Year'] = years[year]

running = pd.concat(all_sheets)
running["team_name"] = running["team_name"].replace(to_replace = r'OAK', value = r'LV', regex = True)
running["team_name"] = running["team_name"].replace(to_replace = r'SL', value = r'LA', regex = True)
running["team_name"] = running["team_name"].replace(to_replace = r'SD', value = r'LAC', regex = True)
# running.to_csv(f"db_running.csv", index=False) ##

sal_cols = ['player-name', 'year signed', 'age', 'year 2','value','average/year']
sal_2007 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2007.csv", usecols= sal_cols)
sal_2008 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2008.csv", usecols= sal_cols)
sal_2009 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2009.csv", usecols= sal_cols)
sal_2010 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2010.csv", usecols= sal_cols)
sal_2011 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2011.csv", usecols= sal_cols)
sal_2012 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2012.csv", usecols= sal_cols)
sal_2013 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2013.csv", usecols= sal_cols)
sal_2014 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2014.csv", usecols= sal_cols)
sal_2015 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2015.csv", usecols= sal_cols)
sal_2016 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2016.csv", usecols= sal_cols)
sal_2017 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2017.csv", usecols= sal_cols)
sal_2018 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2018.csv", usecols= sal_cols)
sal_2019 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2019.csv", usecols= sal_cols)
sal_2020 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2020.csv", usecols= sal_cols)
sal_2021 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/db/db2021.csv", usecols= sal_cols)
all_sal = [sal_2021, sal_2020, sal_2019, sal_2018, sal_2017, sal_2016, sal_2015, sal_2014, sal_2013, sal_2012, sal_2011, sal_2010, sal_2009, sal_2008, sal_2007]

for count, i in enumerate(all_sal):
    all_sal[count] = i.sort_values(['player-name', 'year 2'], ascending=[True, False])

for count, i in enumerate(all_sal):
    all_sal[count] = i.drop_duplicates(subset=['player-name'])

salary = pd.concat(all_sal)

# drop rookie contracts
salary["age"] = salary["age"].replace(to_replace = r'-', value = r'0', regex = True)
salary['age'] = salary['age'].astype('int')
salary = salary[(salary['age'] > 23)]

salary["year signed"] = salary["year signed"].replace(to_replace = r'([0-9]{4})-([0-9]{4}) \(FA: [0-9]*\)', value = r'\1', regex = True)
salary['year signed'] = salary['year signed'].astype('int')

salary = salary.rename({"year signed": "year_signed", "year 2": "contract_length", 'player-name':'player_name'}, axis='columns')

salary["player_name"] = salary["player_name"].replace(to_replace = r'D.J. Reed', value = r'D.J. Reed Jr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Casey Hayward ', value = r'Casey Hayward Jr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Chris Harris', value = r'Chris Harris Jr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Kenny Moore', value = r'Kenny Moore II', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Byron Murphy ', value = r'Byron Murphy Jr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'David Long', value = r'David Long Jr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r"Michael Carter", value = r"Michael Carter II", regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'William Jackson', value = r'William Jackson III', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Desmond King', value = r'Desmond King II', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Tashaun Gipson', value = r'Tashaun Gipson Sr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'John Johnson', value = r'John Johnson III', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Lonnie Johnson', value = r'Lonnie Johnson Jr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Vernon Hargreaves', value = r'Vernon Hargreaves III', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Earl Thomas', value = r'Earl Thomas III', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'D.J. Swearinger', value = r'D.J. Swearinger Sr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Travis Carrie', value = r'T.J. Carrie', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Tramaine Brock', value = r'Tramaine Brock Sr.', regex = True)

new_salary = pd.DataFrame(columns = ['index','player_name', 'year_signed', 'age', 'contract_length', 'value','average/year'])
for count, data in enumerate(salary.iterrows()):
    index, row = data[0], data[1]
    years = row['contract_length']
    for j in range(years):
        new_salary.loc[len(new_salary.index)] = [count, row['player_name'], row['year_signed'] + j, row['age'] + j, row['contract_length'], row['value'], row['average/year']]

new_salary["average/year"] = new_salary["average/year"].replace(to_replace = r'\$', value = r'', regex = True)
new_salary["average/year"] = new_salary["average/year"].replace(to_replace = r',', value = r'', regex = True)
new_salary['average/year'] = new_salary['average/year'].astype('int')

new_salary = new_salary.drop_duplicates(subset = ['player_name', 'year_signed'])
new_salary.to_csv(f"db_sal1.csv", index=False) ##

full = running.merge(new_salary, how = 'inner', left_on=['player', 'Year'], right_on=['player_name', 'year_signed'])
full.to_csv(f"db_sal2.csv", index=False) ##

# find number of valid receivers for each year
numbers = full['Year'].value_counts()
# print(numbers.mean())

avg = full.copy()
# avg.to_csv(f"db_test.csv", index=False)

average = pd.DataFrame(columns = ['position','player_name', 'team_name', 'grades_defense', 'snap_counts_pass_play', 'rank','Year', 'player_name', 'year_signed', 'age', 'average/year', 'sim_sal'])
end_year = 2021
countem = -1

for count, data in enumerate(avg.iterrows()):
    index, row = data[0], data[1]
    end = numbers.loc[row['Year']] - 1
    if end_year != row['Year']:
        countem = -1
        end_year = row['Year']
    countem += 1

    if countem == 0:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                           row['snap_counts_pass_play'], row['rank'], row['Year'], row['player_name'],
                                           row['year_signed'], row['age'], row['average/year'],
                                           avg.iloc[count :count  + 6, 14].mean()]
        continue
    if countem == 1:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                       row['snap_counts_pass_play'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count  - 1:count  + 6, 14].mean()]
        continue
    if countem == 2:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                       row['snap_counts_pass_play'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count  - 2:count  + 6, 14].mean()]
        continue
    if countem == 3:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                       row['snap_counts_pass_play'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count  - 3:count  + 6, 14].mean()]
        continue
    if countem == 4:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                       row['snap_counts_pass_play'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count  - 4:count  + 6, 14].mean()]
        continue
    if countem == 5:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                       row['snap_counts_pass_play'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count  - 5:count  + 6, 14].mean()]
        continue
    else:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                           row['snap_counts_pass_play'], row['rank'], row['Year'], row['player_name'],
                                           row['year_signed'], row['age'], row['average/year'],
                                           avg.iloc[count-6:count+6, 14].mean()]

average['diff'] = average['average/year'] - average['sim_sal']

average.to_csv(f"db_something.csv", index=False) ##

teams = average.copy()
end = teams.groupby(['team_name', 'Year'], as_index=False).agg(avg_diff_db=('diff', 'mean'))
end.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/final/db_end.csv', index=False) ##

