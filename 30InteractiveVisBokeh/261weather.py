from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df = pandas.read_excel("verlegenhuken.xlsx")
x = df["Temperature"]/10
y = df["Pressure"]/10


#prepare the output file
output_file("verlegenhuken.html")

# create figure object
f = figure()
f.title.text="Temperature and pressure"
f.title.text_color="Red"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color="Yellow"
f.yaxis.minor_tick_line_color="Green"
f.xaxis.axis_label="Temperature (°C)"
f.yaxis.axis_label="Pressure (hPa)"

# create line plot
f.circle(x,y, size=1, color="red")


show(f)