import justpy as jp
import pandas

data = pandas.read_csv('data\\reviews.csv', parse_dates=['Timestamp'])

# aggregating by month and by course
day_average  = data
day_average['Dayname']=day_average['Timestamp'].dt.strftime("%A")
day_average['Daynumber']=day_average['Timestamp'].dt.strftime("%w")
print(day_average['Dayname'])
day_average = day_average.groupby(['Dayname', 'Daynumber']).mean()
day_average = day_average.sort_values('Daynumber')
# plt.plot(day_average.index.get_level_values(0), day_average['Rating'])

# print(month_course_aggregated.index)
# print('*********')
# print(month_course_aggregated.head())
# print('*********')
# print(month_course_aggregated.columns)
# print('*********')
# print(list(month_course_aggregated))
# print('*********')
# print(len(list(month_course_aggregated)))
# print('*********')
# print(month_course_aggregated.head)
# print('*********')

chart_options = """{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Happiest Day in the week'
    },
    subtitle: {
        text: 'According to the udemy rating data'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 1 to 5.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Day'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: Monday to Sunday.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Day',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}"""

# average rating by month by course
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course reviews",
                 classes="text-h3 text-center q-py-xl q-px-xl")
    p1 = jp.QDiv(a=wp, text="These Graphs represents Course review analysis")
    hc = jp.HighCharts(a=wp, options=chart_options)
    hc.options.title.text = "Rating per Month"
    hc.options.xAxis.categories = list(day_average.index.get_level_values(0))
    hc.options.series[0]['data']=list(day_average['Rating'])


    return wp

jp.justpy(app)