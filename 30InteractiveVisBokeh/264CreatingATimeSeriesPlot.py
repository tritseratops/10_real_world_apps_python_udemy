from bokeh.plotting import figure, output_file, show
import pandas

df = pandas.read_csv("https://query1.finance.yahoo.com/v7/finance/download/ADBE?period1=1596284598&period2=1627820598&interval=1d&events=history&includeAdjustedClose=true",
                     parse_dates = ["Date"])


p = figure(width = 500, height = 500, x_axis_type = "datetime", sizing_mode = "scale_width")

p.line(df["Date"], df["Close"], color = "Orange", alpha = 0.5)

output_file("timeseriesplot.html")
show(p)
