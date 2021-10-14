from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df = pandas.read_csv("data.csv")
x = df["x"]
y = df["y"]

# #prepare some data
# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
#
# tri_x = [3,7.5,10]
# tri_y = [3,6,9]
# tri_pow = [10,10,10]


#prepare the output file
output_file("line_from_csv.html")

# create figure object
f = figure()

# create line plot
f.line(x,y)
# f.triangle(x=tri_x,y=tri_y, size=tri_pow,color="#99D594", line_width=2)
# f.circle(x=[3, 7.5, 10], y=[3, 6, 9], size=20)

show(f)