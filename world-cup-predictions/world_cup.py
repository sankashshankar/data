import pandas as pd
import numpy as np
import sklearn
import matplotlib
import os

from operator import itemgetter
from datetime import *


csv_files = []
for f in os.listdir(os.getcwd()):
	if f[-4:] == ".csv":
		csv_files.append(f)

for idx in range(len(csv_files)):
	temp_df = pd.read_csv(csv_files[idx])
	if idx == 0:
		world_cup = temp_df
	for attr in temp_df.columns[3:]:
		if idx == 0:
			world_cup[attr] = [[elem] for elem in world_cup[attr]]
		else:
			world_cup[attr] = [elem[0] + [elem[1]] for elem in zip(world_cup[attr], temp_df[attr])]


date_time = [datetime(int(item[3:7]), int(item[7:9]), int(item[9:11]), int(item[12:14]), int(item[14:16]), int(item[16:18])) for item in csv_files]
normalized_datetime_intervals = [(date_time[i] - date_time[0]).total_seconds()/86400. for i in range(len(date_time))]

git remote set-url origin https://srs37@github.com/srs37/data.git