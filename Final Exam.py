'''
【问题描述】
高级猜数字
制作交互性强、容错率高的猜数字游戏程序。
要求：
为猜数字游戏增加记录玩家成绩的功能，包括玩家用户名、玩的次数、平均猜中的轮数、最少猜中的轮数等；
如果记录里没有玩家输入的用户名，就新建一条记录，否则在原有记录上更新数据；
对玩家输入做检测，判定输入的有效性，并保证程序不会因异常输入而出错；
从网络上获取每一局的答案，请求地址：https://python666.cn/cls/number/guess/
打开文件时，地址使用相对路径
(可选)如果记录文件不存在，就自动创建一个文件，避免程序报错跳出
'''
import requests

#定义用户类
class Player:
    def __init__(self,name,times=0,round=0,minround=0,):
        self.name=name
        self.times=times
        self.round=round
        self.minround=minround

    def records(self,times,minround,round):

        self.round = ((self.round * self.times)+round)/(self.times+1)
        self.times+=times
        self.minround=minround

    def __str__(self):

        return '%s %d %d %.1f\n'\
               %(self.name,self.times,self.minround,self.round)

#函数 创建能更改游戏记录的函数
def createRecord(name,p):
    with open('Records.txt','a+') as f:
        f.seek(0)
        content=f.readlines()
        n=0
        m=1
        for i in content:
            if name in i:
                m=0
                with open('Records.txt','w',encoding='gbk') as f2:
                    f2.writelines(p)
                break
        if m:
            f.seek(2)
            f.write(p)
#函数 检测名字是否已存在，并提取或初始化次数，最小轮数，平均轮数
def checkname(name):
    global ti
    global ro
    ti=0
    ro=0
    aver=0
    with open('Records.txt') as f:
        content=f.readlines()
        n=1
        for i in content:
            if name in i:
                n=0
                l=i.strip().split()
                p.times=int(l[1])
                p.minround=int(l[2])
                p.round=float(l[3])
                print('%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案，开始游戏!'\
                      %(name,p.times,p.minround,p.round))
                break
        if n:
            print('%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案，开始游戏!'\
                  %(name,ti,ro,aver))

#函数 获取url中的随机答案
def getAnswer():
    url='https://python666.cn/cls/number/guess/'
    return requests.get(url).text
#函数 计算最少多少轮
def count(round,min):
    global ro
    ro=round
    if min!=0 and ro>min:
        ro=min

#游戏运行

#检查用户名是否为空
while True :
    name=input('请输入你的名字：')
    if name==''or name==' ':
        print('名字不能为空，请重新输入')
    elif name!=''and name!=' ':
        break

#创建玩家对象
p=Player(name)
#检测名字是否已存在，并提取或初始化次数，最小轮数，平均轮数
checkname(name)

#检测用户输入是否为1-100间的整数
def getp_answer():
    global p_answer
    while True:
        p_answer=input('请猜一个1-100的数字：')
        if p_answer.isdecimal():
            if 1<=int(p_answer)<=100:
                break
            else :
                print('输入数值不符合规定范围，请重新输入')
        elif not p_answer.isdecimal():
            print('输入内容错误，请重新输入一个1-100间的整数！')

#进入猜数字环节
y='y'
while True:
    if y=='y':
        #获取随机答案
        answer=getAnswer()
        #检测答案用print(answer)
        #轮数，次数，正确轮数
        round = 1
        ti=0
        while True :
            getp_answer()
            if p_answer==answer:
                print('猜对了，你一共猜了%d轮'%round)
                ti += 1
                count(round,p.minround)
                #对象记录赋值
                p.records(ti,ro,round)
                #写入记录
                createRecord(name,p.__str__())
                print('%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案'\
                      %(name,p.times,p.minround,p.round))
                y=input('是否继续游戏（输入y继续，其他退出）')
                break

            if p_answer>answer:
                print('猜大了，再试试')
                round+=1

            if p_answer<answer:
                print('猜小了，再试试')
                round+=1

    else:
        print('退出游戏，欢迎下次再来')
        break


