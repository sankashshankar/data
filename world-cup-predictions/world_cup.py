import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import os

from operator import itemgetter
from datetime import *


csv_files = []
for f in os.listdir(os.getcwd()):
	if f[-4:] == ".csv":
		csv_files.append(f)

world_cup = pd.DataFrame()

# clean this up
for idx, csv_file in enumerate(csv_files):
	temp_df = pd.read_csv(csv_file)
	if idx == 0:
		world_cup = temp_df

	for attr in temp_df.columns[3:]:
		if idx == 0:
			world_cup[attr] = [[elem] for elem in world_cup[attr]]
		else:
			world_cup[attr] = [elem[0] + [elem[1]] for elem in zip(world_cup[attr], temp_df[attr])]

world_cup.index = list(world_cup['country_id'])
world_cup = world_cup.drop(['country', 'country_id'],1)

date_time = [datetime(
	year=int(item[3:7]),
 	month=int(item[7:9]),
 	day=int(item[9:11]), 
 	hour=int(item[12:14]), 
 	minute=int(item[14:16]), 
 	second=int(item[16:18])) for item in csv_files]

minute = 60
hour = 60 * minute
day = 24 * hour

normalized_datetime_intervals = [(date_time[i] - date_time[0]).total_seconds()/day for i in range(len(date_time))]

fig = plt.figure()
ax1 = fig.add_subplot(111)
# plt.scatter(normalized_datetime_intervals, world_cup.loc['ESP']['win'], c='#E60026',label='Spain')
# plt.scatter(normalized_datetime_intervals, world_cup.loc['BRA']['win'], c='#FFCC29',label='Brazil')
# plt.scatter(normalized_datetime_intervals, world_cup.loc['ARG']['win'], c='#75AADB',label='Argentina')
# plt.scatter(normalized_datetime_intervals, world_cup.loc['GER']['win'], c='#000000',label='Germany')
plt.scatter(normalized_datetime_intervals, world_cup.loc['USA']['win'], c='b', label='United States')
plt.scatter(normalized_datetime_intervals, world_cup.loc['MEX']['win'], c='g', label='Mexico')

plt.legend(loc='upper left')
plt.show()
