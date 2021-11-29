import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc
data = pandas.read_csv('data\\reviews.csv', parse_dates=['Timestamp'])
# print(data.head())
print(data.columns)

day_average  = data
day_average['Dayname']=day_average['Timestamp'].dt.strftime("%A")
day_average['Daynumber']=day_average['Timestamp'].dt.strftime("%w")
print(day_average['Dayname'])
day_average = day_average.groupby(['Dayname', 'Daynumber']).mean()
print(day_average.columns)
print(day_average)
print(type(day_average))
print(day_average.head())
print(day_average.index)

day_average = day_average.sort_values('Daynumber')
plt.figure(figsize=(25,5))
plt.plot(day_average.index.get_level_values(0), day_average['Rating'])
plt.show()
dir(plt)
help(plt.pie)

share = data.groupby(['Course Name'])['Rating'].count()
plt.pie(share, labels=share.index)
plt.show()