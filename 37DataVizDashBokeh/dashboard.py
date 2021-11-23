from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

start = datetime.datetime(2016,1,1)
end = datetime.datetime(2016,11,10)
df = data.DataReader(name="EPAM", data_source="yahoo", start=start, end=end)

# print(dir(data.DataReader))

p = figure(x_axis_type="datetime", width=1000, height=300, sizing_mode = "scale_width")
p.title = "Candlestick chart"
p.grid.grid_line_alpha=0
hours_12=12*60*60*1000 # milliseconds in 12 hours

date_increase = df.index[df.Close>df.Open]
date_decrease = df.index[df.Close<df.Open]

def inc_dec(open, close):
    if open<close:
        return "Increase"
    elif close<open:
        return "Decrease"
    else:
        return "Equal"

df["Status"]=[inc_dec(o, c) for o,c in zip(df.Open, df.Close)]
df["Middle"]= (df["Open"]+df["Close"])/2
df["Height"]= abs(df.Open-df.Close)
print(df)

p.segment(
    df.index,
    df.High,
    df.index,
    df.Low,
    color="Black"
)
p.rect(
    df.index[df.Status=="Decrease"],
    df.Middle[df.Status=="Decrease"],
    hours_12,
    df.Height[df.Status=="Decrease"],
    fill_color="#ffb1b6",
    line_color="black")

p.rect(
    df.index[df.Status=="Increase"],
    df.Middle[df.Status=="Increase"],
    hours_12,
    df.Height[df.Status=="Increase"],
    fill_color="#a9ffeb",
    line_color="black")

output_file("CS.html")

show(p)