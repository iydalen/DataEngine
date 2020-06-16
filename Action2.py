import numpy as np
persontype = np.dtype({'names':['name','chinese','math','english'],'formats':['U32','i','i','i']})
people = np.array([("张飞",68,65,30),("关羽",95,76,98),("刘备",98,86,88),("典韦",90,88,77),("许褚",80,90,90)],dtype=persontype)
personname = people['name']
chineses = people['chinese']
maths = people['math']
englishs = people['english']

print('语文平均分：',np.average(chineses))
print('数学平均分：',np.average(maths))
print('英语平均分：',np.average(englishs))
print('------------------------')
print('语文最低分：',np.min(chineses))
print('数学最低分：',np.min(maths))
print('英语最低分：',np.min(englishs))
print('------------------------')
print('语文最高分：',np.max(chineses))
print('数学最高分：',np.max(maths))
print('英语最高分：',np.max(englishs))
print('------------------------')
print('语文成绩的方差：',np.var(chineses))
print('数学成绩的方差：',np.var(maths))
print('英语成绩的方差：',np.var(englishs))
print('------------------------')
print('语文成绩的标准差：',np.std(chineses))
print('数学成绩的标准差：',np.std(maths))
print('英语成绩的标准差：',np.std(englishs))
print('------------------------')
total={}
for i in range(len(people)):
    total[people[i][0]]=people[i][1]+people[i][2]+people[i][3]
total=sorted(total.items(),key=lambda x:x[1] , reverse = True)
print('总成绩排名：')
for i in range(len(total)):
    print("第{}名： {}\t总成绩：{}".format(i+1,total[i][0],total[i][1]))


