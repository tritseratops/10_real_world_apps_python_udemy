import justpy as jp
import pandas

data = pandas.read_csv('data\\reviews.csv', parse_dates=['Timestamp'])

# aggregating by course
data_course_reviews  = data
data_course_reviews = data_course_reviews.groupby(['Course Name']).count()
# plt.plot(day_average.index.get_level_values(0), day_average['Rating'])

# print(data_course_reviews.index)
# print('*********')
# print(data_course_reviews.head())
# print('*********')
# print(data_course_reviews.columns)
# print('*********')
# print(list(data_course_reviews))
# print('*********')
# print(len(list(data_course_reviews)))
# print('*********')
# print(data_course_reviews.head)
# print('*********')

chart_options = """{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Courses',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
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
    # hc.options.xAxis.categories = list(data_course_reviews.index.get_level_values(0))
    print(list(data_course_reviews.index.get_level_values(0)))
    # series_data =  [{'name': index, 'y': row['Rating']} for index, row in data_course_reviews.iterrows()]
    # print(series_data)
    # hc.options.series[0]['data']=series_data

    return wp

jp.justpy(app)