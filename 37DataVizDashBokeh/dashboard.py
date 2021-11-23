from pandas_datareader import data
import datetime

start = datetime.datetime(2016,1,1)
end = datetime.datetime(2021,6,1)
df = data.DataReader(name="EPAM", data_source="yahoo", start=start, end=end)
print(df)

# print(dir(data.DataReader))