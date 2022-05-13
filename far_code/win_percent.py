import pandas as pd

wins = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/football_team_wins.csv")

wins_percent = pd.DataFrame(columns=['team_name', "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "win_percentage"])
for count, data in enumerate(wins.iterrows()):
    index, row = data[0], data[1]
    wins_percent.loc[len(wins_percent.index)] = [row["team_name"], round(row['2021']/17, 3), round(row['2020']/16, 3), round(row['2019']/16, 3), round(row['2018']/16, 3), round(row['2017']/16, 3), round(row['2016']/16, 3), round(row["2015"]/16, 3), round(row["2014"]/16, 3), round(row["2013"]/16, 3), round(row['2012']/16, 3), row['Win_Percentage']]

ints = ['21', '20', '19', '18', '17', '16', '15', '14', '13', '12']
years = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012']
wins_formatted = pd.DataFrame(columns=['team_name', "year", "win_percentage"])
for count, data in enumerate(wins_percent.iterrows()):
    index, row = data[0], data[1]
    for i in range(10):
        wins_formatted.loc[len(wins_formatted.index)] = [row['team_name'], years[i], row[f'20{ints[i]}']]

wins_formatted.to_csv(f"wins_percent.csv", index=False)
