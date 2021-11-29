import pandas
# from pandas import isna
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc
data = pandas.read_csv('data\\reviews.csv', parse_dates=['Timestamp'])

print(data.head())
print(data.shape)
print(data.columns)


hist = data.hist('Rating')
print(hist)
print(type(hist))
ratings = data['Rating']
print(ratings.mean())
print(data[['Course Name', 'Timestamp']])
print(data[['Comment', 'Timestamp']].iloc[3:7])
print(data.iloc[3])
print(data[data['Rating']>4].head())
print(data[data['Rating']>4].count())
# print(data[data['Comment'].notna()][data['Rating']>4].count()) # gives error
data_w_comment = data[data['Comment'].notna()]
data_4_w_comment = data_w_comment[data_w_comment['Rating']>4] # works
print(data_4_w_comment.count())

data_4_w_comment = data[data['Comment'].notna()].query('Rating >4') # works
print(data_4_w_comment.count())

data_4_w_comment = data[(data['Comment'].notna()) & (data_w_comment['Rating']>4)] # works
print(data_4_w_comment.count())

rating4 = data[data['Rating']>4]
print(rating4['Comment'].iloc[1])
print(type(rating4['Comment'].iloc[1]))

plt.hist(ratings, bins = [1,2,3,4,5])
plt.show()

# time base filtering
data_by_date = data[(data['Timestamp']>datetime(2020,7,1, tzinfo=utc)) &
                    (data['Timestamp']<datetime(2020,12,31, tzinfo=utc))]
print(data_by_date.count())


# Average Rating
print(data.Rating.mean())
# Avg rating for particulat course
print(data['Course Name'].iloc[0])
print(data['Rating'][data['Course Name']==
                     "The Python Mega Course: Build 10 Real World Applications"].mean())

# Avg Rating for particulat period for particular course
data_course_10app = data[data['Course Name']=="The Python Mega Course: Build 10 Real World Applications"]
data__course_10app_by_date = data[(data['Timestamp']>datetime(2020,7,1, tzinfo=utc)) &
                    (data['Timestamp']<datetime(2020,12,31, tzinfo=utc))]
print(data__course_10app_by_date['Rating'].mean())

# Avg of uncommented rating
data_4_wo_comment = data[data['Comment'].isna()]
print(data_4_wo_comment.count())
print(data_4_wo_comment['Rating'].mean())

# Avg of commented rating
data_4_wcomment = data[data['Comment'].notna()]
print(data_4_wcomment.count())
print(data_4_wcomment['Rating'].mean())

#  Number of comments containing a certain word
data_4_wcomment = data[data['Comment'].notna()]
data_4_w_accent = data_4_wcomment[data_4_wcomment['Comment'].str.contains('accent')]
print(data_4_w_accent.count())

#  Average on commented rating with accent in comment
# data_4_wcomment = data[data['Comment'].notna()]
data_4_w_accent = data[data['Comment'].str.contains('accent', na=False)]
print(data_4_w_accent['Rating'].mean())

