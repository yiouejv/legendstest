# Host: localhost  (Version 5.7.20-log)
# Date: 2018-11-02 13:25:28
# Generator: MySQL-Front 5.4  (Build 4.153) - http://www.mysqlfront.de/

/*!40101 SET NAMES utf8 */;

#
# Structure for table "admin"
#

DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `admin_uuid` varchar(50) NOT NULL,
  `admin_name` varchar(50) NOT NULL,
  `admin_email` varchar(50) DEFAULT NULL,
  `_admin_password` varchar(100) NOT NULL,
  `admin_phone` varchar(11) NOT NULL,
  `admin_is_super` tinyint(1) DEFAULT NULL,
  `admin_is_delete` tinyint(1) DEFAULT NULL,
  `admin_create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`admin_uuid`),
  UNIQUE KEY `admin_phone` (`admin_phone`),
  UNIQUE KEY `admin_email` (`admin_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "admin"
#

INSERT INTO `admin` VALUES ('2c6ac51a-81f4-4a45-a33e-a6d48eb10de4','秦尚智','qin@126.com','pbkdf2:sha256:50000$o0ZZxofc$386ad6361523b6c3be13f13ebc6cb76328eb3cc867f5eb45e12e9a1362086959','18899996666',0,0,'2018-11-02 12:57:16'),('3d1be82e-7d0e-48ce-a92a-2172db83755b','yang','yiouejv@126.com','pbkdf2:sha256:50000$qKKrDxAI$8ad21a5063dae5b453c707126f4d7fa4e613d880c5f5be25273cd02d701a6660','15210212773',1,0,'2018-10-28 22:03:37');

#
# Structure for table "choice"
#

DROP TABLE IF EXISTS `choice`;
CREATE TABLE `choice` (
  `choice_id` int(11) NOT NULL AUTO_INCREMENT,
  `choice_type` varchar(50) DEFAULT NULL,
  `choice_content` text NOT NULL,
  `choice_option_A` text NOT NULL,
  `choice_option_B` text NOT NULL,
  `choice_option_C` text NOT NULL,
  `choice_option_D` text NOT NULL,
  `choice_result` varchar(1) NOT NULL,
  `choice_parse` varchar(500) DEFAULT NULL,
  `short_answer_create_time` datetime DEFAULT NULL,
  `short_answer_update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`choice_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

#
# Data for table "choice"
#

INSERT INTO `choice` VALUES (1,'python','题目','1.5','1','2','以上都不对','A','Python3内置的abs()函数用于取参数的绝对值','2018-10-28 22:04:13','2018-10-28 22:04:13'),(2,'python','(单选题)下面描述函数覆盖错误的是()','要有子类继承或实现','子类方法与父类方法同名','父类中__开头的私有方法可以被子类覆盖','子类方法与父类方法的调用传参方式要相同','C','私有方法只能在类内部调用，不能被示例对象调用','2018-10-28 22:04:13','2018-10-28 22:04:13'),(3,'python','(单选题)a = 21 % 2.5，a的值是？（）','1.0','2.0','0','1.5','A','% 是求余数运算符，21 // 2.5 = 8； 21 – 2.5 * 8 = 1.0','2018-10-28 22:04:13','2018-10-28 22:04:13'),(4,'python','(单选题)一个数据库包含两个表,分别为 Customer 和 Order.\n您执行以下语句:\ndelete from Order where CustomerID=209;\n结果是什么?（）','从 Customer 表中删除 CustomerID为209的记录','从 Order 表中删除 CustomerID为209 的所有记录\n并从 Customer 表中删除 CustomerID为209的记录','从 Order 表中删除 CustomerID为209 的第一条记录','从 Order 表中删除 CustomerID为209 的所有记录','D','本题考查delete语句的使用， 无论delete语句中涉及到几张表，删除记录时删除的是delete from后所跟的表名中的相关记录。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(5,'python','(单选题)下列代码的执行结果是（）\nclass A():\nv = 100\ndef __init__(self):\nself.v = 200\nclass B(A):\nv = 300\ndef __init__(self):\nself.v = 400\nsuper().__init__()\na = B()\nprint(a.v)','100','200','300','400','B','子类覆盖版本的__init__方法调用父类的__init__方法，最后对实例变量v赋值的为A类的__init__方法','2018-10-28 22:04:13','2018-10-28 22:04:13'),(6,'python','(单选题)有字典：d = {\'a\': 3, \'b\': 2, \'c\': 1}，以下表达式为True的是？（）','3 in d','(\'a\',3) in d','\'b\' in d','bool(d.clear())','C','字典的in操作是判断key是否在字典中存在的。空字典的bool值为False。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(7,'python','(单选题)如下代码：\na=\'C:\\newfile\\test.py\'\nb = len(a)\nprint(a,b)\n输出的结果是？（）','C:\\newfile\\test.py,18','C:\newfile\test.py 16','C:newfile test.py, 17','以上都不对','B','如上字符串中 \\ 是转义字符，\\n 是换行符、\\t是制表符，在字符串中如果忽略转义字符可以使用ram字符串，在符串前面加r，如：r\'C:\\newfile\\test.py\'','2018-10-28 22:04:13','2018-10-28 22:04:13'),(8,'python','(单选题)在Python中，用于实现运行时多态性的是（）','构造方法','覆盖方法','类方法','静态方法','B','Python通过子类实例方法覆盖父类实例方法，在对象调用方法时优先调用子类的覆盖版本实现多态中的\'动态\'调用','2018-10-28 22:04:13','2018-10-28 22:04:13'),(9,'python','(单选题)Python3中有如下代码：\nx = [1, \'Two\', 3, \'Four\']\na = x.sort()\n以上代码执行结果是？（）',' [1, 3, \'Four\', \'Two\']','[1, \'Two\', 3, \'Four\']','不能执行','以上都不对','C','列表如果使用sort方法，并且key参数默认，则列表中元素类型必须相同。并且sort方法直接修改原列表，返回值为None。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(10,'python','(单选题)set({1: \"1\", 2: \"2\", 5: \"5\"})的结果是？（）','{1, 2, 5}','{\'2\', \'1\', \'5\'}','{1,\"1\", 2, \"2\", 5,\"5\"}','以上均不对','A','set使用字典最（作）为参数时，生成字典key的集合。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(11,'python','(单选题)下列Python3代码能得到 \'C:/Programe Files/Python3\' 的是？（）',' A.\'/\'.join(\"C:\", \"Programe Files\", \"Python3\")','\'/\'.join([\"C:\", \"Programe Files\", \"Python3\"])','\'C:Programe FilesPython3\'.split(sep=\'/\')','\'C:Programe FilesPython3\'.split()','B','join将可迭代对象用分隔符连接生成新的字符串，split用分隔符拆分字符串，得到字符串列表。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(12,'python','(单选题)有如下代码：\na = {\'one\': 1, \'two\': 2, \'three\': 3}\na[\'one\'] += 1\nprint(a[\'one\'])\n执行结果是？（）','1','2','None','有语法错误不能执行','B','字典可以通过d[key]方式访问字典的值，使用此种方式key要在字典中存在，可以使用d[key]=value方式对字典的key进行赋值或者添加key，value到字典中。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(13,'python','(单选题)以下能够删除一列的是？（）','alter table students remove age','alter table students drop age','alter table students delete age tinyint unsigned','alter table students drop age tinyint unsigned','B','删除表字段使用关键字drop，且要删除的字段名之后无需给定该字段的数据类型，delete是删除表中相关记录，和字段操作无关。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(14,'python','(单选题)关于Linux命令以下说法正确的是？（）','cd 命令可以切换工作目录','touch命令只能创建空文件','cp 命令只能在同一个目录下复制文件','mv 命令只能在不同的目录间搬移文件','A','本题考察对cd、touch、cp、mv命令的掌握情况，请参考相关命令手册。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(15,'python','(单选题)Python3中list((\'aaa\'))结果是？（）','[\'aaa\']','[\'a\', \'a\', \'a\']','[a,a,a]','[aaa]','B','列表构造函数list可以由可迭代对象生成列表，本体由字符串生成列表。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(16,'python','(单选题)普通索引、唯一索引、主键索引的KEY标志分别为？( )','MUL、PRI、UNI','PRI、UNI、MUL','MUL、UNI、PRI','UNI、MUL、PRI','C','普通索引KEY标志：MUL，唯一索引KEY标志：UNI，主键索引KEY标志：PRI。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(17,'python','(单选题)Linux 系统中 ls 命令的作用，说法不正确的是? （）',' ls 可以查看指定目录的内容','ls 可以查看文件大小','ls 可以查看文件操作权限','ls 可以查看文件内容和修改时间','D','ls 命令可以查看指定目录的内容和文件信息，但不能查看文件内容，查看文本文件内容可以使用cat，more，head，tail等命令或者其他编辑器。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(18,'python','(单选题)关于Python程序运行方式，以下说法错误的是？（）','Python是解释型语言，运行时需要解释器','Python支持交互模式运行','Python程序可以在命令行执行解释器来解释执行Python程序文件','Python程序不能以脚本方式运行','D','Python语言是支持面向对象思想的解释型计算机编程语言，采用Python语言编写的程序需要Python解释器解释执行。Python程序通常在命令行使用解释器解释执行，同时可以把Python程序做成可执行的Python脚本。Python还支持交互运行模式，这个种模式大大方便了大家完成临时性工作和验证功能代码。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(19,'python','(单选题)哪条语句会在students表中删除未输入电话号码的行？（）','delete from students where phone is not null','delete from students where phone = “”','delete from students where phone is null','delete from students phone = null','C','NULL为空值，””为空字符串，匹配空值（NULL）必须用 is 或者 is not，而匹配空字符串（””）则用 = 或者 !=。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(20,'python','(单选题)x = [ x**2 for x in range(1,10) if x % 2 == 1 ]，x的值为？（）','[1, 9, 25, 49, 81]','[2, 6, 10, 14, 18]','[4, 16, 36, 64]','以上都不对','A','本例主要考察列表推导式，本例生成1-10之间（含1）的奇数的平方数构成的列表。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(21,'python','(单选题)您有一个包含有关您学校中所有学生的信息的表。要更改表中学生的名字,应使用哪个 SQL 关键字?（）','change','update','insert','select','B','change为修改表名，update为更新表记录，insert为插入表记录，select为查询表记录。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(22,'python','(单选题)下面关于进程和线程的描述错误的是（）','进程和线程都是多任务编程的机制','进程线程都能够使用计算机多核','线程运行不消耗计算机资源','一个进程可以包含多个线程','C','A B D 均为进程线程的特征，C中线程创建消耗资源较少，但是无论创建和运行都是需要消耗计算机资源的','2018-10-28 22:04:13','2018-10-28 22:04:13'),(23,'python','(单选题)mysql中的约束不包括？（）','检查约束','默认约束','非空约束','唯一约束','A','MySQL中的约束有默认约束、非空约束、唯一约束、主键约束、外键约束，不包含检查约束。','2018-10-28 22:04:13','2018-10-28 22:04:13'),(24,'python','下面关于孤儿进程和僵尸进程的描述错误的是（）','孤儿进程是父进程退出后子进程还在运行就会变为孤儿进程','僵尸进程是子进程退出后父进程没有处理子进程退出状态子进程就会成为僵尸','孤儿进程对系统是有危害的','僵尸进程对系统是有危害的','C','A B 是对僵尸进程和孤儿进程产生原因的描述，C中孤儿进程会被专门的进程收养不会对系统产生危害，D中大量的僵尸进程会占用系统资源，所以应该尽量避免僵尸进程产生','2018-10-28 22:04:13','2018-10-28 22:04:13');

#
# Structure for table "class"
#

DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `class_id` int(11) NOT NULL AUTO_INCREMENT,
  `class_name` varchar(50) NOT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

#
# Data for table "class"
#

INSERT INTO `class` VALUES (1,'AID1087'),(2,'AID1807'),(3,'AID1808'),(4,'AID1807'),(5,'AID1808'),(6,'AID1809'),(7,'AID1708'),(8,'AID1709'),(9,'AID1710'),(10,'AID1711'),(11,'AID1810'),(12,'AID1811'),(13,'AID1812'),(14,'AID1712'),(15,'AID1807'),(16,'AID1807'),(17,'AID1807'),(21,'AID1807'),(22,'AID1807'),(23,'AID1808'),(24,'AID1710');

#
# Structure for table "program"
#

DROP TABLE IF EXISTS `program`;
CREATE TABLE `program` (
  `program_id` int(11) NOT NULL AUTO_INCREMENT,
  `program_type` varchar(50) DEFAULT NULL,
  `program_content` text NOT NULL,
  `program_result` text NOT NULL,
  `program_create_time` datetime DEFAULT NULL,
  `program_update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`program_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

#
# Data for table "program"
#

INSERT INTO `program` VALUES (1,'python','打印99乘法表','\n\n    def gen(line_cnt):\n        for i in range(1,line_cnt+1):\n            for j in range(1,i+1):\n                m=i*j\n                print \'%s*%s=%s\t\' %(i,j,m),\n            print(\'\')\n    if __name__== \'__main__\':\n        gen(9)\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(2,'python','求可用被17整除的所有三位数','\n\n    for num in range(99,1000):\n        if num % 17 == 0:\n            print(num)\n\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(3,'python','写一个程序，提示输入整数X，然后计算从1到X连续整数的和','\n\n    sum = 0\n    x = int (raw_input (\'pls input x: \'))\n    #输入函数\n    for num in range(0,x):\n        sum += num\n    print(sum)\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(4,'python','有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？','\n\n    cnt = 0\n    for i in range(1,5):\n    for j in range(1,5):\n        for k in range(1,5):\n            if i!=j and i!=k and j!=k:\n                print(i*100+j*10+k)\n                cnt+=1\n    print(cnt)\n\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(5,'python','一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程\n　　　            找出1000以内的所有完数\n','\n\n\tfrom math import sqrt\n\tn = int(raw_input(\'input a number:\'))\n\tsum = n*-1\n\tk = int(sqrt(n))\n\tfor i in range(1,k+1):\n    \t    if n%i == 0:\n            sum += n/i\n            sum += i\n        if sum == n:\n    \t    print \'YES\'\n\telse:\n            print \'NO\'\n\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(6,'python','题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元\t\t\t的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于\t\t\t40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，\t\t\t从键盘输入当月利润I，求应发放奖金总数？','\n\n\ti = int(raw_input(\'Enter the profit:\'))\n\tarr = [1000000,600000,400000,200000,100000,0]\n\trat = [0.01,0.015,0.03,0.05,0.075,0.1]\n\tr = 0\n\tfor idx in range(0,6):\n    \t    if i>arr[idx]:\n            r+=(i-arr[idx])*rat[idx]\n            print (i-arr[idx])*rat[idx]\n            i=arr[idx]\n        print(r)\n\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(7,'python','一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？','\n\n\timport math\n\tnum = 1\n\twhile True:\n    \t    if math.sqrt(num + 100)-int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268)-int(math.sqrt(num + 268)) == 0:\n                print(num)\n                break\n            num += 1\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(8,'python','输入某年某月某日，判断这一天是这一年的第几天？','\n\n\timport datetime\n\timport time\n\tdtstr = str(raw_input(\'Enter the datetime:(20151215):\'))\n\tdt = datetime.datetime.strptime(dtstr, \"%Y%m%d\")\n\tanother_dtstr =dtstr[:4] +\'0101\'\n\tanother_dt = datetime.datetime.strptime(another_dtstr, \"%Y%m%d\")\n\tprint (int((dt-another_dt).days) + 1)\n\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(9,'python','古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问\t\t\t每个月的兔子总数为多少？','\n\ta = 1\n\tb = 1\n\tfor i in range(1,21,2):\n    \t    print \'%d %d\'%(a,b),\n    \t    a += b\n    \t    b += a\n\n\n\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(10,'python','判断101-200之间有多少个素数，并输出所有素数','\n\n\t#!/usr/bin/python\n\t#-*- coding:utf-8 -*-\n\tfrom math import sqrt \n\tdef main():\n    \t    for i in range(101,201):\n            flag = 1\n            k = int(sqrt(i))\n            for j in range(2,k+1):\n                if i%j == 0:\n                    flag = 0\n                    break\n            if flag == 1:\n                print(\'%5d\'%(i)),\n\n        if __name__ == \"__main__\":\n            main()\n\n\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(11,'python','题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单\t\t\t\t,a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。','\n\nfor i in range(ord(\'x\'),ord(\'z\') + 1):\n    for j in range(ord(\'x\'),ord(\'z\') + 1):\n        if i != j:\n            for k in range(ord(\'x\'),ord(\'z\') + 1):\n                if (i != k) and (j != k):\n                    if (i != ord(\'x\')) and (k != ord(\'x\')) and (k != ord(\'z\')):\n                        print(\'order is a -- %s\t b -- %s\tc--%s\' % (chr(i),chr(j),chr(k)))\n\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(12,'python','打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，\t\t\t因为153=1的三次方＋5的三次方＋3的三次方','\n\n\t#!/usr/bin/python\n\t#-*- coding:utf-8 -*-\n\tdef main():\n    \t    for i in range(100,1000):\n            a = i%10\n            b = i/100\n            c = (int(i/10))%10\n            if i == a**3+b**3+c**3:\n                print(\'%5d\'%(i)),\n\n        if __name__ == \"__main__\":\n    \t    main()\n\n\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(13,'python','给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字','\n\n\t#!/usr/bin/python\n\t# -*- coding: UTF-8 -*-\n\n\tx = int(raw_input(\"请输入一个数:\n\"))\n\ta = x / 10000\n\tb = x % 10000 / 1000\n\tc = x % 1000 / 100\n\td = x % 100 / 10\n\te = x % 10\n\n\tif a != 0:\n    \t    print(\"5 位数：\",e,d,c,b,a)\n\telif b != 0:\n    \t    print(\"4 位数：\",e,d,c,b,)\n\telif c != 0:\n    \t    print(\"3 位数：\",e,d,c)\n\telif d != 0:\n            print(\"2 位数：\",e,d)\n\telse:\n    \t    print(\"1 位数：\",e)\n\n','2018-10-28 22:03:53','2018-10-28 22:03:53'),(14,'python','sdfs','asda','2018-10-30 08:57:25','2018-10-30 08:57:25');

#
# Structure for table "short_answer"
#

DROP TABLE IF EXISTS `short_answer`;
CREATE TABLE `short_answer` (
  `short_answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `short_answer_type` varchar(50) DEFAULT NULL,
  `short_answer_content` text NOT NULL,
  `short_answer_result` text NOT NULL,
  `short_answer_create_time` datetime DEFAULT NULL,
  `short_answer_update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`short_answer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

#
# Data for table "short_answer"
#

INSERT INTO `short_answer` VALUES (1,'python','为什么学习Python？','\n\t因为python相对其他语言非常优雅简洁,有着丰富的第三方库,很强大、很方便;\n\t还有就是，python简单易学，生态圈庞大，例如：web开发、爬虫、人工智能等，而且未来发展趋势也很不错。\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(2,'python','\t请至少列举5个 PEP8 规范（越多越好)','\n\t#1、空格使用\n\t\ta 各种右括号前不要加空格。\n\t\tb 逗号、冒号、分号前不要加空格。\n\t\tc 函数的左括号前不要加空格。如Func(1)。\n\t\td 序列的左括号前不要加空格。如list[2]。\n\t\te 操作符左右各加一个空格，不要为了对齐增加空格。\n\t\tf 函数默认参数使用的赋值符左右省略空格。\n\t\tg 不要将多句语句写在同一行，尽管使用‘；’允许。\n\t\tif/for/while语句中，即使执行语句只有一句，也必须另起一行。\n\t#2、代码编排\n   \t\ta 缩进，4个空格，而不是tab键\n   \t\tb 每行长度79，换行可使用反斜杠，最好使用圆括号。\n  \t\tc 类与类之间空两行\n  \t\td 方法之间空一行\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(3,'python','\n\tascii、unicode、utf-8、gbk 区别？\n\t','\n\t#Ascii： 1个字节 支持英文\n\t#unicode ：所有字符（无论中文、英文等）1个字符：4个字节\n\t#gbk ： 1个字符，英文1个字节，中文2个字节。\n\t#utf-8 ：英文1个字节，欧洲字符：2个字节， 亚洲： 3个字节。\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(4,'python','\n\n\txrange和range的区别？\n\t','\n\n\t#range产生的是一个列表，xrange产生的是生成器。\n\t#数据较大时xrange比range好。\n\t#Range一下把数据都返回，xrange通过yield每次返回一个。\t\n\n\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(5,'python','\n\tlambda表达式格式以及应用场景？\n\t','\n\t# 格式：\n    \t\t匿名函数：res = lambda x：i*x   print(res(2))\n\t# 应用场景：\n   \t\t Filter(),map(),reduce(),sorted()函数中经常用到，它们都需要函数形参数；\n   \t\t 一般定义调用一次。\n    \t\t（reduce()对参数序列中元素进行累积）\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(6,'python','\n\n\t简述Python的深浅拷贝以及应用场景\n\t','\n\n\t#浅拷贝：\n\t\t不管多么复杂的数据结构，只copy对象最外层本身，该对象引用的其他对象不copy，\n\t\t内存里两个变量的地址是一样的，一个改变另一个也改变。\n\t#深拷贝：\n\t\t完全复制原变量的所有数据，内存中生成一套完全一样的内容；只是值一样，内存地址不一样，一方修改另一方不受影响\n\n\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(7,'python','\n\n\tPython垃圾回收机制？\n\t','\n\n\t# Python垃圾回收机制\n\t\tPython垃圾回收机制,主要使用\'引用计数\'来跟踪和回收垃圾。\n\t\t在\'引用计数\'的基础上，通过\'标记-清除\'（mark and sweep）解决容器对象可能产生的循环引用问题.\n\t\t通过\'分代回收\'以空间换时间的方法提高垃圾回收效率。\n\n\t\'引用计数\'\n\t\tPyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。\n\t\t当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，\n\t\t它的ob_refcnt就会减少.引用计数为0时，该对象生命就结束了。\n    \t\t\\优点:1.简单 2.实时性\n    \t\t\\缺点:1.维护引用计数消耗资源 2.循环引用\n\n\t\'标记-清楚机制\'\n\t\t基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，\n\t\t遍历以对象为节点、以引用为边构成的图，把所有可以访问到的对象打上标记，\n\t\t然后清扫一遍内存空间，把所有没标记的对象释放。\n\n\t\'分代技术\'\n\t\t分代回收的整体思想是：\n\t\t将系统中的所有内存块根据其存活时间划分为不同的集合，每个集合就成为一个“代”，\n\t\t垃圾收集频率随着“代”的存活时间的增大而减小，存活时间通常利用经过几次垃圾回收来度量。\n\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(8,'python','\n\n\tPython的可变类型和不可变类型？\n\n\t','\n\n\t# 可变类型：列表、字典、集合\n\t# 不可变类型：数字、字符串、元祖\n\n\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(9,'python','\n\n\tfilter、map、reduce的作用？\n\t','\n\n\t# map:遍历序列，为每一个序列进行操作，获取一个新的序列\n\t# reduce：对于序列里面的所有内容进行累计操作\n\t# filter：对序列里面的元素进行筛选，最终获取符合条件的序列。\n\n\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(10,'python','\n\n\t简述 生成器、迭代器、可迭代对象 以及应用场景？\n\t','\n\n\t# 装饰器：\n\t\t能够在不修改原函数代码的基础上，在执行前后进行定制操作，闭包函数的一种应用\n\t\t场景：\n  \t\t \t- flask路由系统\n   \t\t\t- flask before_request\n   \t\t\t- csrf\n   \t\t\t- django内置认证\n   \t\t\t- django缓存\n\t# 手写装饰器；\n\t\timport functools\n\t\tdef wrapper(func):\n   \t\t\t@functools.wraps(func)  #不改变原函数属性\n   \t\tdef inner(*args, **kwargs):\n      \t\t\t执行函数前\n      \t\t\treturn func(*args, **kwargs)\n      \t\t\t执行函数后\n   \t\t\treturn inner\n\t\t1. 执行wapper函数，并将被装饰的函数当做参数。 wapper(index)\n\t\t2. 将第一步的返回值，重新赋值给  新index =  wapper(老index)\n\t\t@wrapper    #index=wrapper(index)\n\t\tdef index(x):\n   \t\treturn x+100\n# ---------------------------------------------------------------\n\t# 生成器：\n\t\t一个函数内部存在yield关键字\n\t应用场景：\n   \t\t- rang/xrange\n   \t\t- redis获取值\n      \t\t- conn = Redis(......)\n       \t\t- v=conn.hscan_iter() # 内部通过yield 来返回值\n    \t\t- stark组件中\n        \t- 前端调用后端的yield\n# ---------------------------------------------------------------\n\t# 迭代器：\n\t\t内部有__next__和__iter__方法的对象，帮助我们向后一个一个取值，迭代器不一定是生成器\n\t应用场景：\n   \t\t- wtforms里面对form对象进行循环时，显示form中包含的所有字段\n  \t \t- 列表、字典、元组\n   \t\t（可以让一个对象被for循环）\n\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(11,'python','\n\n\t是否使用过functools中的函数？其作用是什么？\n\t','\n\n在装饰器中，会用到；functools.wraps()主要在装饰器中用来装饰函数\n\nStark上下文管理源码中，走到视图阶段时有用到functools中的偏函数，request = LocalProxy(partial(_lookup_req_object, \'request\'))\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(12,'python','\n\n\t如何判断是函数还是方法\n\t','\n\n# 看他的调用者是谁，如果是类，需要传入参数self，这时就是一个函数；\n# 如果调用者是对象，不需要传入参数值self，这时是一个方法。\n(FunctionType/MethodType)\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(13,'python','\n\n\t什么是反射？以及应用场景？\n\t','\n\n反射就是以字符串的方式导入模块，以字符串的方式执行函数\n# 应用场景：\n   rest framework里面的CBV\n','2018-10-28 22:04:03','2018-10-28 22:04:03'),(14,'python','aaa','','2018-10-30 08:56:15','2018-10-30 08:56:15'),(15,'python','dasdas','dsadasd','2018-10-30 08:57:03','2018-10-30 08:57:03');

#
# Structure for table "student_choice_result"
#

DROP TABLE IF EXISTS `student_choice_result`;
CREATE TABLE `student_choice_result` (
  `student_choice_result_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_choice_result_student_id` int(11) NOT NULL,
  `student_choice_result_test_pager_id` int(11) NOT NULL,
  `student_choice_result_choice_id` int(11) NOT NULL,
  `student_choice_result_student_choice_result` varchar(1) NOT NULL,
  `student_choice_result_choice_result` varchar(1) NOT NULL,
  `student_choice_result_choice_score` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`student_choice_result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

#
# Data for table "student_choice_result"
#

INSERT INTO `student_choice_result` VALUES (1,3,1,4,'C','D','0'),(2,3,1,8,'B','B','1'),(3,3,1,12,'B','B','1'),(4,3,1,16,'C','C','1'),(5,3,2,4,'D','D','1'),(6,3,2,8,'B','B','1'),(7,3,2,12,'B','B','1'),(8,3,2,16,'C','C','1'),(9,5,1,4,'C','D','0'),(10,5,1,8,'B','B','1'),(11,5,1,12,'B','B','1'),(12,5,1,16,'C','C','1'),(13,5,3,1,'A','A','4'),(14,5,3,4,'D','D','4'),(15,5,3,5,'B','B','4'),(16,5,3,8,'B','B','4'),(17,5,3,9,'C','C','4'),(18,5,3,12,'B','B','4'),(19,5,3,13,'A','B','0'),(20,5,3,16,'C','C','4'),(21,5,3,20,'A','A','4'),(22,5,3,24,'C','C','4'),(23,4,1,4,'D','D','1'),(24,4,1,8,'C','B','0'),(25,4,1,12,'D','B','0'),(26,4,1,16,'A','C','0'),(27,2,4,4,'D','D','1');

#
# Structure for table "student_program_result"
#

DROP TABLE IF EXISTS `student_program_result`;
CREATE TABLE `student_program_result` (
  `student_program_result_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_program_student_id` int(11) NOT NULL,
  `student_program__test_pager_id` int(11) NOT NULL,
  `student_program_program_id` int(11) NOT NULL,
  `student_program_student_result` varchar(500) NOT NULL,
  `student_program_result` varchar(500) NOT NULL,
  `student_program_score` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`student_program_result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

#
# Data for table "student_program_result"
#

INSERT INTO `student_program_result` VALUES (1,3,1,4,'xxx','\n\n    cnt = 0\n    for i in range(1,5):\n    for j in range(1,5):\n        for k in range(1,5):\n            if i!=j and i!=k and j!=k:\n                print(i*100+j*10+k)\n                cnt+=1\n    print(cnt)\n\n','0'),(2,3,2,4,'xxx','\n\n    cnt = 0\n    for i in range(1,5):\n    for j in range(1,5):\n        for k in range(1,5):\n            if i!=j and i!=k and j!=k:\n                print(i*100+j*10+k)\n                cnt+=1\n    print(cnt)\n\n','0'),(3,5,1,4,'bbb','\n\n    cnt = 0\n    for i in range(1,5):\n    for j in range(1,5):\n        for k in range(1,5):\n            if i!=j and i!=k and j!=k:\n                print(i*100+j*10+k)\n                cnt+=1\n    print(cnt)\n\n','0'),(4,5,3,1,'ccc','\n\n    def gen(line_cnt):\n        for i in range(1,line_cnt+1):\n            for j in range(1,i+1):\n                m=i*j\n                print \'%s*%s=%s\t\' %(i,j,m),\n            print(\'\')\n    if __name__== \'__main__\':\n        gen(9)\n','0'),(5,5,3,4,'ddd','\n\n    cnt = 0\n    for i in range(1,5):\n    for j in range(1,5):\n        for k in range(1,5):\n            if i!=j and i!=k and j!=k:\n                print(i*100+j*10+k)\n                cnt+=1\n    print(cnt)\n\n','0'),(6,5,3,5,'eee','\n\n\tfrom math import sqrt\n\tn = int(raw_input(\'input a number:\'))\n\tsum = n*-1\n\tk = int(sqrt(n))\n\tfor i in range(1,k+1):\n    \t    if n%i == 0:\n            sum += n/i\n            sum += i\n        if sum == n:\n    \t    print \'YES\'\n\telse:\n            print \'NO\'\n\n','0'),(7,5,3,8,'fff','\n\n\timport datetime\n\timport time\n\tdtstr = str(raw_input(\'Enter the datetime:(20151215):\'))\n\tdt = datetime.datetime.strptime(dtstr, \"%Y%m%d\")\n\tanother_dtstr =dtstr[:4] +\'0101\'\n\tanother_dt = datetime.datetime.strptime(another_dtstr, \"%Y%m%d\")\n\tprint (int((dt-another_dt).days) + 1)\n\n','0'),(8,5,3,12,'ggg','\n\n\t#!/usr/bin/python\n\t#-*- coding:utf-8 -*-\n\tdef main():\n    \t    for i in range(100,1000):\n            a = i%10\n            b = i/100\n            c = (int(i/10))%10\n            if i == a**3+b**3+c**3:\n                print(\'%5d\'%(i)),\n\n        if __name__ == \"__main__\":\n    \t    main()\n\n\n','0'),(9,4,1,4,'bbbbbbbbb','\n\n    cnt = 0\n    for i in range(1,5):\n    for j in range(1,5):\n        for k in range(1,5):\n            if i!=j and i!=k and j!=k:\n                print(i*100+j*10+k)\n                cnt+=1\n    print(cnt)\n\n','1'),(10,2,4,4,'eee','\n\n    cnt = 0\n    for i in range(1,5):\n    for j in range(1,5):\n        for k in range(1,5):\n            if i!=j and i!=k and j!=k:\n                print(i*100+j*10+k)\n                cnt+=1\n    print(cnt)\n\n','1');

#
# Structure for table "student_short_answer_result"
#

DROP TABLE IF EXISTS `student_short_answer_result`;
CREATE TABLE `student_short_answer_result` (
  `student_short_answer_result_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_short_answer_student_id` int(11) NOT NULL,
  `student_short_answer_test_pager_id` int(11) NOT NULL,
  `student_short_answer_short_answer_id` int(11) NOT NULL,
  `student_short_answer_student_short_answer_result` varchar(500) NOT NULL,
  `student_short_answer_short_answer_result` varchar(500) NOT NULL,
  `student_short_answer_score` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`student_short_answer_result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

#
# Data for table "student_short_answer_result"
#

INSERT INTO `student_short_answer_result` VALUES (1,3,1,4,'<p>xxx</p>','\n\n\t#range产生的是一个列表，xrange产生的是生成器。\n\t#数据较大时xrange比range好。\n\t#Range一下把数据都返回，xrange通过yield每次返回一个。\t\n\n\n','1'),(2,3,2,4,'<p>xxx</p>','\n\n\t#range产生的是一个列表，xrange产生的是生成器。\n\t#数据较大时xrange比range好。\n\t#Range一下把数据都返回，xrange通过yield每次返回一个。\t\n\n\n','1'),(3,5,1,4,'<p>aaa</p>','\n\n\t#range产生的是一个列表，xrange产生的是生成器。\n\t#数据较大时xrange比range好。\n\t#Range一下把数据都返回，xrange通过yield每次返回一个。\t\n\n\n','1'),(4,5,3,4,'<p>aaa</p>','\n\n\t#range产生的是一个列表，xrange产生的是生成器。\n\t#数据较大时xrange比range好。\n\t#Range一下把数据都返回，xrange通过yield每次返回一个。\t\n\n\n','5'),(5,5,3,8,'<p>bbb</p>','\n\n\t# 可变类型：列表、字典、集合\n\t# 不可变类型：数字、字符串、元祖\n\n\n','5'),(6,4,1,4,'<p>aaa</p>','\n\n\t#range产生的是一个列表，xrange产生的是生成器。\n\t#数据较大时xrange比range好。\n\t#Range一下把数据都返回，xrange通过yield每次返回一个。\t\n\n\n','1'),(7,2,4,4,'<p>aaa</p>','\n\n\t#range产生的是一个列表，xrange产生的是生成器。\n\t#数据较大时xrange比range好。\n\t#Range一下把数据都返回，xrange通过yield每次返回一个。\t\n\n\n','1');

#
# Structure for table "teacher"
#

DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_name` varchar(50) NOT NULL,
  `teacher_phone` varchar(11) NOT NULL,
  `teacher_email` varchar(50) NOT NULL,
  `_teacher_password` varchar(100) NOT NULL,
  `teacher_is_delete` tinyint(1) DEFAULT NULL,
  `teacher_create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`teacher_id`),
  UNIQUE KEY `teacher_phone` (`teacher_phone`),
  UNIQUE KEY `teacher_email` (`teacher_email`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;

#
# Data for table "teacher"
#

INSERT INTO `teacher` VALUES (1,'张三','13510101010','13510101010@qq.com','pbkdf2:sha256:50000$gE4MK5RI$839a84c2aabc85dd0043fc7b7f38cc45234a504c645d0968a56ef48e1b74ed33',1,'2018-10-28 22:04:10'),(2,'李四','13510101011','13510101011@qq.com','pbkdf2:sha256:50000$wf9VOsT2$feb7b15cf6d7d3afdc2770a305e4d0f90f92ace61798b992132235ccdd8e6b2f',0,'2018-10-28 22:04:10'),(3,'王五','13510101012','13510101012@qq.com','pbkdf2:sha256:50000$gZUrUZ8L$34f638b56307b3d19f4e8968b47954c2cd1a40c08a98e979feb6e1d3ec980b65',0,'2018-10-28 22:04:10'),(4,'小红','13510101013','13510101013@qq.com','pbkdf2:sha256:50000$itOi2lcH$362bedc3fdcc6c6132a65cd195933af9d3a8d262ba9dcd8f656a918bdfa7b13f',0,'2018-10-28 22:04:10'),(5,'小李','13510101014','13510101014@qq.com','pbkdf2:sha256:50000$fIRCk8H6$9e7f3225e225f180a5e3617b369b295220d43906cb7d9ab741aba920b17a7291',0,'2018-10-28 22:04:10'),(6,'小冯','13510101015','13510101015@qq.com','pbkdf2:sha256:50000$olPZwCsO$558edaf66366a77c9270770f51fd9065e78874647583b17d8ffb08a0ec80e14d',0,'2018-10-28 22:04:10'),(7,'小赵','13510101116','13510101116@qq.com','pbkdf2:sha256:50000$is1mrTid$43e11f8ff244d61cc6d90d77556d49a5b490b0b290df315fd1acbe5ef9754d10',0,'2018-10-28 22:04:10'),(8,'小钱','13510101016','13510101016@qq.com','pbkdf2:sha256:50000$f2mflpTS$016886809b1bb0b960fc7af6e7c5d5efdc84bcdb5d4915c5b76842a14796caf0',0,'2018-10-28 22:04:10'),(9,'小孙','13510101017','13510101017@qq.com','pbkdf2:sha256:50000$nDmJTEhJ$15029298f6f4c076d4f493403d8bd417e3d5e0ca9d7f46f395ca155e61979615',0,'2018-10-28 22:04:10'),(10,'小周','13510101018','13510101018@qq.com','pbkdf2:sha256:50000$o1py2X9q$0a79e9d98cfd3189b49df6c29f880e67b3dc6e6e9babc0ee496ce3da2e61e248',0,'2018-10-28 22:04:10'),(11,'小吴','13510101119','13510101119@qq.com','pbkdf2:sha256:50000$ux4YUsv7$182b82b1dd00900ec085dc3bf2b379cbc832146d3a862aa41a01e6d96f50e304',0,'2018-10-28 22:04:10'),(12,'郑周','13520101019','13520101019@qq.xom','pbkdf2:sha256:50000$zmpgOeWn$1a68bd8ec7eaf1a52b5ebe67aa94f2cd1199cb7fd43aea4e4f35b4eec1754cda',0,'2018-10-28 22:04:10'),(13,'小王','13520101020','13520101020@qq.xom','pbkdf2:sha256:50000$gHx7moCY$3f6ba6b5b6978a0d73a7fc6014672c7e2cf5cb7c4696862844a618a9c8ed2587',0,'2018-10-28 22:04:10'),(14,'冯假','13520101021','13520101021@qq.com','pbkdf2:sha256:50000$T2HBDYFt$d93c7769da78548f7750f1d5f92405f6ab195a424741b10641745f3808afc698',0,'2018-10-28 22:04:10'),(15,'陈独秀','13520101022','13520101022@qq.com','pbkdf2:sha256:50000$PlTffS1n$b985ab0bd84b59b281dcdfc23bfea80044cd7de1106a7f4729b5f5d42e5e18f2',0,'2018-10-28 22:04:10'),(16,'诸葛','13520101023','13520101023@qq.com','pbkdf2:sha256:50000$2FnO7rn6$0a97d5490df6bc7a19f950b94619d16a731229ac4b9e47f8761950f679246f97',0,'2018-10-28 22:04:10'),(17,'卫海','13520101024','13520101024@qq.com','pbkdf2:sha256:50000$9KZIaGQD$0516e799c8163c484868edf25b271f8363b8a7d485d743c237bcee672bf8858a',0,'2018-10-28 22:04:10'),(18,'蒋介石','13520101025','13520101025@qq.com','pbkdf2:sha256:50000$Ky3ywZQ7$a558583961a92202ef45bf27dae8588912fbde25e7889c25f01f3d33aa74c403',0,'2018-10-28 22:04:10'),(19,'沈琼','13520101026','13520101026@126.com','pbkdf2:sha256:50000$Cxpg9DuQ$0406e1845d46217c0db3389152bc8416001e220d3c6dc604e04c44a723173d0c',0,'2018-10-28 22:04:10'),(20,'韩雪','17720101010','17720101010@qq.com','pbkdf2:sha256:50000$WXPFtSmv$c82eb2571f5e584972e6fdb135c39e7a073d3adfceac069772a3f19d68b076f6',0,'2018-10-28 22:04:10'),(21,'杨哈哈','17720101011','17720101011@qq.com','pbkdf2:sha256:50000$cdGJPIYO$5b582abf9dc75be608370264ba8d1a5bf7839d0a4b076b68eead6f9a8804db67',0,'2018-10-28 22:04:10'),(22,'朱珠','17720101012','17720101012@qq.com','pbkdf2:sha256:50000$XgP8aTkT$b74c9b7eecd6fe28c89b8bbd9fa576b87d03273c3fa8ed45c7e28f9fd0ed95bb',0,'2018-10-28 22:04:10'),(23,'秦始皇','17728101013','17728101013@qq.com','pbkdf2:sha256:50000$vRP593ZP$ff1c07da033b402f1e899eea4feca5dcf02df8aba397d3461fd507617ba85a1e',0,'2018-10-28 22:04:10'),(24,'许仙','17728101014','17728101014@qq.com','pbkdf2:sha256:50000$jOyi1rTv$c91c84d860ed4d93b191985e6e5db68df685c3abaf0173cc8c2c50c55b78172c',0,'2018-10-28 22:04:10'),(25,'何仙姑','17728101015','17728101015@qq.com','pbkdf2:sha256:50000$mlefTAJV$58f63ae1e4e854202af3dfedc0db1652caec947ef6c2475dd3168ed51a0f9283',0,'2018-10-28 22:04:10'),(26,'吕洞宾','17728101016','17728101016@qq.com','pbkdf2:sha256:50000$tR5PRiXW$6a0e025b4d63bf2f0f2b33c2e5e6b11542120ab58f630cffe0c6b6f2b595af16',0,'2018-10-28 22:04:10'),(27,'张杰','17728101017','17728101017@qq.com','pbkdf2:sha256:50000$UgzokR6P$cc1cd11708223c283e41d634316dd311cb94c5d82e916a4f271a34fff46d8432',0,'2018-10-28 22:04:10'),(28,'谢娜那','18728101017','18728101017@qq.com','pbkdf2:sha256:50000$z8fhS3Cu$46cc3b70c235db7b5dfaab7afff6dd036317ac7011d107cb23f2e0b2ded6d54f',0,'2018-10-28 22:04:10'),(29,'孔明','18728101018','18728101018@qq.com','pbkdf2:sha256:50000$rzmTmNpQ$139a6d44392f1e9240cffd6914c817fcef7e2a12e57ba6955a0366ae84ebfe9d',0,'2018-10-28 22:04:10'),(30,'曹植','18728101019','18728101019@qq.com','pbkdf2:sha256:50000$XVlY6H7r$49bcc18e2f00b352800d44de7a8e4fe782e7ae61a2caa2a445674be284db18e9',0,'2018-10-28 22:04:10'),(31,'严格','18728101020','18728101020@qq.com','pbkdf2:sha256:50000$fsEve7i7$e15fa0aafb5db42e54b45b7c7ef6103d8c690039867bc70f1e5ff764182a3e65',0,'2018-10-28 22:04:10'),(32,'华画','18728101021','18728101021@qq.com','pbkdf2:sha256:50000$zeKFRX7Z$e13abea15145a47181f4d2caba61b06dea40e4b9795343ab8e5eff3dccc9c0a8',0,'2018-10-28 22:04:10'),(33,'魏延','18728101023','18728101023@qq.com','pbkdf2:sha256:50000$f7gSpQ0N$9b5ea81a5b5ad3aa335bd93e02e304c11ca853290a0e5a755f54f367522a2b6b',0,'2018-10-28 22:04:10'),(34,'姜凉生','18728101024','18728101024@qq.com','pbkdf2:sha256:50000$7sJzDY6n$b761a814acc121bc2c55ecba605f97a6550e24d7f5f470e8742dc5efbbd95c66',0,'2018-10-28 22:04:10'),(35,'戚薇','18728101025','18728101025@qq.com','pbkdf2:sha256:50000$n3jlfEsz$fef6cd90447d6b6933e1b9cbee2296df5243122eea7bc4a2e5c019697fb4488c',0,'2018-10-28 22:04:10'),(36,'谢逊','18728101026','18728101026@qq.com','pbkdf2:sha256:50000$XTLExvtQ$fd7caeb9cec6f6c02475389b9dc2f2c42d3fa755ac327611d26710219b749454',0,'2018-10-28 22:04:10'),(37,'金世佳','18728101022','18728101022@qq.com','pbkdf2:sha256:50000$Bs40bmur$6f0d9826c757eff9f3564aa82dd7709ca48fa1f3dcf788da93d99b7ea7661226',0,'2018-10-28 22:04:10'),(38,'唐伯虎','18728101027','18728101027@qq.com','pbkdf2:sha256:50000$XRzQIAta$b525a2fb250590eb4b4995d3f480d87807f81fa73035e270d3a30c3bf5e2169f',0,'2018-10-28 22:04:10'),(39,'秋香','18728101028','18728101028@qq.com','pbkdf2:sha256:50000$LjOXuZVu$f532cae7e05dd1f1be537f725d1d040ff28720c8d9851ef0fb5718822d3b05e9',0,'2018-10-28 22:04:10');

#
# Structure for table "student"
#

DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_name` varchar(50) NOT NULL,
  `student_phone` varchar(11) NOT NULL,
  `student_email` varchar(50) NOT NULL,
  `_student_password` varchar(100) NOT NULL,
  `student_is_delete` tinyint(1) DEFAULT NULL,
  `student_create_time` datetime DEFAULT NULL,
  `student_class_id` int(11) DEFAULT NULL,
  `student_teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `student_class_id` (`student_class_id`),
  KEY `student_teacher_id` (`student_teacher_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`student_class_id`) REFERENCES `class` (`class_id`),
  CONSTRAINT `student_ibfk_2` FOREIGN KEY (`student_teacher_id`) REFERENCES `teacher` (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;

#
# Data for table "student"
#

INSERT INTO `student` VALUES (1,'杨文俊','15210212773','yiouejv@126.com','pbkdf2:sha256:50000$3epw6SSG$05d987de8ca6c44d69015cd90d2860723665e37ee27cee48177d6a7e92d22493',0,'2018-10-28 22:03:43',1,NULL),(2,'李莉','17610227384','1367084141@qq.com','pbkdf2:sha256:50000$aULdQX3s$2f8b53638522cb108f9974ef9be1a746ba4ef157b2bf106874d0adb92f73e5ec',0,'2018-10-28 22:03:50',2,NULL),(3,'小昭','17610027384','17610027384@qq.com','pbkdf2:sha256:50000$dzfjxXNk$3da33e77faaa843a8827b025a2a006ae982c6bdcbf743cb464b0c4a3ad0d9c4c',0,'2018-10-28 22:03:50',2,NULL),(4,'晓丽','18831417241','18831417241@qq.com','pbkdf2:sha256:50000$AAgJcxmR$460ed987414b775591916ae938fd900e175bc3a6f563b193c03e6d280b0b15a4',0,'2018-10-28 22:03:50',2,NULL),(5,'婉言','17643256845','17643256845@qq.com','pbkdf2:sha256:50000$Uj971usr$00913433a9f1bbbcd3c6b72206c8b0105dd21844032f1a9d982c088ec048ef3b',0,'2018-10-28 22:03:50',2,NULL),(6,'欣荣','15223658452','15223658452@qq.com','pbkdf2:sha256:50000$9Na9pvtZ$ed02341740d326b9948619494b896ffccf5276b10a79ce34e50be69f96b2258f',0,'2018-10-28 22:03:50',2,NULL),(7,'若曦','1865247632','1865247632@qq.com','pbkdf2:sha256:50000$0Q4yGzRh$dd2052b820b2cffa2cd45d45fab4d0983bc42da900bae1ee4ac2f12493a3144e',0,'2018-10-28 22:03:50',2,NULL),(8,'洛晴川','13952648537','13952648537@qq.com','pbkdf2:sha256:50000$wA4vWsrp$235beb8b7b983b39955e59cf81b3d69eab7251cdba22a222394a173e89750a76',0,'2018-10-28 22:03:50',2,NULL),(9,'魏晨','13952648531','13952648531@qq.com','pbkdf2:sha256:50000$6JyHcaaD$7d6c8becfc7c83d9cfcf2c44ff8fcf854e565bbcecb5c6f1473560e9256d84aa',0,'2018-10-28 22:03:50',2,NULL),(10,'楚雨荨','13952648532','13952648532@qq.com','pbkdf2:sha256:50000$BMu8YKBa$81bcf4029faaad70df57ffb9ca8d61f20903aacb231aa44e9d5207935dee4fc9',0,'2018-10-28 22:03:50',2,NULL),(11,'如懿','15268452561','15268452561@qq.com','pbkdf2:sha256:50000$CnuBNULp$65e1d2f2f1ae3a04fab9e05d03b2ea06fa3472cf6ed8fd5f7dbbdb0256cd4c60',0,'2018-10-28 22:03:50',2,NULL),(12,'玲珑','15268452565','15268452565@qq.com','pbkdf2:sha256:50000$9pPeCulr$0ac9e3a798ca1a1c72e9ad32a14b4329c2bfe7f1fc4b201a1b22a18b9c35ecc6',0,'2018-10-28 22:03:50',2,NULL),(13,'张翰','15234586587','15234586587@qq.com','pbkdf2:sha256:50000$ScxNOhZI$9bc39ccbfcc670edbad60beddf6d489c5d8b4e5a3471c3a126ede163a296e062',0,'2018-10-28 22:03:50',2,NULL),(14,'魏燕碗','17610235989','17610235989@qq.com','pbkdf2:sha256:50000$pv2ww8Mv$6c582e90df534f65491ad086d06de00c5a6e6073ba0b5b0f442f34c1ef08d1a4',0,'2018-10-28 22:03:50',2,NULL),(15,'晓霞','17610235986','17610235986@qq.com','pbkdf2:sha256:50000$qW4HaTIi$8605b6e013b2a6ba0fe3508dd1e320d6ab5eee2456f137f5d09d4e59463e6d5e',0,'2018-10-28 22:03:50',2,NULL),(16,'杨洋','17610235981','17610235981@qq.com','pbkdf2:sha256:50000$k3Y9KU9G$8eecd8bf497086af6f80e4c51b0ccaf804344250c855bc8e5351c9c803994079',0,'2018-10-28 22:03:50',2,NULL),(17,'恩典','17610235984','17610235984@qq.com','pbkdf2:sha256:50000$qaWP8CGf$19683f3b32176866d4669261b5958e23f493e4e8aa5a264173f1c9415e2afefa',0,'2018-10-28 22:03:50',2,NULL),(18,'陈伟霆','15002351684','15002351684@qq.com','pbkdf2:sha256:50000$ABbAJH5D$bb3c377a02bd28fda69bd861eeeeb6cf2cc8fb00eb0270a42836dffb01c26486',0,'2018-10-28 22:03:50',2,NULL),(19,'本兮','15002351683','15002351683@qq.com','pbkdf2:sha256:50000$l8wnJXpw$6fbb9ab77d46777952f98b85100c487e9e2893dce02a344839061ac88c33def8',0,'2018-10-28 22:03:50',2,NULL),(20,'程茜','15002351681','15002351681@qq.com','pbkdf2:sha256:50000$JGQYizzM$289190b433980a394b63ea665bf781a2aba437b55baa1a58e4bcab0833800430',0,'2018-10-28 22:03:50',2,NULL),(21,'晨曦','15002351685','15002351685@qq.com','pbkdf2:sha256:50000$NfxQEcFG$bbd557175b70d51eb27d61b1c6ffe7a33caabaf2a8ab3144c7bccd649379e886',0,'2018-10-28 22:03:50',2,NULL),(22,'谢娜','15248652353','15248652353@qq.com','pbkdf2:sha256:50000$0YlPAdJR$4883889fc02bd0f6ec3010d161761e10410d3e8873bd8a0e5210de958661a40d',0,'2018-10-28 22:03:50',2,NULL),(23,'张杰','15248652355','15248652355@qq.com','pbkdf2:sha256:50000$UCR9Jguq$891407204961fdaaca09ff346985b1b4b33308d3f12a01146f9dffe37216170e',0,'2018-10-28 22:03:50',2,NULL),(24,'奕欢','15248652351','15248652351@qq.com','pbkdf2:sha256:50000$NRvub0Ig$24e38f423c8167f8fb5be5dcab1af464ae6bc13d1a9f92770a7376f98a915fb9',0,'2018-10-28 22:03:50',2,NULL),(25,'盛利','15248652357','15248652357@qq.com','pbkdf2:sha256:50000$vrePjXah$ae6ffb819fea2cc37d3ed3dd7193a1d033642a4edd011301962ada8391f1b6b5',0,'2018-10-28 22:03:50',2,NULL),(26,'怡儿','13852641595','13852641595@qq.com','pbkdf2:sha256:50000$6cT39uAK$53047f14968333afde433f4948c842fab9b005b1d2dcef27341f5167ef520333',0,'2018-10-28 22:03:50',2,NULL),(27,'常德','13852641596','13852641596@qq.com','pbkdf2:sha256:50000$YtUZJ7xE$d9e5d4d2e9a6995dc81d071eae13bc4a553205a2748bb1fd25adec62bdf06287',0,'2018-10-28 22:03:50',3,NULL),(28,'哈达迪','15248652654','15248652654@qq.com','pbkdf2:sha256:50000$EGfEhukC$06d9274a6c5dc102189d0b4e8cc1831e4c5bcd6b8e3f5753316739a122fc1751',0,'2018-10-28 22:03:50',3,NULL),(29,'黄凯','15826547521','15826547521@qq.com','pbkdf2:sha256:50000$OD3Nv3r4$3cdc9006c9ff612e446f01cf32172aae7e8338493c5e9fb540c3aaa57be4ef95',0,'2018-10-28 22:03:50',3,NULL),(30,'周宏','15625684265','15625684265@qq.com','pbkdf2:sha256:50000$yy3b0jil$9a4dd54dd3dd16840177ac7b289909a619aeaef3d67e43b58e145ea2baadc2f9',0,'2018-10-28 22:03:50',3,NULL),(31,'宏瑞','15624589875','15624589875@qq.com','pbkdf2:sha256:50000$zavNtB2v$a2e55c6e1dc15b22b7e60d6fa8131fa41d46f1dfcd0d572e09ec2e1ece82169e',0,'2018-10-28 22:03:50',3,NULL),(32,'张飞','15248652365','15248652365@qq.com','pbkdf2:sha256:50000$YF6pLmVU$96ec281213863d9309a1ef6bc30ec0fce0b290d643b37bbe72a0ccd01fb2700c',0,'2018-10-28 22:03:50',3,NULL),(33,'裴玄','15642279865','15642279865@qq.com','pbkdf2:sha256:50000$BjCLKnV2$0cb8fb60d68d2220c1a4d76b3732752cd6d89852fd23a46875a7e0e2975f9631',0,'2018-10-28 22:03:50',3,NULL),(34,'新华','15326485724','15326485724@qq.com','pbkdf2:sha256:50000$NvJM79VL$64aa0c612199c059cf1697ef12fd975720fbfcdb86cf326b4462ec9ce6ef471d',0,'2018-10-28 22:03:50',3,NULL),(35,'凯强','13952468521','13952468521@qq.com','pbkdf2:sha256:50000$H9Zhy4dT$e9143bc8c07b1ace766492b3ea254e128bd67e45825e93f7c37756a63ce447c2',0,'2018-10-28 22:03:50',3,NULL),(36,'陈勇同','13831392033','13831392033@qq.com','pbkdf2:sha256:50000$YLXghjau$cf82504cf17a658ddde3878f2b4316ca0e3c42100c0938ddc374e26d79784036',0,'2018-10-28 22:03:50',3,NULL),(37,'刘玉婷','15002325167','15002325167','pbkdf2:sha256:50000$9FnPN0Oy$bb9d68d172febca098bb7322f136b48c497b36dc63e27c25517f6f5294624c19',0,'2018-10-28 22:03:50',3,NULL),(38,'婉婷','15002325767','15002325767@qq.com','pbkdf2:sha256:50000$GPiFm32v$463097d2e2ce9e7f68af10ef2283f57579b65bb50ddda2fe3529c5c81d6186b4',0,'2018-10-28 22:03:50',3,NULL),(39,'艳玲','15003335167','15003335167@qq.com','pbkdf2:sha256:50000$kAi72bzX$6b41f28b9ce59ea2cc2b982ad12b44508249acf9a0a32bc21cb0474e77207dd0',0,'2018-10-28 22:03:50',3,NULL),(40,'雪儿','17612324865','17612324865@qq.com','pbkdf2:sha256:50000$MmLqThm6$2d62fdfcb6bd4e862c724fa43122017e6dcf12fd1a00b845a7a3a41dadbaaa00',0,'2018-10-28 22:03:50',3,NULL),(41,'富贵','18836257954','18836257954@qq.com','pbkdf2:sha256:50000$YT27lZQG$07770d40943535c848a58dc5b9ab17eb14d58fbdf5651c365e73e20e0ffe81af',0,'2018-10-28 22:03:50',3,NULL);

#
# Structure for table "student_teacher"
#

DROP TABLE IF EXISTS `student_teacher`;
CREATE TABLE `student_teacher` (
  `student_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`student_id`,`teacher_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `student_teacher_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),
  CONSTRAINT `student_teacher_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "student_teacher"
#


#
# Structure for table "class_teacher"
#

DROP TABLE IF EXISTS `class_teacher`;
CREATE TABLE `class_teacher` (
  `class_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`class_id`,`teacher_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `class_teacher_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`),
  CONSTRAINT `class_teacher_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "class_teacher"
#

INSERT INTO `class_teacher` VALUES (4,2),(4,3),(4,4),(6,5),(6,6),(6,7),(6,8),(7,9),(7,10),(7,11),(7,12),(8,13),(8,14),(8,15),(8,16),(9,17),(9,18),(9,20),(10,21),(10,22),(10,23),(10,24),(10,25),(11,26),(11,27),(11,28),(11,29),(12,30),(12,31),(12,32),(13,33),(13,34),(13,35),(13,36),(14,37),(14,38),(14,39),(22,1),(23,1),(24,19);

#
# Structure for table "test_pager"
#

DROP TABLE IF EXISTS `test_pager`;
CREATE TABLE `test_pager` (
  `test_pager_id` int(11) NOT NULL AUTO_INCREMENT,
  `test_pager_type` varchar(50) DEFAULT NULL,
  `test_pager_name` varchar(50) NOT NULL,
  `test_pager_total_score` int(11) DEFAULT NULL,
  `test_pager_create_time` datetime DEFAULT NULL,
  `test_pager_test_time` datetime DEFAULT NULL,
  `test_pager_publish` tinyint(1) DEFAULT NULL,
  `test_pager_choice_num` int(11) DEFAULT NULL,
  `test_pager_short_answer_num` int(11) DEFAULT NULL,
  `test_pager_program_num` int(11) DEFAULT NULL,
  `test_pager_choice_score` int(11) DEFAULT NULL,
  `test_pager_short_answer_score` int(11) DEFAULT NULL,
  `test_pager_program_score` int(11) DEFAULT NULL,
  PRIMARY KEY (`test_pager_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

#
# Data for table "test_pager"
#

INSERT INTO `test_pager` VALUES (1,'python','2018年09月-AID1807-月考',6,'2018-10-28 22:04:38','2018-10-10 00:00:00',1,4,1,1,1,1,1),(2,'python','2018年05月-AID1807-月考',6,'2018-10-28 22:07:43','2101-11-11 00:00:00',1,4,1,1,1,1,1),(3,'python','2018年09月-AID1807-补考',100,'2018-10-29 08:53:55','2012-10-10 00:00:00',1,10,2,5,4,5,10),(4,'python','asss',3,'2018-10-30 09:07:26','2010-10-10 00:00:00',1,1,1,1,1,1,1),(5,'python','2018年09月-AID1807-月考',3,'2018-10-30 11:17:00',NULL,0,1,1,1,1,1,1);

#
# Structure for table "score"
#

DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `score_id` int(11) NOT NULL AUTO_INCREMENT,
  `score_student_socre` int(11) DEFAULT NULL,
  `score_state` varchar(10) DEFAULT NULL,
  `score_student_id` int(11) DEFAULT NULL,
  `score_test_pager_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`score_id`),
  KEY `score_student_id` (`score_student_id`),
  KEY `score_test_pager_id` (`score_test_pager_id`),
  CONSTRAINT `score_ibfk_1` FOREIGN KEY (`score_student_id`) REFERENCES `student` (`student_id`),
  CONSTRAINT `score_ibfk_2` FOREIGN KEY (`score_test_pager_id`) REFERENCES `test_pager` (`test_pager_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

#
# Data for table "score"
#

INSERT INTO `score` VALUES (1,0,'未参加考试',2,1),(2,5,'已经批阅',3,1),(3,1,'已经批阅',4,1),(4,5,'已经批阅',5,1),(5,0,'未参加考试',6,1),(6,0,'未参加考试',7,1),(7,0,'未参加考试',8,1),(8,0,'未参加考试',9,1),(9,0,'未参加考试',10,1),(10,0,'未参加考试',11,1),(11,0,'未参加考试',12,1),(12,0,'未参加考试',13,1),(13,0,'未参加考试',14,1),(14,0,'未参加考试',15,1),(15,0,'未参加考试',16,1),(16,0,'未参加考试',17,1),(17,0,'未参加考试',18,1),(18,0,'未参加考试',19,1),(19,0,'未参加考试',20,1),(20,0,'未参加考试',21,1),(21,0,'未参加考试',22,1),(22,0,'未参加考试',23,1),(23,0,'未参加考试',24,1),(24,0,'未参加考试',25,1),(25,0,'未参加考试',26,1),(26,0,'未参加考试',2,2),(27,6,'已经批阅',3,2),(28,0,'未参加考试',4,2),(29,0,'未参加考试',5,2),(30,0,'未参加考试',6,2),(31,0,'未参加考试',7,2),(32,0,'未参加考试',8,2),(33,0,'未参加考试',9,2),(34,0,'未参加考试',10,2),(35,0,'未参加考试',11,2),(36,0,'未参加考试',12,2),(37,0,'未参加考试',13,2),(38,0,'未参加考试',14,2),(39,0,'未参加考试',15,2),(40,0,'未参加考试',16,2),(41,0,'未参加考试',17,2),(42,0,'未参加考试',18,2),(43,0,'未参加考试',19,2),(44,0,'未参加考试',20,2),(45,0,'未参加考试',21,2),(46,0,'未参加考试',22,2),(47,0,'未参加考试',23,2),(48,0,'未参加考试',24,2),(49,0,'未参加考试',25,2),(50,0,'未参加考试',26,2),(51,0,'未参加考试',2,3),(52,0,'未参加考试',3,3),(53,0,'未参加考试',4,3),(54,86,'已经批阅',5,3),(55,0,'未参加考试',6,3),(56,0,'未参加考试',7,3),(57,0,'未参加考试',8,3),(58,0,'未参加考试',9,3),(59,0,'未参加考试',10,3),(60,0,'未参加考试',11,3),(61,0,'未参加考试',12,3),(62,0,'未参加考试',13,3),(63,0,'未参加考试',14,3),(64,0,'未参加考试',15,3),(65,0,'未参加考试',16,3),(66,0,'未参加考试',17,3),(67,0,'未参加考试',18,3),(68,0,'未参加考试',19,3),(69,0,'未参加考试',20,3),(70,0,'未参加考试',21,3),(71,0,'未参加考试',22,3),(72,0,'未参加考试',23,3),(73,0,'未参加考试',24,3),(74,0,'未参加考试',25,3),(75,0,'未参加考试',26,3),(76,3,'已经批阅',2,4),(77,0,'未参加考试',3,4),(78,0,'未参加考试',4,4),(79,0,'未参加考试',5,4),(80,0,'未参加考试',6,4),(81,0,'未参加考试',7,4),(82,0,'未参加考试',8,4),(83,0,'未参加考试',9,4),(84,0,'未参加考试',10,4),(85,0,'未参加考试',11,4),(86,0,'未参加考试',12,4),(87,0,'未参加考试',13,4),(88,0,'未参加考试',14,4),(89,0,'未参加考试',15,4),(90,0,'未参加考试',16,4),(91,0,'未参加考试',17,4),(92,0,'未参加考试',18,4),(93,0,'未参加考试',19,4),(94,0,'未参加考试',20,4),(95,0,'未参加考试',21,4),(96,0,'未参加考试',22,4),(97,0,'未参加考试',23,4),(98,0,'未参加考试',24,4),(99,0,'未参加考试',25,4),(100,0,'未参加考试',26,4);

#
# Structure for table "test_pager_choice"
#

DROP TABLE IF EXISTS `test_pager_choice`;
CREATE TABLE `test_pager_choice` (
  `test_pager_id` int(11) NOT NULL,
  `choice_id` int(11) NOT NULL,
  PRIMARY KEY (`test_pager_id`,`choice_id`),
  KEY `choice_id` (`choice_id`),
  CONSTRAINT `test_pager_choice_ibfk_1` FOREIGN KEY (`test_pager_id`) REFERENCES `test_pager` (`test_pager_id`),
  CONSTRAINT `test_pager_choice_ibfk_2` FOREIGN KEY (`choice_id`) REFERENCES `choice` (`choice_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "test_pager_choice"
#

INSERT INTO `test_pager_choice` VALUES (1,4),(1,8),(1,12),(1,16),(2,4),(2,8),(2,12),(2,16),(3,1),(3,4),(3,5),(3,8),(3,9),(3,12),(3,13),(3,16),(3,20),(3,24),(4,4),(5,4);

#
# Structure for table "test_pager_class"
#

DROP TABLE IF EXISTS `test_pager_class`;
CREATE TABLE `test_pager_class` (
  `test_pager_id` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  PRIMARY KEY (`test_pager_id`,`class_id`),
  KEY `class_id` (`class_id`),
  CONSTRAINT `test_pager_class_ibfk_1` FOREIGN KEY (`test_pager_id`) REFERENCES `test_pager` (`test_pager_id`),
  CONSTRAINT `test_pager_class_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "test_pager_class"
#

INSERT INTO `test_pager_class` VALUES (1,15),(2,16),(3,17),(4,21);

#
# Structure for table "test_pager_program"
#

DROP TABLE IF EXISTS `test_pager_program`;
CREATE TABLE `test_pager_program` (
  `program_id` int(11) NOT NULL,
  `test_pager_id` int(11) NOT NULL,
  PRIMARY KEY (`program_id`,`test_pager_id`),
  KEY `test_pager_id` (`test_pager_id`),
  CONSTRAINT `test_pager_program_ibfk_1` FOREIGN KEY (`program_id`) REFERENCES `program` (`program_id`),
  CONSTRAINT `test_pager_program_ibfk_2` FOREIGN KEY (`test_pager_id`) REFERENCES `test_pager` (`test_pager_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "test_pager_program"
#

INSERT INTO `test_pager_program` VALUES (1,3),(4,1),(4,2),(4,3),(4,4),(4,5),(5,3),(8,3),(12,3);

#
# Structure for table "test_pager_short_answer"
#

DROP TABLE IF EXISTS `test_pager_short_answer`;
CREATE TABLE `test_pager_short_answer` (
  `short_answer_id` int(11) NOT NULL,
  `test_pager_id` int(11) NOT NULL,
  PRIMARY KEY (`short_answer_id`,`test_pager_id`),
  KEY `test_pager_id` (`test_pager_id`),
  CONSTRAINT `test_pager_short_answer_ibfk_1` FOREIGN KEY (`short_answer_id`) REFERENCES `short_answer` (`short_answer_id`),
  CONSTRAINT `test_pager_short_answer_ibfk_2` FOREIGN KEY (`test_pager_id`) REFERENCES `test_pager` (`test_pager_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "test_pager_short_answer"
#

INSERT INTO `test_pager_short_answer` VALUES (4,1),(4,2),(4,3),(4,4),(4,5),(8,3);
