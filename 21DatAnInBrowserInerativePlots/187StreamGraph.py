import justpy as jp
import pandas

data = pandas.read_csv('data\\reviews.csv', parse_dates=['Timestamp'])

# aggregating by month and by course
month_course_average = data
month_course_average['Month']=month_course_average['Timestamp'].dt.strftime("%Y-%m")
month_course_aggregated = month_course_average.groupby(['Month', 'Course Name']).mean().unstack()
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
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

# average rating by month by course
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course reviews",
                 classes="text-h3 text-center q-py-xl q-px-xl")
    p1 = jp.QDiv(a=wp, text="These Graphs represents Course review analysis")
    hc = jp.HighCharts(a=wp, options=chart_options)
    hc.options.title.text = "Rating per Month"
    hc.options.xAxis.categories = list(month_course_aggregated.index)

    series = [{'name':index[1], 'data':[rating for rating in month_course_aggregated[index]]} for index in month_course_aggregated.columns]
    # series = []
    # for course in month_course_aggregated.columns:
    #     course_dict = {"name": course[1]}
    #     course_data=[]
    #     for rating in month_course_aggregated[course]:
    #         course_data.append(rating)
    #     course_dict['data'] = course_data
    #     series.append(course_dict)

    hc.options.series=series

    return wp

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
# for course in list(month_course_aggregated):
#     print(course)
#     print(type(course))
# print(month_course_aggregated['The Python Mega Course: Build 10 Real World Applications'])

# for course in month_course_aggregated.columns:
#     print(course)
#     print(month_course_aggregated[course])

jp.justpy(app)