import justpy as jp
import pandas
df=pandas.read_csv('reviews.csv')
df['Timestamp']=pandas.to_datetime(df['Timestamp'])
df['Day']=df['Timestamp'].dt.date
df['Week']=df['Timestamp'].dt.strftime('%Y %U')
df['Month']=df['Timestamp'].dt.strftime('%Y %m')
month_avg=df.groupby(['Month','Course Name']).mean().unstack()
data='''
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average Rating by month by course'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
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
            text: 'Average Rating'
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
'''
def web():
    w=jp.QuasarPage()
    h1 = jp.QDiv(a=w, text='Analysis of courses', classes='text-h3 text-center text-secondary q-pa-md ')
    p1 = jp.QDiv(a=w, text='This web page contains the information about the course reviews data')
    c=jp.HighCharts(a=w,options=data)
    c.options.xAxis.categories=list(month_avg.index)
    c.options.series=[{'name':i,'data':list(month_avg['Rating'][i])} for i in month_avg['Rating'].columns]
    c.options.xAxis.title.text='Month'
    return w
jp.justpy(web)