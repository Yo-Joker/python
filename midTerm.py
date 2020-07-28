'''
【问题描述】
统计成绩
要求：
1.读取 report.txt 文件中的成绩；
2.统计每名学生总成绩、计算平均并从高到低重新排名；
3.汇总每一科目的平均分和总平均分（见下表第一行）；
4.添加名次，替换60分以下的成绩为“不及格”；
5.将处理后的成绩另存为一个新文件（result.txt）。
'''
def total(l):
    list=l
    a=0
    for i in list[1:]:
        a+=int(i)
    return a

#1.读取 report.txt 文件中的成绩；
with open('report.txt',encoding='utf-8') as f:
    grade=f.readlines()
    n=0
    student = []
    global allstudent
    allstudent = []
    for i in grade:
        grade[n]=grade[n].strip()
        n+=1
    n=0
#2.统计每名学生总成绩、计算平均并从高到低重新排名；
    for j in grade:
        n+=1
        try:
            student=grade[n].split()
            t=total(student)
            student.append(t)
            student.append('%.1f'%(t/9))
            allstudent.append(student)
        except:
            pass
    allstudent.sort(key=lambda x:x[-2],reverse=True)
# 3.汇总每一科目的平均分和总平均分（见下表第一行）；
    m=1
    a=0
    averlist=[]
    try:
        for k in allstudent :
            for l in allstudent :
                a+=float((l[m]))
            averlist.append('%.1f'%(a/len(allstudent)))
            a = 0
            m += 1
    except:
        pass
    averlist.insert(0,'平均')
    averlist.insert(0, '0')
#4.添加名次，替换60分以下的成绩为“不及格”；
    n=0
    for y in allstudent:
        for z in y[1:] :
            if float(z) < 60.0:
                y[y.index(z)]='不及格'
        y.insert(0,n+1)
        n+=1
    allstudent.insert(0,averlist)
#5.将处理后的成绩另存为一个新文件（result.txt）。
    n=0
    for i in allstudent:
        allstudent[n]=' '.join('%s'%j for j in i )
        allstudent[n] += '\n'
        n+=1
    title = grade[0] + ' 总分 平均分\n'
    allstudent.insert(0,title)
with open('result.txt','w',encoding='utf-8') as f2:
    f2.writelines(allstudent)

