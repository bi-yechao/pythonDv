import json,pygal,math

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

#这里注意列表的定义不能放在for循环中
dates,months,weeks,weekdays,close=[],[],[],[],[]
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    #强制类型转换
    close.append(int(float(btc_dict['close'])))

    # line_chart = pygal.Line(x_label_retation=20,show_minor_x_labels=False)
    # line_chart.title = '收盘价(￥)'
    # line_chart.x_labels = dates
    # N = 20
    # line_chart.x_labels_major = dates[::N]
    # line_chart.add('收盘价',close)
    # line_chart.render_to_file('收盘价折线图(￥).svg')

line_chart = pygal.Line(x_label_retation=20,show_minor_x_labels=False)
line_chart.title = '对数变换收盘价(￥)'
line_chart.x_labels = dates
N = 20
#这里不知道为什么横坐标没有显示出来
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价',close_log)
line_chart.render_to_file('对数变换收盘价折线图(￥).svg')
