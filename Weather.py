import requests
import re
url=''
citysites=(
        ["http://www.weather.com.cn/weathern/101010100.shtml",'北京'],
        ["http://www.weather.com.cn/weathern/101020100.shtml" ,'上海'],
        ["http://www.weather.com.cn/weathern/101210101.shtml" ,'杭州'],
        ["http://www.weather.com.cn/weathern/101280101.shtml" ,'广州'],
        ["http://www.weather.com.cn/weathern/101200101.shtml" ,'武汉'],
        ["http://www.weather.com.cn/weathern/101190101.shtml" ,'南京'],
        ["http://www.weather.com.cn/weathern/101280601.shtml", '深圳'],
        ["http://www.weather.com.cn/weathern/101190401.shtml" ,'苏州'],
        ["http://www.weather.com.cn/weathern/101230201.shtml", '厦门'],
        ["http://www.weather.com.cn/weathern/101220101.shtml",'合肥'] ,
        ["http://www.weather.com.cn/weathern/203010101.shtml",'柏林'],
        ["http://www.weather.com.cn/weathern/401110101.shtml",'纽约'],
        ["http://www.weather.com.cn/weathern/201010100.shtml",'伦敦'],
        ["http://www.weather.com.cn/weathern/124020100.shtml",'迪拜'],
)
def getUrl():
    global url
    while True:
        city = input('请输入城市名称来查询城市天气，如“北京”，“柏林”.. ,输入 2.返回:\n')
        for i in citysites:
            if city in i :
                url=i[0]
                return 0
        if city!='2' and url=='':
            print('抱歉，无法查看该城市天气，请尝试其他城市')
        if city=='2':
            break


def getWeather():
    global url
    print('正在查询中',end='')
    site=requests.get(url)
    print('.',end='')
    site.encoding='utf-8'
    textInfo=site.text

    #昨天今天明天
    dateInfo=re.findall(r'<p class="date-info">.*</p>',textInfo)
    newDate=''.join(dateInfo)
    justDate=re.findall(r'[\u4e00-\u9fa5]+',newDate)
    print('.', end='')

    #天气
    weatherInfo = re.findall(r'<p class="weather-info.*">(.*)</p>', textInfo)
    print('.', end='')

    #温度
    htemInfo=re.findall(r'var eventDay.*;',textInfo)
    htem=''.join(htemInfo)
    htem=re.findall(r'\d+',htem)
    print('.', end='')


    ltemInfo=re.findall(r'var eventNight.*;',textInfo)
    ltem=''.join(ltemInfo)
    ltem=re.findall(r'\d+',ltem)
    print('.', end='')

    #日出日落
    sunupInfo=re.findall('var sunup.*;',textInfo)
    sunup=''.join(sunupInfo)
    sunup=re.findall(r'\d{2}:\d{2}',sunup)
    sunsetInfo=re.findall('var sunset.*;',textInfo)
    sunset=''.join(sunsetInfo)
    sunset=re.findall(r'\d{2}:\d{2}',sunset)
    print('.', end='')

    #风向
    wind1=re.findall(r'<i class="wind-icon.*title=".*</i>',textInfo)
    wind1=''.join(wind1)
    wind1=re.findall(r'[\u4e00-\u9fa5]+',wind1)
    wind2='转,'.join([i for i in wind1[0:-1:2]])
    wind2=wind2.split(',')
    wind2[-1]=wind2[-1]+"转"
    wind=[]
    j=0
    for i in wind2 :
        wind.append(i+[n for n in wind1[1::2]][j])
        j+=1
    print('.', end='')

    #风力
    strength = re.findall(r'<p class="wind-info.*">[><\d].*</p>', textInfo)
    strength = ''.join(strength)
    t = re.findall('">(\d?[<>-]?\d\w\w?\d?[<>-]?\d?\w?)</p>', strength)
    print('.', end='')
    print('查询完毕\n')
    if justDate[1]=='今天':
        print(justDate[1], '\b天气:', weatherInfo[1], '风向:', wind[1], '风力:', t[1],
              '\n最高温度:', htem[1], '\b度', '最低温度:', ltem[1], '\b度', '\n今日日落时间为：',
              sunset[0], '明日日出时间为：', sunup[0])
    elif justDate[0]=='今天':
        print(justDate[0], '\b天气:', weatherInfo[0], '风向:', wind[0], '风力:', t[0],
              '\n最高温度:', htem[0], '\b度', '最低温度:', ltem[0], '\b度', '\n今日日落时间为：',
              sunset[0], '明日日出时间为：', sunup[0])

    print()


    while True:
        s = input('输入 1 查看历史天气及未来6天天气，2 返回:\n')
        if int(s)==1:
            k=0
            for i in justDate:
                if i =='今天':
                    k+=1
                    continue
                print(justDate[k], '\b天气:', weatherInfo[k], '风向:', wind[k], '风力:', t[k],
                      '\n最高温度:', htem[k], '\b度', '最低温度:', ltem[k], '\b度')
                k+=1
            print()
            print('查询结束')
            print()
            break
        if int(s)==2:
            break
while True:
    choice=input('输入1.查询天气 ， 2.结束程序:\n')
    if choice=='1':
        a=getUrl()
        if a==0:
            getWeather()
    if choice=='2':
        print('程序已结束')
        break

