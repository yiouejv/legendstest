# encoding:utf-8
'''
    name: yiouejv
    email: yiouejv@126.com
    data: 2018-10
    introduce: 介绍
    env: python3.5
'''
from config import session as db_session
from apps.front.models import Choice

choice1 = Choice(
    choice_type="python",
    choice_content="(单选题)abs(1.5)输出的结果是？（）",
    choice_option_A="1.5",
    choice_option_B="1",
    choice_option_C="2",
    choice_option_D="以上都不对",
    choice_result="A",
    choice_parse="Python3内置的abs()函数用于取参数的绝对值"
)

choice2 = Choice(
    choice_type="python",
    choice_content="(单选题)下面描述函数覆盖错误的是()",
    choice_option_A="要有子类继承或实现",
    choice_option_B="子类方法与父类方法同名",
    choice_option_C="父类中__开头的私有方法可以被子类覆盖",
    choice_option_D="子类方法与父类方法的调用传参方式要相同",
    choice_result="C",
    choice_parse="私有方法只能在类内部调用，不能被示例对象调用"
)

choice3 = Choice(
    choice_type="python",
    choice_content="(单选题)a = 21 % 2.5，a的值是？（）",
    choice_option_A="1.0",
    choice_option_B="2.0",
    choice_option_C="0",
    choice_option_D="1.5",
    choice_result="A",
    choice_parse = "% 是求余数运算符，21 // 2.5 = 8； 21 – 2.5 * 8 = 1.0"

)
choice4 = Choice(
    choice_type="python",
    choice_content="(单选题)一个数据库包含两个表,分别为 Customer 和 Order.\n"
                   "您执行以下语句:\n"
                   "delete from Order where CustomerID=209;\n"
                   "结果是什么?（）",
    choice_option_A="从 Customer 表中删除 CustomerID为209的记录",
    choice_option_B="从 Order 表中删除 CustomerID为209 的所有记录\n"
                    "并从 Customer 表中删除 CustomerID为209的记录",
    choice_option_C="从 Order 表中删除 CustomerID为209 的第一条记录",
    choice_option_D="从 Order 表中删除 CustomerID为209 的所有记录",
    choice_result="D",
    choice_parse="本题考查delete语句的使用， 无论delete语句中涉及到几张表，删除记录时删除的是delete from后所跟的表名中的相关记录。"
)
choice5 = Choice(
    choice_type="python",
    choice_content="(单选题)下列代码的执行结果是（）\n"
                   "class A():\n"
                   "v = 100\n"
                   "def __init__(self):\n"
                   "self.v = 200\n"
                   "class B(A):\n"
                   "v = 300\n"
                   "def __init__(self):\n"
                   "self.v = 400\n"
                   "super().__init__()\n"
                   "a = B()\n"
                   "print(a.v)",
    choice_option_A="100",
    choice_option_B="200",
    choice_option_C="300",
    choice_option_D="400",
    choice_result="B",
    choice_parse = "子类覆盖版本的__init__方法调用父类的__init__方法，最后对实例变量v赋值的为A类的__init__方法"
)
choice6 = Choice(
    choice_type="python",
    choice_content="(单选题)有字典：d = {'a': 3, 'b': 2, 'c': 1}，以下表达式为True的是？（）",
    choice_option_A="3 in d",
    choice_option_B="('a',3) in d",
    choice_option_C="'b' in d",
    choice_option_D="bool(d.clear())",
    choice_result="C",
    choice_parse = "字典的in操作是判断key是否在字典中存在的。空字典的bool值为False。"

)
choice7 = Choice(
    choice_type="python",
    choice_content="(单选题)如下代码：\n"
                   "a='C:\\newfile\\test.py'\n"
                   "b = len(a)\n"
                   "print(a,b)\n"
                   "输出的结果是？（）",
    choice_option_A="C:\\newfile\\test.py,18",
    choice_option_B="C:\n"
                    "ewfile	est.py 16",
    choice_option_C="C:newfile test.py, 17",
    choice_option_D="以上都不对",
    choice_result="B",
    choice_parse = "如上字符串中 \ 是转义字符，\\n 是换行符、\\t是制表符，在字符串中如果忽略转义字符可以使用ram字符串，在符串前面加r，如：r'C:\\newfile\\test.py'"

)
choice8 = Choice(
    choice_type="python",
    choice_content="(单选题)在Python中，用于实现运行时多态性的是（）",
    choice_option_A="构造方法",
    choice_option_B="覆盖方法",
    choice_option_C="类方法",
    choice_option_D="静态方法",
    choice_result="B",
    choice_parse = "Python通过子类实例方法覆盖父类实例方法，在对象调用方法时优先调用子类的覆盖版本实现多态中的'动态'调用"

)
choice9 = Choice(
    choice_type="python",
    choice_content="(单选题)Python3中有如下代码：\n"
                   "x = [1, 'Two', 3, 'Four']\n"
                   "a = x.sort()\n"
                   "以上代码执行结果是？（）",
    choice_option_A=" [1, 3, 'Four', 'Two']",
    choice_option_B="[1, 'Two', 3, 'Four']",
    choice_option_C="不能执行",
    choice_option_D="以上都不对",
    choice_result="C",
    choice_parse="列表如果使用sort方法，并且key参数默认，则列表中元素类型必须相同。并且sort方法直接修改原列表，返回值为None。"
)
choice10 = Choice(
    choice_type="python",
    choice_content='''(单选题)set({1: "1", 2: "2", 5: "5"})的结果是？（）''',
    choice_option_A="{1, 2, 5}",
    choice_option_B="{'2', '1', '5'}",
    choice_option_C='''{1,"1", 2, "2", 5,"5"}''',
    choice_option_D="以上均不对",
    choice_result="A",
    choice_parse="set使用字典最（作）为参数时，生成字典key的集合。"
)
choice11 = Choice(
    choice_type="python",
    choice_content="(单选题)下列Python3代码能得到 'C:/Programe Files/Python3' 的是？（）",
    choice_option_A=''' A.'/'.join("C:", "Programe Files", "Python3")''',
    choice_option_B=''''/'.join(["C:", "Programe Files", "Python3"])''',
    choice_option_C=''''C:Programe FilesPython3'.split(sep='/')''',
    choice_option_D=''''C:Programe FilesPython3'.split()''',
    choice_result="B",
    choice_parse = "join将可迭代对象用分隔符连接生成新的字符串，split用分隔符拆分字符串，得到字符串列表。"
)
choice12 = Choice(
    choice_type="python",
    choice_content="(单选题)有如下代码：\n"
                   "a = {'one': 1, 'two': 2, 'three': 3}\n"
                   "a['one'] += 1\n"
                   "print(a['one'])\n"
                   "执行结果是？（）",
    choice_option_A="1",
    choice_option_B="2",
    choice_option_C="None",
    choice_option_D="有语法错误不能执行",
    choice_result="B",
    choice_parse="字典可以通过d[key]方式访问字典的值，使用此种方式key要在字典中存在，可以使用d[key]=value方式对字典的key进行赋值或者添加key，value到字典中。"
)

choice13 = Choice(
    choice_type="python",
    choice_content="(单选题)以下能够删除一列的是？（）",
    choice_option_A="alter table students remove age",
    choice_option_B="alter table students drop age",
    choice_option_C="alter table students delete age tinyint unsigned",
    choice_option_D="alter table students drop age tinyint unsigned",
    choice_result="B",
    choice_parse="删除表字段使用关键字drop，且要删除的字段名之后无需给定该字段的数据类型，delete是删除表中相关记录，和字段操作无关。"
)
choice14 = Choice(
    choice_type="python",
    choice_content="(单选题)关于Linux命令以下说法正确的是？（）",
    choice_option_A="cd 命令可以切换工作目录",
    choice_option_B="touch命令只能创建空文件",
    choice_option_C="cp 命令只能在同一个目录下复制文件",
    choice_option_D="mv 命令只能在不同的目录间搬移文件",
    choice_result="A",
    choice_parse="本题考察对cd、touch、cp、mv命令的掌握情况，请参考相关命令手册。"
)
choice15 = Choice(
    choice_type="python",
    choice_content="(单选题)Python3中list(('aaa'))结果是？（）",
    choice_option_A="['aaa']",
    choice_option_B="['a', 'a', 'a']",
    choice_option_C="[a,a,a]",
    choice_option_D="[aaa]",
    choice_result="B",
    choice_parse="列表构造函数list可以由可迭代对象生成列表，本体由字符串生成列表。"
)
choice16 = Choice(
    choice_type="python",
    choice_content="(单选题)普通索引、唯一索引、主键索引的KEY标志分别为？( )",
    choice_option_A="MUL、PRI、UNI",
    choice_option_B="PRI、UNI、MUL",
    choice_option_C="MUL、UNI、PRI",
    choice_option_D="UNI、MUL、PRI",
    choice_result="C",
    choice_parse="普通索引KEY标志：MUL，唯一索引KEY标志：UNI，主键索引KEY标志：PRI。"
)
choice17 = Choice(
    choice_type="python",
    choice_content="(单选题)Linux 系统中 ls 命令的作用，说法不正确的是? （）",
    choice_option_A=" ls 可以查看指定目录的内容",
    choice_option_B="ls 可以查看文件大小",
    choice_option_C="ls 可以查看文件操作权限",
    choice_option_D="ls 可以查看文件内容和修改时间",
    choice_result="D",
    choice_parse="ls 命令可以查看指定目录的内容和文件信息，但不能查看文件内容，查看文本文件内容可以使用cat，more，head，tail等命令或者其他编辑器。"
)
choice18 = Choice(
    choice_type="python",
    choice_content="(单选题)关于Python程序运行方式，以下说法错误的是？（）",
    choice_option_A="Python是解释型语言，运行时需要解释器",
    choice_option_B="Python支持交互模式运行",
    choice_option_C="Python程序可以在命令行执行解释器来解释执行Python程序文件",
    choice_option_D="Python程序不能以脚本方式运行",
    choice_result="D",
    choice_parse="Python语言是支持面向对象思想的解释型计算机编程语言，采用Python语言编写的程序需要Python解释器解释执行。Python程序通常在命令行使用解释器解释执行，同时可以把Python程序做成可执行的Python脚本。Python还支持交互运行模式，这个种模式大大方便了大家完成临时性工作和验证功能代码。"
)
choice19 = Choice(
    choice_type="python",
    choice_content="(单选题)哪条语句会在students表中删除未输入电话号码的行？（）",
    choice_option_A="delete from students where phone is not null",
    choice_option_B="delete from students where phone = “”",
    choice_option_C="delete from students where phone is null",
    choice_option_D="delete from students phone = null",
    choice_result="C",
    choice_parse="NULL为空值，””为空字符串，匹配空值（NULL）必须用 is 或者 is not，而匹配空字符串（””）则用 = 或者 !=。"
)
choice20 = Choice(
    choice_type="python",
    choice_content="(单选题)x = [ x**2 for x in range(1,10) if x % 2 == 1 ]，x的值为？（）",
    choice_option_A="[1, 9, 25, 49, 81]",
    choice_option_B="[2, 6, 10, 14, 18]",
    choice_option_C="[4, 16, 36, 64]",
    choice_option_D="以上都不对",
    choice_result="A",
    choice_parse="本例主要考察列表推导式，本例生成1-10之间（含1）的奇数的平方数构成的列表。"
)
choice21 = Choice(
    choice_type="python",
    choice_content="(单选题)您有一个包含有关您学校中所有学生的信息的表。要更改表中学生的名字,应使用哪个 SQL 关键字?（）",
    choice_option_A="change",
    choice_option_B="update",
    choice_option_C="insert",
    choice_option_D="select",
    choice_result="B",
    choice_parse="change为修改表名，update为更新表记录，insert为插入表记录，select为查询表记录。"
)
choice22 = Choice(
    choice_type="python",
    choice_content="(单选题)下面关于进程和线程的描述错误的是（）",
    choice_option_A="进程和线程都是多任务编程的机制",
    choice_option_B="进程线程都能够使用计算机多核",
    choice_option_C="线程运行不消耗计算机资源",
    choice_option_D="一个进程可以包含多个线程",
    choice_result="C",
    choice_parse="A B D 均为进程线程的特征，C中线程创建消耗资源较少，但是无论创建和运行都是需要消耗计算机资源的"
)
choice23 = Choice(
    choice_type="python",
    choice_content="(单选题)mysql中的约束不包括？（）",
    choice_option_A="检查约束",
    choice_option_B="默认约束",
    choice_option_C="非空约束",
    choice_option_D="唯一约束",
    choice_result="A",
    choice_parse="MySQL中的约束有默认约束、非空约束、唯一约束、主键约束、外键约束，不包含检查约束。"
)
choice24 = Choice(
    choice_type="python",
    choice_content="下面关于孤儿进程和僵尸进程的描述错误的是（）",
    choice_option_A="孤儿进程是父进程退出后子进程还在运行就会变为孤儿进程",
    choice_option_B="僵尸进程是子进程退出后父进程没有处理子进程退出状态子进程就会成为僵尸",
    choice_option_C="孤儿进程对系统是有危害的",
    choice_option_D="僵尸进程对系统是有危害的",
    choice_result="C",
    choice_parse="A B 是对僵尸进程和孤儿进程产生原因的描述，C中孤儿进程会被专门的进程收养不会对系统产生危害，D中大量的僵尸进程会占用系统资源，所以应该尽量避免僵尸进程产生"
)

db_session.add(choice1)
db_session.add(choice2)
db_session.add(choice3)
db_session.add(choice4)
db_session.add(choice5)
db_session.add(choice6)
db_session.add(choice7)
db_session.add(choice8)
db_session.add(choice9)
db_session.add(choice10)
db_session.add(choice11)
db_session.add(choice12)
db_session.add(choice13)
db_session.add(choice14)
db_session.add(choice15)
db_session.add(choice16)
db_session.add(choice17)
db_session.add(choice18)
db_session.add(choice19)
db_session.add(choice20)
db_session.add(choice21)
db_session.add(choice22)
db_session.add(choice23)
db_session.add(choice24)

db_session.commit()
