import justpy as jp
import pandas
# import matplotlib.pyplot as plt
# from datetime import datetime
# from pytz import utc
data = pandas.read_csv('data\\reviews.csv', parse_dates=['Timestamp'])
week_average  = data
week_average['Week']=week_average['Timestamp'].dt.strftime("%Y-%U")
week_average = week_average.groupby(['Week']).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Rating per Week'
    },
    subtitle: {
        text: 'According to data from udemy'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week'
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
    hc.options.title.text = "Rating per Week"
    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0]['data'] = list(week_average.Rating)
    print(week_average.head())


    return wp

jp.justpy(app)