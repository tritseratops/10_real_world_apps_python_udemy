from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df = pandas.read_csv("bachelors.csv")
x = df["Year"]
y = df["Engineering"]


#prepare the output file
output_file("barchelors.html")

# create figure object
f = figure()
f.title.text="Cool Data"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Year"
f.yaxis.axis_label="Barchelors"

# create line plot
f.line(x,y)


show(f)