import justpy as jp
import pandas
# import matplotlib.pyplot as plt
# from datetime import datetime
# from pytz import utc
data = pandas.read_csv('data\\reviews.csv', parse_dates=['Timestamp'])
day_average = data
day_average['Date']=day_average['Timestamp'].dt.date
day_average = day_average.groupby(['Date']).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Rating per day'
    },
    subtitle: {
        text: 'According to data from udemy'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Day'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 2018 to 2021 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: 1 to 5.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp=jp.QuasarPage()
    h1 = jp.QDiv(a=wp,text="Analysis of Course reviews",
                 classes="text-h3 text-center q-py-xl q-px-xl")
    p1 = jp.QDiv(a=wp,text="Theese Graphs represents Course review analysis")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Rating per day"
    # x = day_average.index
    # y = day_average.Rating
    # print(day_average)
    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0]['data'] = list(day_average.Rating)
    print(day_average.head())
    # print(hc.options.title.text)
    # print(hc.options, flush=True)
    # print(type(hc.options),flush=True)

    return wp

jp.justpy(app)