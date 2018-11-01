# encoding:utf-8
'''
    name: yiouejv
    email: yiouejv@126.com
    data: 2018-10
    introduce: 介绍
    env: python3.5
'''

from apps.front.models import ShortAnswer
from config import session as db_session


short_answer1 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""为什么学习Python？""",
    short_answer_result="""
	因为python相对其他语言非常优雅简洁,有着丰富的第三方库,很强大、很方便;
	还有就是，python简单易学，生态圈庞大，例如：web开发、爬虫、人工智能等，而且未来发展趋势也很不错。
""",
)

short_answer2 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""
	请至少列举5个 PEP8 规范（越多越好）
	""",
    short_answer_result="""
	#1、空格使用
		a 各种右括号前不要加空格。
		b 逗号、冒号、分号前不要加空格。
		c 函数的左括号前不要加空格。如Func(1)。
		d 序列的左括号前不要加空格。如list[2]。
		e 操作符左右各加一个空格，不要为了对齐增加空格。
		f 函数默认参数使用的赋值符左右省略空格。
		g 不要将多句语句写在同一行，尽管使用‘；’允许。
		if/for/while语句中，即使执行语句只有一句，也必须另起一行。
	#2、代码编排
   		a 缩进，4个空格，而不是tab键
   		b 每行长度79，换行可使用反斜杠，最好使用圆括号。
  		c 类与类之间空两行
  		d 方法之间空一行
""",
)

short_answer3 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""
	ascii、unicode、utf-8、gbk 区别？
	""",
    short_answer_result="""
	#Ascii： 1个字节 支持英文
	#unicode ：所有字符（无论中文、英文等）1个字符：4个字节
	#gbk ： 1个字符，英文1个字节，中文2个字节。
	#utf-8 ：英文1个字节，欧洲字符：2个字节， 亚洲： 3个字节。
""",
)

short_answer4 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""

	xrange和range的区别？
	""",
    short_answer_result="""

	#range产生的是一个列表，xrange产生的是生成器。
	#数据较大时xrange比range好。
	#Range一下把数据都返回，xrange通过yield每次返回一个。	


""",
)

short_answer5 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""
	lambda表达式格式以及应用场景？
	""",
    short_answer_result="""
	# 格式：
    		匿名函数：res = lambda x：i*x   print(res(2))
	# 应用场景：
   		 Filter(),map(),reduce(),sorted()函数中经常用到，它们都需要函数形参数；
   		 一般定义调用一次。
    		（reduce()对参数序列中元素进行累积）
""",
)

short_answer6 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""

	简述Python的深浅拷贝以及应用场景
	""",
    short_answer_result="""

	#浅拷贝：
		不管多么复杂的数据结构，只copy对象最外层本身，该对象引用的其他对象不copy，
		内存里两个变量的地址是一样的，一个改变另一个也改变。
	#深拷贝：
		完全复制原变量的所有数据，内存中生成一套完全一样的内容；只是值一样，内存地址不一样，一方修改另一方不受影响


""",
)

short_answer7 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""

	Python垃圾回收机制？
	""",
    short_answer_result="""

	# Python垃圾回收机制
		Python垃圾回收机制,主要使用'引用计数'来跟踪和回收垃圾。
		在'引用计数'的基础上，通过'标记-清除'（mark and sweep）解决容器对象可能产生的循环引用问题.
		通过'分代回收'以空间换时间的方法提高垃圾回收效率。

	'引用计数'
		PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。
		当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，
		它的ob_refcnt就会减少.引用计数为0时，该对象生命就结束了。
    		\优点:1.简单 2.实时性
    		\缺点:1.维护引用计数消耗资源 2.循环引用

	'标记-清楚机制'
		基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，
		遍历以对象为节点、以引用为边构成的图，把所有可以访问到的对象打上标记，
		然后清扫一遍内存空间，把所有没标记的对象释放。

	'分代技术'
		分代回收的整体思想是：
		将系统中的所有内存块根据其存活时间划分为不同的集合，每个集合就成为一个“代”，
		垃圾收集频率随着“代”的存活时间的增大而减小，存活时间通常利用经过几次垃圾回收来度量。

""",
)

short_answer8 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""

	Python的可变类型和不可变类型？

	""",
    short_answer_result="""

	# 可变类型：列表、字典、集合
	# 不可变类型：数字、字符串、元祖


""",
)

short_answer9 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""

	filter、map、reduce的作用？
	""",
    short_answer_result="""

	# map:遍历序列，为每一个序列进行操作，获取一个新的序列
	# reduce：对于序列里面的所有内容进行累计操作
	# filter：对序列里面的元素进行筛选，最终获取符合条件的序列。


""",
)

short_answer10 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""

	简述 生成器、迭代器、可迭代对象 以及应用场景？
	""",
    short_answer_result="""

	# 装饰器：
		能够在不修改原函数代码的基础上，在执行前后进行定制操作，闭包函数的一种应用
		场景：
  		 	- flask路由系统
   			- flask before_request
   			- csrf
   			- django内置认证
   			- django缓存
	# 手写装饰器；
		import functools
		def wrapper(func):
   			@functools.wraps(func)  #不改变原函数属性
   		def inner(*args, **kwargs):
      			执行函数前
      			return func(*args, **kwargs)
      			执行函数后
   			return inner
		1. 执行wapper函数，并将被装饰的函数当做参数。 wapper(index)
		2. 将第一步的返回值，重新赋值给  新index =  wapper(老index)
		@wrapper    #index=wrapper(index)
		def index(x):
   		return x+100
# ---------------------------------------------------------------
	# 生成器：
		一个函数内部存在yield关键字
	应用场景：
   		- rang/xrange
   		- redis获取值
      		- conn = Redis(......)
       		- v=conn.hscan_iter() # 内部通过yield 来返回值
    		- stark组件中
        	- 前端调用后端的yield
# ---------------------------------------------------------------
	# 迭代器：
		内部有__next__和__iter__方法的对象，帮助我们向后一个一个取值，迭代器不一定是生成器
	应用场景：
   		- wtforms里面对form对象进行循环时，显示form中包含的所有字段
  	 	- 列表、字典、元组
   		（可以让一个对象被for循环）

""",
)

short_answer11 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""

	是否使用过functools中的函数？其作用是什么？
	""",
    short_answer_result="""

在装饰器中，会用到；functools.wraps()主要在装饰器中用来装饰函数

Stark上下文管理源码中，走到视图阶段时有用到functools中的偏函数，request = LocalProxy(partial(_lookup_req_object, 'request'))
""",
)

short_answer12 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""

	如何判断是函数还是方法
	""",
    short_answer_result="""

# 看他的调用者是谁，如果是类，需要传入参数self，这时就是一个函数；
# 如果调用者是对象，不需要传入参数值self，这时是一个方法。
(FunctionType/MethodType)
""",
)

short_answer14 = ShortAnswer(
    short_answer_type="python",
    short_answer_content="""

	什么是反射？以及应用场景？
	""",
    short_answer_result="""

反射就是以字符串的方式导入模块，以字符串的方式执行函数
# 应用场景：
   rest framework里面的CBV
""",
)

l = [
    short_answer1,
    short_answer2,
    short_answer3,
    short_answer4,
    short_answer5,
    short_answer6,
    short_answer7,
    short_answer8,
    short_answer9,
    short_answer10,
    short_answer11,
    short_answer12,
    short_answer14,
]

for i in l:
    db_session.add(i)

db_session.commit()