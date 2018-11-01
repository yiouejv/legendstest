# encoding:utf-8
'''
    name: yiouejv
    email: yiouejv@126.com
    data: 2018-10
    introduce: 介绍
    env: python3.5
'''
from config import session as db_session
from apps.front.models import Student, Class


stu1 = Student(
	student_name = "李莉",
	student_phone = "17610227384",
	student_email = "1367084141@qq.com",
	student_password = "123456789"
)
# stu1.student_class = "AID1807"

stu2 = Student(
	student_name = "小昭",
	student_phone = "17610027384",
	student_email = "17610027384@qq.com",
	student_password = "123456789"
)
# stu2.student_class = "AID1807"

stu3 = Student(
	student_name = "晓丽",
	student_phone = "18831417241",
	student_email = "18831417241@qq.com",
	student_password = "123456789"
)
# stu3.student_class = "AID1807"

stu4 = Student(
	student_name = "婉言",
	student_phone = "17643256845",
	student_email = "17643256845@qq.com",
	student_password = "123456789"
)
# stu4.student_class = "AID1807"

stu5 = Student(
	student_name = "欣荣",
	student_phone = "15223658452",
	student_email = "15223658452@qq.com",
	student_password = "123456789"
)
# stu5.student_class = "AID1807"

stu6 = Student(
	student_name = "若曦",
	student_phone = "1865247632",
	student_email = "1865247632@qq.com",
	student_password = "123456789"
)
# stu6.student_class = "AID1807"

stu7 = Student(
	student_name = "洛晴川",
	student_phone = "13952648537",
	student_email = "13952648537@qq.com",
	student_password = "123456789"
)
# stu7.student_class = "AID1807"

stu8 = Student(
	student_name = "魏晨",
	student_phone = "13952648531",
	student_email = "13952648531@qq.com",
	student_password = "123456789"
)
# stu8.student_class = "AID1807"

stu9 = Student(
	student_name = "楚雨荨",
	student_phone = "13952648532",
	student_email = "13952648532@qq.com",
	student_password = "123456789"
)
# stu9.student_class = "AID1807"

stu10 = Student(
	student_name = "如懿",
	student_phone = "15268452561",
	student_email = "15268452561@qq.com",
	student_password = "123456789"
)
# stu10.student_class = "AID1807"

stu11 = Student(
	student_name = "玲珑",
	student_phone = "15268452565",
	student_email = "15268452565@qq.com",
	student_password = "123456789"
)
# stu11.student_class = "AID1807"

stu12 = Student(
	student_name = "张翰",
	student_phone = "15234586587",
	student_email = "15234586587@qq.com",
	student_password = "123456789"
)
# stu12.student_class = "AID1807"

stu13 = Student(
	student_name = "魏燕碗",
	student_phone = "17610235989",
	student_email = "17610235989@qq.com",
	student_password = "123456789"
)
# stu13.student_class = "AID1807"

stu14 = Student(
	student_name = "晓霞",
	student_phone = "17610235986",
	student_email = "17610235986@qq.com",
	student_password = "123456789"
)
# stu14.student_class = "AID1807"

stu15 = Student(
	student_name = "杨洋",
	student_phone = "17610235981",
	student_email = "17610235981@qq.com",
	student_password = "123456789"
)
# stu15.student_class = "AID1807"

stu16 = Student(
	student_name = "恩典",
	student_phone = "17610235984",
	student_email = "17610235984@qq.com",
	student_password = "123456789"
)
# stu16.student_class = "AID1807"

stu17 = Student(
	student_name = "陈伟霆",
	student_phone = "15002351684",
	student_email = "15002351684@qq.com",
	student_password = "123456789"
)
# stu17.student_class = "AID1807"

stu18 = Student(
	student_name = "本兮",
	student_phone = "15002351683",
	student_email = "15002351683@qq.com",
	student_password = "123456789"
)
# stu18.student_class = "AID1807"

stu19 = Student(
	student_name = "程茜",
	student_phone = "15002351681",
	student_email = "15002351681@qq.com",
	student_password = "123456789"
)
# stu19.student_class = "AID1807"

stu20 = Student(
	student_name = "晨曦",
	student_phone = "15002351685",
	student_email = "15002351685@qq.com",
	student_password = "123456789"
)
# stu20.student_class = "AID1807"

stu21 = Student(
	student_name = "谢娜",
	student_phone = "15248652353",
	student_email = "15248652353@qq.com",
	student_password = "123456789"
)
# stu21.student_class = "AID1808"

stu22 = Student(
	student_name = "张杰",
	student_phone = "15248652355",
	student_email = "15248652355@qq.com",
	student_password = "123456789"
)
# stu22.student_class = "AID1808"

stu23 = Student(
	student_name = "奕欢",
	student_phone = "15248652351",
	student_email = "15248652351@qq.com",
	student_password = "123456789"
)
# stu23.student_class = "AID1808"

stu24 = Student(
	student_name = "盛利",
	student_phone = "15248652357",
	student_email = "15248652357@qq.com",
	student_password = "123456789"
)
# stu24.student_class = "AID1808"

stu25 = Student(
	student_name = "怡儿",
	student_phone = "13852641595",
	student_email = "13852641595@qq.com",
	student_password = "123456789"
)
# stu25.student_class = "AID1808"

stu26 = Student(
	student_name = "常德",
	student_phone = "13852641596",
	student_email = "13852641596@qq.com",
	student_password = "123456789"
)
# stu26.student_class = "AID1808"

stu27 = Student(
	student_name = "哈达迪",
	student_phone = "15248652654",
	student_email = "15248652654@qq.com",
	student_password = "123456789"
)
# stu27.student_class = "AID1808"

stu28 = Student(
	student_name = "黄凯",
	student_phone = "15826547521",
	student_email = "15826547521@qq.com",
	student_password = "123456789"
)
# stu28.student_class = "AID1808"

stu29 = Student(
	student_name = "周宏",
	student_phone = "15625684265",
	student_email = "15625684265@qq.com",
	student_password = "123456789"
)
# stu29.student_class = "AID1808"

stu30 = Student(
	student_name = "宏瑞",
	student_phone = "15624589875",
	student_email = "15624589875@qq.com",
	student_password = "123456789"
)
# stu30.student_class = "AID1808"

stu31 = Student(
	student_name = "张飞",
	student_phone = "15248652365",
	student_email = "15248652365@qq.com",
	student_password = "123456789"
)
# stu31.student_class = "AID1808"

stu32 = Student(
	student_name = "裴玄",
	student_phone = "15642279865",
	student_email = "15642279865@qq.com",
	student_password = "123456789"
)
# stu32.student_class = "AID1808"

stu33 = Student(
	student_name = "新华",
	student_phone = "15326485724",
	student_email = "15326485724@qq.com",
	student_password = "123456789"
)
# stu33.student_class = "AID1808"

stu34 = Student(
	student_name = "凯强",
	student_phone = "13952468521",
	student_email = "13952468521@qq.com",
	student_password = "123456789"
)
# stu34.student_class = "AID1808"

stu35 = Student(
	student_name = "陈勇同",
	student_phone = "13831392033",
	student_email = "13831392033@qq.com",
	student_password = "123456789"
)
# stu35.student_class = "AID1808"

stu36 = Student(
	student_name = "刘玉婷",
	student_phone = "15002325167",
	student_email = "15002325167",
	student_password = "123456789"
)
# stu36.student_class = "AID1808"

stu37 = Student(
	student_name = "婉婷",
	student_phone = "15002325767",
	student_email = "15002325767@qq.com",
	student_password = "123456789"
)
# stu37.student_class = "AID1808"

stu38 = Student(
	student_name = "艳玲",
	student_phone = "15003335167",
	student_email = "15003335167@qq.com",
	student_password = "123456789"
)
# stu38.student_class = "AID1808"

stu39 = Student(
	student_name = "雪儿",
	student_phone = "17612324865",
	student_email = "17612324865@qq.com",
	student_password = "123456789"
)
# stu39.student_class = "AID1808"

stu40 = Student(
	student_name = "富贵",
	student_phone = "18836257954",
	student_email = "18836257954@qq.com",
	student_password = "123456789"
)
# stu40.student_class = "AID1808"

class1 = Class(class_name='AID1807')
class2 = Class(class_name='AID1808')
class3 = Class(class_name='AID1809')
class4 = Class(class_name='AID1708')
class5 = Class(class_name='AID1709')
class6 = Class(class_name='AID1710')
class7 = Class(class_name='AID1711')
class8 = Class(class_name='AID1810')
class9 = Class(class_name='AID1811')
class10 = Class(class_name='AID1812')
class11 = Class(class_name='AID1712')

class1.class_students.append(stu1)
class1.class_students.append(stu2)
class1.class_students.append(stu3)
class1.class_students.append(stu4)
class1.class_students.append(stu5)
class1.class_students.append(stu6)
class1.class_students.append(stu7)
class1.class_students.append(stu8)
class1.class_students.append(stu9)
class1.class_students.append(stu10)
class1.class_students.append(stu11)
class1.class_students.append(stu12)
class1.class_students.append(stu13)
class1.class_students.append(stu14)
class1.class_students.append(stu15)
class1.class_students.append(stu16)
class1.class_students.append(stu17)
class1.class_students.append(stu18)
class1.class_students.append(stu19)
class1.class_students.append(stu20)
class1.class_students.append(stu21)
class1.class_students.append(stu22)
class1.class_students.append(stu23)
class1.class_students.append(stu24)
class1.class_students.append(stu25)
class1.class_students.append(stu26)
class2.class_students.append(stu26)
class2.class_students.append(stu27)
class2.class_students.append(stu28)
class2.class_students.append(stu29)
class2.class_students.append(stu30)
class2.class_students.append(stu31)
class2.class_students.append(stu32)
class2.class_students.append(stu33)
class2.class_students.append(stu34)
class2.class_students.append(stu35)
class2.class_students.append(stu36)
class2.class_students.append(stu37)
class2.class_students.append(stu38)
class2.class_students.append(stu39)
class2.class_students.append(stu40)
db_session.add(class1)
db_session.add(class2)

db_session.commit()
