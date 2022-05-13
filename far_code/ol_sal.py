import pandas as pd

cols = ['player', 'player_id', "position", "team_name", "grades_offense", "snap_counts_block"]
nfl_2012 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/blocking/Blocking_2012.csv", usecols=cols)
nfl_2013 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/blocking/Blocking_2013.csv", usecols=cols)
nfl_2014 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/blocking/Blocking_2014.csv", usecols=cols)
nfl_2015 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/blocking/Blocking_2015.csv", usecols=cols)
nfl_2016 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/blocking/Blocking_2016.csv", usecols=cols)
nfl_2017 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/blocking/Blocking_2017.csv", usecols=cols)
nfl_2018 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/blocking/Blocking_2018.csv", usecols=cols)
nfl_2019 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/blocking/Blocking_2019.csv", usecols=cols)
nfl_2020 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/blocking/Blocking_2020.csv", usecols=cols)
nfl_2021 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/nfl/blocking/Blocking_2021.csv", usecols=cols)
all_sheets = [nfl_2021, nfl_2020, nfl_2019, nfl_2018, nfl_2017, nfl_2016, nfl_2015, nfl_2014, nfl_2013, nfl_2012]

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.loc[i["position"].isin(["C","G","T"])]

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.drop_duplicates(subset=['player'])

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.sort_values(['team_name', 'snap_counts_block'], ascending=[True, False]).groupby('team_name').head(5)

for count, i in enumerate(all_sheets):
    all_sheets[count] = i.sort_values(['grades_offense'], ascending=[False])

for count, i in enumerate(all_sheets):
    all_sheets[count]["rank"] = i["grades_offense"].rank(method='min', ascending=False)


years = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
for year, i in enumerate(all_sheets):
    i['Year'] = years[year]

running = pd.concat(all_sheets)
running["team_name"] = running["team_name"].replace(to_replace = r'OAK', value = r'LV', regex = True)
running["team_name"] = running["team_name"].replace(to_replace = r'SL', value = r'LA', regex = True)
running["team_name"] = running["team_name"].replace(to_replace = r'SD', value = r'LAC', regex = True)
# running.to_csv(f"ol_running.csv", index=False) ##

sal_cols = ['player-name', 'year signed', 'age', 'year 2', 'value', 'average/year']
sal_2007 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2007.csv", usecols=sal_cols)
sal_2008 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2008.csv", usecols=sal_cols)
sal_2009 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2009.csv", usecols=sal_cols)
sal_2010 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2010.csv", usecols=sal_cols)
sal_2011 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2011.csv", usecols=sal_cols)
sal_2012 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2012.csv", usecols=sal_cols)
sal_2013 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2013.csv", usecols=sal_cols)
sal_2014 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2014.csv", usecols=sal_cols)
sal_2015 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2015.csv", usecols=sal_cols)
sal_2016 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2016.csv", usecols=sal_cols)
sal_2017 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2017.csv", usecols=sal_cols)
sal_2018 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2018.csv", usecols=sal_cols)
sal_2019 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2019.csv", usecols=sal_cols)
sal_2020 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2020.csv", usecols=sal_cols)
sal_2021 = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/salary/ol/ol2021.csv", usecols=sal_cols)
all_sal = [sal_2021, sal_2020, sal_2019, sal_2018, sal_2017, sal_2016, sal_2015, sal_2014, sal_2013, sal_2012, sal_2011, sal_2010, sal_2009, sal_2008, sal_2007]

for count, i in enumerate(all_sal):
    all_sal[count] = i.sort_values(['player-name', 'year 2'], ascending=[True, False])

for count, i in enumerate(all_sal):
    all_sal[count] = i.drop_duplicates(subset=['player-name'])

salary = pd.concat(all_sal)

# drop rookie contracts
salary["age"] = salary["age"].replace(to_replace=r'-', value=r'0', regex=True)
salary['age'] = salary['age'].astype('int')
# salary = salary[(salary['age'] > 23)]

salary["year signed"] = salary["year signed"].replace(to_replace=r'([0-9]{4})-([0-9]{4}) \(FA: [0-9]*\)', value=r'\1', regex=True)
salary['year signed'] = salary['year signed'].astype('int')

salary = salary.rename({"year signed": "year_signed", "year 2": "contract_length", 'player-name':'player_name'}, axis='columns')

salary["player_name"] = salary["player_name"].replace(to_replace=r'Charles Leno', value=r'Charles Leno Jr.', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Mike Onwenu', value=r'Michael Onwenu', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Michael Schofield', value=r'Michael Schofield III', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Jedrick Wills', value=r'Jedrick Wills Jr.', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r"Dan Moore", value=r"Dan Moore Jr.", regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Lloyd Cushenberry', value=r'Lloyd Cushenberry III', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Chuks Okorafor', value=r'Chukwuma Okorafor', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Geron Christian', value=r'Geron Christian Sr.', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Cameron Erving', value=r'Cam Erving', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Roger Lewis', value=r'Andrew Wylie', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r"Ja'Wuan James", value=r"Ja'Wuan James", regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Trenton Brown', value=r'Trent Brown', regex=True)
salary["player_name"] = salary["player_name"].replace(to_replace=r'Michael Person', value=r'Mike Person', regex=True)

new_salary = pd.DataFrame(columns = ['index','player_name', 'year_signed', 'age', 'contract_length', 'value', 'average/year'])
for count, data in enumerate(salary.iterrows()):
    index, row = data[0], data[1]
    years = row['contract_length']
    for j in range(years):
        new_salary.loc[len(new_salary.index)] = [count, row['player_name'], row['year_signed'] + j, row['age'] + j, row['contract_length'], row['value'], row['average/year']]

new_salary["average/year"] = new_salary["average/year"].replace(to_replace=r'\$', value=r'', regex=True)
new_salary["average/year"] = new_salary["average/year"].replace(to_replace=r',', value=r'', regex=True)
new_salary['average/year'] = new_salary['average/year'].astype('int')

new_salary = new_salary.drop_duplicates(subset=['player_name', 'year_signed'])
new_salary.to_csv(f"ol_sal1.csv", index=False) ##

full = running.merge(new_salary, how='inner', left_on=['player', 'Year'], right_on=['player_name', 'year_signed'])
full.to_csv(f"ol_sal2.csv", index=False) ##

# find number of valid receivers for each year
numbers = full['Year'].value_counts()
# print(numbers.mean())

avg = full.copy()
# avg.to_csv(f"rb_test.csv", index=False)

average = pd.DataFrame(columns = ['position', 'player_name', 'team_name', 'grades_offense', 'snap_counts_block', 'rank',
                                  'Year', 'player_name', 'year_signed', 'age', 'average/year', 'sim_sal'])
end_year = 2021
countem = -1

for count, data in enumerate(avg.iterrows()):
    index, row = data[0], data[1]
    end = numbers.loc[row['Year']] - 1
    if end_year != row['Year']:
        countem = -1
        end_year = row['Year']
    countem += 1
    # change this to change band of numbers, the min is 6, max is 12
    if countem == 0:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                           row['snap_counts_block'], row['rank'], row['Year'], row['player_name'],
                                           row['year_signed'], row['age'], row['average/year'],
                                           avg.iloc[count:count + 6, 14].mean()]
        continue
    if countem == 1:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                       row['snap_counts_block'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count - 1:count + 6, 14].mean()]
        continue
    if countem == 2:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                       row['snap_counts_block'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count - 2:count + 6, 14].mean()]
        continue
    if countem == 3:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                       row['snap_counts_block'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count - 3:count + 6, 14].mean()]
        continue
    if countem == 4:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                       row['snap_counts_block'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count - 4:count + 6, 14].mean()]
        continue
    if countem == 5:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                       row['snap_counts_block'], row['rank'], row['Year'], row['player_name'],
                                       row['year_signed'], row['age'], row['average/year'],
                                       avg.iloc[count - 5:count + 6, 14].mean()]
        continue
    else:
        average.loc[len(average.index)] = [row['position'], row['player_name'], row['team_name'], row['grades_offense'],
                                           row['snap_counts_block'], row['rank'], row['Year'], row['player_name'],
                                           row['year_signed'], row['age'], row['average/year'],
                                           avg.iloc[count-6:count+6, 14].mean()]

average['diff'] = average['average/year'] - average['sim_sal']

average.to_csv(f"ol_something.csv", index=False) ##

teams = average.copy()
end = teams.groupby(['team_name', 'Year'], as_index=False).agg(avg_diff_ol=('diff', 'mean'))
end.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/final/ol_end.csv', index=False) ##
