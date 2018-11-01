# encoding:utf-8
'''
    name: yiouejv
    email: yiouejv@126.com
    data: 2018-10
    introduce: 介绍
    env: python3.5
'''

from apps.front.models import Program
from config import session as db_session


pro1 = Program(
    program_type="python",
    program_content="打印99乘法表",
    program_result="""

    def gen(line_cnt):
        for i in range(1,line_cnt+1):
            for j in range(1,i+1):
                m=i*j
                print '%s*%s=%s\t' %(i,j,m),
            print('')
    if __name__== '__main__':
        gen(9)
""",
)

pro2 = Program(
    program_type="python",
    program_content="求可用被17整除的所有三位数",
    program_result="""

    for num in range(99,1000):
        if num % 17 == 0:
            print(num)

""",
)

pro3 = Program(
    program_type="python",
    program_content="写一个程序，提示输入整数X，然后计算从1到X连续整数的和",
    program_result="""

    sum = 0
    x = int (raw_input ('pls input x: '))
    #输入函数
    for num in range(0,x):
        sum += num
    print(sum)
""",
)

pro4 = Program(
    program_type="python",
    program_content="有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？",
    program_result="""

    cnt = 0
    for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                print(i*100+j*10+k)
                cnt+=1
    print(cnt)

""",
)

pro5 = Program(
    program_type="python",
    program_content="""一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
　　　            找出1000以内的所有完数
""",
program_result = """

	from math import sqrt
	n = int(raw_input('input a number:'))
	sum = n*-1
	k = int(sqrt(n))
	for i in range(1,k+1):
    	    if n%i == 0:
            sum += n/i
            sum += i
        if sum == n:
    	    print 'YES'
	else:
            print 'NO'

""",
)

pro6 = Program(
    program_type="python",
    program_content="""题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元			的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于			40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，			从键盘输入当月利润I，求应发放奖金总数？""",
    program_result="""

	i = int(raw_input('Enter the profit:'))
	arr = [1000000,600000,400000,200000,100000,0]
	rat = [0.01,0.015,0.03,0.05,0.075,0.1]
	r = 0
	for idx in range(0,6):
    	    if i>arr[idx]:
            r+=(i-arr[idx])*rat[idx]
            print (i-arr[idx])*rat[idx]
            i=arr[idx]
        print(r)

""",
)

pro7 = Program(
    program_type="python",
    program_content="一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？",
    program_result="""

	import math
	num = 1
	while True:
    	    if math.sqrt(num + 100)-int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268)-int(math.sqrt(num + 268)) == 0:
                print(num)
                break
            num += 1
""",
)

pro8 = Program(
    program_type="python",
    program_content="输入某年某月某日，判断这一天是这一年的第几天？",
    program_result="""

	import datetime
	import time
	dtstr = str(raw_input('Enter the datetime:(20151215):'))
	dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
	another_dtstr =dtstr[:4] +'0101'
	another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
	print (int((dt-another_dt).days) + 1)

""",
)

pro9 = Program(
    program_type="python",
    program_content="古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问			每个月的兔子总数为多少？",
    program_result="""
	a = 1
	b = 1
	for i in range(1,21,2):
    	    print '%d %d'%(a,b),
    	    a += b
    	    b += a



""",
)

pro10 = Program(
    program_type="python",
    program_content="判断101-200之间有多少个素数，并输出所有素数",
    program_result="""

	#!/usr/bin/python
	#-*- coding:utf-8 -*-
	from math import sqrt 
	def main():
    	    for i in range(101,201):
            flag = 1
            k = int(sqrt(i))
            for j in range(2,k+1):
                if i%j == 0:
                    flag = 0
                    break
            if flag == 1:
                print('%5d'%(i)),

        if __name__ == "__main__":
            main()


""",
)

pro11 = Program(
    program_type="python",
    program_content="题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单				,a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。",
    program_result="""

for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))

""",
)

pro12 = Program(
    program_type="python",
    program_content="打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，			因为153=1的三次方＋5的三次方＋3的三次方",
    program_result="""

	#!/usr/bin/python
	#-*- coding:utf-8 -*-
	def main():
    	    for i in range(100,1000):
            a = i%10
            b = i/100
            c = (int(i/10))%10
            if i == a**3+b**3+c**3:
                print('%5d'%(i)),

        if __name__ == "__main__":
    	    main()


""",
)

pro13 = Program(
    program_type="python",
    program_content="给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字",
    program_result="""

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-

	x = int(raw_input("请输入一个数:\n"))
	a = x / 10000
	b = x % 10000 / 1000
	c = x % 1000 / 100
	d = x % 100 / 10
	e = x % 10

	if a != 0:
    	    print("5 位数：",e,d,c,b,a)
	elif b != 0:
    	    print("4 位数：",e,d,c,b,)
	elif c != 0:
    	    print("3 位数：",e,d,c)
	elif d != 0:
            print("2 位数：",e,d)
	else:
    	    print("1 位数：",e)

""",
)

lst = [
    pro1,
    pro2,
    pro3,
    pro4,
    pro5,
    pro6,
    pro7,
    pro8,
    pro9,
    pro10,
    pro11,
    pro12,
    pro13,
]

for i in lst:
    db_session.add(i)

db_session.commit()
