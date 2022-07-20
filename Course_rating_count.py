import justpy as jp
import pandas
df=pandas.read_csv('reviews.csv')
df['Timestamp']=pandas.to_datetime(df['Timestamp'])
df['Day']=df['Timestamp'].dt.date
df['Week']=df['Timestamp'].dt.strftime('%Y %U')
df['Month']=df['Timestamp'].dt.strftime('%Y %m')
df['Weekday']=df['Timestamp'].dt.strftime('%A')
df_crs=df.groupby('Course Name')['Rating'].count()
data='''
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Percentage of Course Ratings'
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
        name: 'Brands',
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
}
'''
def web():
    w=jp.QuasarPage()
    h1 = jp.QDiv(a=w, text='Analysis of courses', classes='text-h3 text-center text-secondary q-pa-md')
    p1 = jp.QDiv(a=w, text='This web page contains the information about the course reviews data')
    c=jp.HighCharts(a=w,options=data)
    c.options.series[0].data=[{'name':i,'y':j} for i,j in zip(df_crs.index,df_crs)]
    return w
jp.justpy(web)