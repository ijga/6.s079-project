import pandas as pd

cols = ['player', 'player_id', "position","team_name", "grades_defense", "snap_counts_run"]
nfl_2012 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/run_defense/RunDefenders_2012.csv", usecols= cols)
nfl_2013 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/run_defense/RunDefenders_2013.csv", usecols= cols)
nfl_2014 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/run_defense/RunDefenders_2014.csv", usecols= cols)
nfl_2015 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/run_defense/RunDefenders_2015.csv", usecols= cols)
nfl_2016 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/run_defense/RunDefenders_2016.csv", usecols= cols)
nfl_2017 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/run_defense/RunDefenders_2017.csv", usecols= cols)
nfl_2018 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/run_defense/RunDefenders_2018.csv", usecols= cols)
nfl_2019 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/run_defense/RunDefenders_2019.csv", usecols= cols)
nfl_2020 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/run_defense/RunDefenders_2020.csv", usecols= cols)
nfl_2021 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/run_defense/RunDefenders_2021.csv", usecols= cols)
all_sheets = [nfl_2021, nfl_2020, nfl_2019, nfl_2018, nfl_2017, nfl_2016, nfl_2015, nfl_2014, nfl_2013, nfl_2012]

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.loc[i["position"].isin(["DI","ED"])]

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.drop_duplicates(subset=['player'])

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.sort_values(['team_name', 'snap_counts_run'], ascending=[True, False]).groupby('team_name').head(5)

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.sort_values(['grades_defense'], ascending=[False])

for count, i in enumerate(all_sheets):
    all_sheets[count]["rank"] = i["grades_defense"].rank(method='min', ascending=False)

years = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
for year, i in enumerate(all_sheets):
    i['Year'] = years[year]

running = pd.concat(all_sheets)
running["team_name"] = running["team_name"].replace(to_replace = r'OAK', value = r'LV', regex = True)
running["team_name"] = running["team_name"].replace(to_replace = r'SL', value = r'LA', regex = True)
running["team_name"] = running["team_name"].replace(to_replace = r'SD', value = r'LAC', regex = True)
# running.to_csv(f"dl_running.csv", index=False) ##

sal_cols = ['player-name', 'year signed', 'age', 'year 2', 'value', 'average/year']
sal_2007 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2007.csv", usecols= sal_cols)
sall_2007 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2007.csv", usecols=sal_cols)
sal_2007 = pd.concat([sall_2007, sal_2007])
sal_2008 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2008.csv", usecols= sal_cols)
sall_2008 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2008.csv", usecols=sal_cols)
sal_2008 = pd.concat([sall_2008, sal_2008])
sal_2009 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2009.csv", usecols= sal_cols)
sall_2009 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2009.csv", usecols=sal_cols)
sal_2009 = pd.concat([sall_2009, sal_2009])
sal_2010 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2010.csv", usecols= sal_cols)
sall_2010 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2010.csv", usecols=sal_cols)
sal_2010 = pd.concat([sall_2010, sal_2010])
sal_2011 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2011.csv", usecols= sal_cols)
sall_2011 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2011.csv", usecols=sal_cols)
sal_2011 = pd.concat([sall_2011, sal_2011])
sal_2012 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2012.csv", usecols= sal_cols)
sall_2012 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2012.csv", usecols=sal_cols)
sal_2012 = pd.concat([sall_2012, sal_2012])
sal_2013 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2013.csv", usecols= sal_cols)
sall_2013 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2013.csv", usecols=sal_cols)
sal_2013 = pd.concat([sall_2013, sal_2013])
sal_2014 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2014.csv", usecols= sal_cols)
sall_2014 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2014.csv", usecols=sal_cols)
sal_2014 = pd.concat([sall_2014, sal_2014])
sal_2015 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2015.csv", usecols= sal_cols)
sall_2015 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2015.csv", usecols=sal_cols)
sal_2015 = pd.concat([sall_2015, sal_2015])
sal_2016 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2016.csv", usecols= sal_cols)
sall_2016 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2016.csv", usecols=sal_cols)
sal_2016 = pd.concat([sall_2016, sal_2016])
sal_2017 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2017.csv", usecols= sal_cols)
sall_2017 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2017.csv", usecols=sal_cols)
sal_2017 = pd.concat([sall_2017, sal_2017])
sal_2018 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2018.csv", usecols= sal_cols)
sall_2018 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2018.csv", usecols=sal_cols)
sal_2018 = pd.concat([sall_2018, sal_2018])
sal_2019 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2019.csv", usecols= sal_cols)
sall_2019 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2019.csv", usecols=sal_cols)
sal_2019 = pd.concat([sall_2019, sal_2019])
sal_2020 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2020.csv", usecols= sal_cols)
sall_2020 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2020.csv", usecols=sal_cols)
sal_2020 = pd.concat([sall_2020, sal_2020])
sal_2021 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/dl/dl2021.csv", usecols= sal_cols)
sall_2021 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/lb/lb2021.csv", usecols=sal_cols)
sal_2021 = pd.concat([sall_2021, sal_2021])

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

salary["player_name"] = salary["player_name"].replace(to_replace = r'Melvin Ingram', value = r'Melvin Ingram III', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'DeForest Buckner', value = r'DeForest Buckner', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Jerry Hughes', value = r'Jerry Hughes', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Harold Landry', value = r'Harold Landry III', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Matt Judon', value = r'Matthew Judon', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Deatrich Wise', value = r'Deatrich Wise Jr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'DeMarcus Lawrence', value = r'Demarcus Lawrence', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Foley Fatukasi', value = r'Folorunso Fatukasi', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Sebastian Joseph', value = r'Sebastian Joseph-Day', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Matthew Ioannidis', value = r'Matt Ioannidis', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r"Da'Ron Payne", value = r'Daron Payne', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Damon Harrison', value = r'Damon Harrison Sr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Domata Peko', value = r'Domata Peko Sr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Vic Beasley', value = r'Vic Beasley Jr.', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Clay Matthews Jr.', value = r'Clay Matthews', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Ronald Blair', value = r'Ronald Blair III', regex = True)
salary["player_name"] = salary["player_name"].replace(to_replace = r'Mario Edwards', value = r'Mario Edwards Jr.', regex = True)

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
new_salary.to_csv(f"dl_sal1.csv", index=False)

full = running.merge(new_salary, how = 'inner', left_on=['player', 'Year'], right_on=['player_name', 'year_signed'])
full.to_csv(f"dl_sal2.csv", index=False) ##

# find number of valid receivers for each year
numbers = full['Year'].value_counts()
# print(numbers.mean())

avg = full.copy()
# avg.to_csv(f"dl_test.csv", index=False) ##

average = pd.DataFrame(columns = ['position','player_name', 'team_name', 'grades_defense', 'snap_counts_run', 'rank','Year', 'player_name', 'year_signed', 'age', 'average/year', 'sim_sal'])
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
                                           row['snap_counts_run'], row['rank'], row['Year'], row['player_name'],
                                           row['year_signed'], row['age'], row['average/year'],
                                           avg.iloc[count:count + 6, 14].mean()]
        continue
    if countem == 1:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                       row['snap_counts_run'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count  - 1:count  + 6, 14].mean()]
        continue
    if countem == 2:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                       row['snap_counts_run'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count  - 2:count  + 6, 14].mean()]
        continue
    if countem == 3:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                       row['snap_counts_run'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count  - 3:count  + 6, 14].mean()]
        continue
    if countem == 4:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                       row['snap_counts_run'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count  - 4:count  + 6, 14].mean()]
        continue
    if countem == 5:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                       row['snap_counts_run'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count  - 5:count  + 6, 14].mean()]
        continue
    else:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_defense'],
                                           row['snap_counts_run'], row['rank'], row['Year'], row['player_name'],
                                           row['year_signed'], row['age'], row['average/year'],
                                           avg.iloc[count-6:count+6, 14].mean()]

average['diff'] = average['average/year'] - average['sim_sal']

average.to_csv(f"dl_something.csv", index=False) ##

teams = average.copy()
end = teams.groupby(['team_name', 'Year'], as_index=False).agg(avg_diff_dl=('diff', 'mean'))
end.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/final/dl_end.csv', index=False) ##
