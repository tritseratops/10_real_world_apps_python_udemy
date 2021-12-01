import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc
data = pandas.read_csv('data\\reviews.csv', parse_dates=['Timestamp'])
# print(data.head())
# print(data.columns)

# aggregating by day
day_average  = data
day_average['Date']=day_average['Timestamp'].dt.date
day_average = day_average.groupby(['Date']).mean()
# print(day_average.columns)
# print(day_average)
# print(type(day_average))
# print(day_average.head())
# print(day_average.index)

plt.figure(figsize=(25,3))
plt.plot(day_average.index, day_average['Rating'])
plt.show()

# aggregating rating average by week
week_average  = data
week_average['Week']=week_average['Timestamp'].dt.strftime("%Y-%U")
# print(week_average['Week'])
week_average = week_average.groupby(['Week']).mean()
# print(week_average.columns)
# print(week_average)
# print(type(week_average))
# print(week_average.head())
# print(week_average.index)

plt.figure(figsize=(25,5))
plt.plot(week_average.index, week_average['Rating'])
plt.show()

# aggregating rating average by month
month_average  = data
month_average['Month']=month_average['Timestamp'].dt.strftime("%Y-%m")
# print(month_average['Month'])
month_average = month_average.groupby(['Month']).mean()
# print(month_average.columns)
# print(month_average)
# print(type(month_average))
# print(month_average.head())
# print(month_average.index)

plt.figure(figsize=(25,5))
plt.plot(month_average.index, month_average['Rating'])
plt.show()

# aggregating by month and by course
month_course_average  = data
month_course_average['Month']=month_course_average['Timestamp'].dt.strftime("%Y-%m")
month_course_aggregated = month_course_average.groupby(['Month', 'Course Name']).mean().unstack()
print(len(list(month_course_aggregated)))
print("************")

print(list(month_course_aggregated))
print("************")
month_course_aggregated.plot(figsize=(25,5))
plt.show()

month_course_aggregated2 = month_course_average.groupby(['Month', 'Course Name'])['Rating'].count().unstack()
# print(month_course_aggregated2.head())
month_course_aggregated2.plot(figsize=(25,5))

plt.show()