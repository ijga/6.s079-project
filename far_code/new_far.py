import pandas as pd

wins = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/far_code/wins_percent.csv")

rb = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/final/rb_end.csv")
wr = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/final/wr_end.csv")
te = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/final/te_end.csv")
ol = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/final/ol_end.csv")
dl = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/final/dl_end.csv")
lb = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/final/lb_end.csv")
db = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/final/db_end.csv")

# copy the data
wr_standardized = wr.copy()
wr_standardized['avg_diff_wr'] = (wr_standardized['avg_diff_wr'] - wr_standardized['avg_diff_wr'].mean()) / wr_standardized['avg_diff_wr'].std()
wr_standardized.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/wr_standardized.csv', index=False) ##

rb_standardized = rb.copy()
rb_standardized['avg_diff_rb'] = (rb_standardized['avg_diff_rb'] - rb_standardized['avg_diff_rb'].mean()) / rb_standardized['avg_diff_rb'].std()
rb_standardized.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/rb_standardized.csv', index=False) ##

te_standardized = te.copy()
te_standardized['avg_diff_te'] = (te_standardized['avg_diff_te'] - te_standardized['avg_diff_te'].mean()) / te_standardized['avg_diff_te'].std()
te_standardized.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/te_standardized.csv', index=False) ##

ol_standardized = ol.copy()
ol_standardized['avg_diff_ol'] = (ol_standardized['avg_diff_ol'] - ol_standardized['avg_diff_ol'].mean()) / ol_standardized['avg_diff_ol'].std()
ol_standardized.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/ol_standardized.csv', index=False) ##

dl_standardized = dl.copy()
dl_standardized['avg_diff_dl'] = (dl_standardized['avg_diff_dl'] - dl_standardized['avg_diff_dl'].mean()) / dl_standardized['avg_diff_dl'].std()
dl_standardized.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/dl_standardized.csv', index=False) ##

lb_standardized = lb.copy()
lb_standardized['avg_diff_lb'] = (lb_standardized['avg_diff_lb'] - lb_standardized['avg_diff_lb'].mean()) / lb_standardized['avg_diff_lb'].std()
lb_standardized.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/lb_standardized.csv', index=False) ##

db_standardized = db.copy()
db_standardized['avg_diff_db'] = (db_standardized['avg_diff_db'] - db_standardized['avg_diff_db'].mean()) / db_standardized['avg_diff_db'].std()
db_standardized.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/db_standardized.csv', index=False) ##

wr_standardized['avg_diff_wr'] = wr_standardized['avg_diff_wr'] * .15384615  # 4/26
rb_standardized['avg_diff_rb'] = rb_standardized['avg_diff_rb'] * .07692308  # 2/26
te_standardized['avg_diff_te'] = te_standardized['avg_diff_te'] * .07692308  # 2/26
ol_standardized['avg_diff_ol'] = ol_standardized['avg_diff_ol'] * .19230769  # 5/26
db_standardized['avg_diff_db'] = db_standardized['avg_diff_db'] * .19230769  # 5/26
lb_standardized['avg_diff_lb'] = lb_standardized['avg_diff_lb'] * .11538462  # 3/26
dl_standardized['avg_diff_dl'] = dl_standardized['avg_diff_dl'] * .19230769  # 5/26

full = wr_standardized.merge(rb_standardized, how='inner', on=['team_name', 'Year'])
full = full.merge(te_standardized, how='inner', on=['team_name', 'Year'])
full = full.merge(ol_standardized, how='inner', on=['team_name', 'Year'])
full = full.merge(db_standardized, how='inner', on=['team_name', 'Year'])
full = full.merge(lb_standardized, how='inner', on=['team_name', 'Year'])
full = full.merge(dl_standardized, how='inner', on=['team_name', 'Year'])

done = pd.DataFrame(columns = ['team_name','year', 'avg_diff'])
for count, data in enumerate(full.iterrows()):
    index, row = data[0], data[1]
    done.loc[len(done.index)] = [row['team_name'], row['Year'], (row['avg_diff_wr'] +  row['avg_diff_rb'] +row['avg_diff_te'] +row['avg_diff_ol']+row['avg_diff_lb']+row['avg_diff_db']+row['avg_diff_dl'])]

done = done.merge(wins, how='inner', on=['team_name', 'year'])

## different aggregations

new = done.groupby('team_name').agg(({'avg_diff': 'sum', 'win_percentage': 'mean'}))
new.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/comparison.csv')

new = done.loc[done["year"].isin([2017,2018,2019,2020,2021])]
new = new.groupby('team_name').agg(({'avg_diff': 'sum', 'win_percentage': 'mean'}))
new.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/comparison17_21.csv')

new = done.loc[done["year"].isin([2012,2013,2014,2015,2016])]
new = new.groupby('team_name').agg(({'avg_diff': 'sum', 'win_percentage': 'mean'}))
new.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/comparison12_16.csv')
####
wr = pd.read_csv("/Users/iangatlin/Desktop/6.s079_project/final/wr_end.csv")
# new = wr.loc[wr["Year"].isin([2012,2013,2014,2015,2016])]
new = wr.groupby('team_name').agg(({'avg_diff_wr': 'mean'}))
new = new.sort_values('avg_diff_wr')
new.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/wr_underVover.csv')

new = wr.loc[wr["Year"].isin([2012,2013,2014,2015,2016])]
new = new.groupby('team_name').agg(({'avg_diff_wr': 'mean'}))
new = new.sort_values('avg_diff_wr')
new.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/wr_underVover12_16.csv')

new = wr.loc[wr["Year"].isin([2017,2018,2019,2020,2021])]
new = new.groupby('team_name').agg(({'avg_diff_wr': 'mean'}))
new = new.sort_values('avg_diff_wr')
new.to_csv(f'/Users/iangatlin/Desktop/6.s079_project/to_visualize/wr_underVover17_21.csv')

# done = done.merge(wins, how='inner', on=['team_name', 'year'])
