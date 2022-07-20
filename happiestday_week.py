import justpy as jp
import pandas
df=pandas.read_csv('reviews.csv')
df['Timestamp']=pandas.to_datetime(df['Timestamp'])
df['Day']=df['Timestamp'].dt.date
df['Week']=df['Timestamp'].dt.strftime('%Y %U')
df['Month']=df['Timestamp'].dt.strftime('%Y %m')
df['Weekday']=df['Timestamp'].dt.strftime('%A')
weekday_avg=df.groupby('Weekday').mean()
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
weekday_avg=weekday_avg.reindex(days)
data='''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Happiest day of week'
    },
    subtitle: {
        text: 'According to reviews.csv'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Days'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
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
'''
def web():
    w=jp.QuasarPage()
    h1 = jp.QDiv(a=w, text='Analysis of courses', classes='text-h3 text-center text-secondary q-pa-md')
    p1 = jp.QDiv(a=w, text='This web page contains the information about the course reviews data')
    c=jp.HighCharts(a=w,options=data)
    c.options.xAxis.categories=list(weekday_avg.index)
    c.options.series[0].data=list(weekday_avg['Rating'])
    return w
jp.justpy(web)