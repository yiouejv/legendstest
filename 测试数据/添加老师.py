# encoding:utf-8
'''
    name: yiouejv
    email: yiouejv@126.com
    data: 2018-10
    introduce: 介绍
    env: python3.5
'''
from apps.front.models import Teacher, Class
from config import session as db_session

teach1 = Teacher(
	teacher_name="张三",
	teacher_phone="13510101010",
	teacher_email="13510101010@qq.com",
	teacher_password="1234567"
	)

teach2 = Teacher(
	teacher_name="李四",
	teacher_phone="13510101011",
	teacher_email="13510101011@qq.com",
	teacher_password="1234568"
	)
# teach2.teacher_class.append("AID1807")
# teach2.teacher_class.append("AID1808")

teach3 = Teacher(
	teacher_name="王五",
	teacher_phone="13510101012",
	teacher_email="13510101012@qq.com",
	teacher_password="1234569"
	)
# teach3.teacher_class.append("AID1807")
# teach3.teacher_class.append("AID1808")

teach4 = Teacher(
	teacher_name="小红",
	teacher_phone="13510101013",
	teacher_email="13510101013@qq.com",
	teacher_password="2345610"
	)
# teach4.teacher_class.append("AID1807")
# teach4.teacher_class.append("AID1808")

teach5 = Teacher(
	teacher_name="小李",
	teacher_phone="13510101014",
	teacher_email="13510101014@qq.com",
	teacher_password="2345611"
	)
# teach5.teacher_class.append("AID1807")
# teach5.teacher_class.append("AID1808")

teach6 = Teacher(
	teacher_name="小冯",
	teacher_phone="13510101015",
	teacher_email="13510101015@qq.com",
	teacher_password="2345612"
	)
# teach6.teacher_class.append("AID1807")
# teach6.teacher_class.append("AID1808")

teach7 = Teacher(
	teacher_name="小赵",
	teacher_phone="13510101116",
	teacher_email="13510101116@qq.com",
	teacher_password="2345613"
	)
# teach7.teacher_class.append("AID1807")
# teach7.teacher_class.append("AID1808")
teach8 = Teacher(
	teacher_name="小钱",
	teacher_phone="13510101016",
	teacher_email="13510101016@qq.com",
	teacher_password="2345614"
	)
# teach8.teacher_class.append("AID1807")
# teach8.teacher_class.append("AID1808")

teach9 = Teacher(
	teacher_name="小孙",
	teacher_phone="13510101017",
	teacher_email="13510101017@qq.com",
	teacher_password="2345615"
	)
# teach9.teacher_class.append("AID1807")
# teach9.teacher_class.append("AID1808")

teach10 = Teacher(
	teacher_name="小周",
	teacher_phone="13510101018",
	teacher_email="13510101018@qq.com",
	teacher_password="2345616"
	)
# teach10.teacher_class.append("AID1807")
# teach10.teacher_class.append("AID1808")
teach11 = Teacher(
	teacher_name="小吴",
	teacher_phone="13510101119",
	teacher_email="13510101119@qq.com",
	teacher_password="2345617"
	)
# teach11.teacher_class.append("AID1807")
# teach11.teacher_class.append("AID1808")


teach12 = Teacher(
	teacher_name="郑周",
	teacher_phone="13520101019",
	teacher_email="13520101019@qq.xom",
	teacher_password="2345618"
	)
# teach12.teacher_class.append("AID1807")
# teach12.teacher_class.append("AID1808")

teach13 = Teacher(
	teacher_name="小王",
	teacher_phone="13520101020",
	teacher_email="13520101020@qq.xom",
	teacher_password="2345619"
	)
# teach13.teacher_class.append("AID1807")
# teach13.teacher_class.append("AID1808")
teach14 = Teacher(
	teacher_name="冯假",
	teacher_phone="13520101021",
	teacher_email="13520101021@qq.com",
	teacher_password="2345620"
	)
# teach14.teacher_class.append("AID1807")
# teach14.teacher_class.append("AID1808")

teach15 = Teacher(
	teacher_name="陈独秀",
	teacher_phone="13520101022",
	teacher_email="13520101022@qq.com",
	teacher_password="3456710"
	)
# teach15.teacher_class.append("AID1807")
# teach15.teacher_class.append("AID1808")

teach16 = Teacher(
	teacher_name="诸葛",
	teacher_phone="13520101023",
	teacher_email="13520101023@qq.com",
	teacher_password="3456711"
	)
# teach16.teacher_class.append("AID1807")
# teach16.teacher_class.append("AID1808")

teach17 = Teacher(
	teacher_name="卫海",
	teacher_phone="13520101024",
	teacher_email="13520101024@qq.com",
	teacher_password="3456712"
	)
# teach17.teacher_class.append("AID1807")
# teach17.teacher_class.append("AID1808")

teach18 = Teacher(
	teacher_name="蒋介石",
	teacher_phone="13520101025",
	teacher_email="13520101025@qq.com",
	teacher_password="3456713"
	)
# teach18.teacher_class.append("AID1807")
# teach18.teacher_class.append("AID1808")

teach19 = Teacher(
	teacher_name="沈琼",
	teacher_phone="13520101026",
	teacher_email="13520101026",
	teacher_password="3456714"
	)
# teach19.teacher_class.append("AID1807")
# teach19.teacher_class.append("AID1808")

teach20 = Teacher(
	teacher_name="韩雪",
	teacher_phone="17720101010",
	teacher_email="17720101010@qq.com",
	teacher_password="3456715"
	)
# teach20.teacher_class.append("AID1807")
# teach20.teacher_class.append("AID1808")

teach21 = Teacher(
	teacher_name="杨哈哈",
	teacher_phone="17720101011",
	teacher_email="17720101011@qq.com",
	teacher_password="9876510"
	)
# teach21.teacher_class.append("AID1807")
# teach21.teacher_class.append("AID1808")

teach22 = Teacher(
	teacher_name="朱珠",
	teacher_phone="17720101012",
	teacher_email="17720101012@qq.com",
	teacher_password="9876511"
	)
# teach22.teacher_class.append("AID1807")
# teach22.teacher_class.append("AID1808")

teach23 = Teacher(
	teacher_name="秦始皇",
	teacher_phone="17728101013",
	teacher_email="17728101013@qq.com",
	teacher_password="9876512"
	)
# teach23.teacher_class.append("AID1807")
# teach23.teacher_class.append("AID1808")

teach24 = Teacher(
	teacher_name="许仙",
	teacher_phone="17728101014",
	teacher_email="17728101014@qq.com",
	teacher_password="9876513"
	)
# teach24.teacher_class.append("AID1807")
# teach24.teacher_class.append("AID1808")

teach25 = Teacher(
	teacher_name="何仙姑",
	teacher_phone="17728101015",
	teacher_email="17728101015@qq.com",
	teacher_password="9876514"
	)

teach26 = Teacher(
	teacher_name="吕洞宾",
	teacher_phone="17728101016",
	teacher_email="17728101016@qq.com",
	teacher_password="9876515"
	)

teach27 = Teacher(
	teacher_name="张杰",
	teacher_phone="17728101017",
	teacher_email="17728101017@qq.com",
	teacher_password="9876516"
	)

teach28 = Teacher(
	teacher_name="谢娜那",
	teacher_phone="18728101017",
	teacher_email="18728101017@qq.com",
	teacher_password="9876517"
	)

teach29 = Teacher(
	teacher_name="孔明",
	teacher_phone="18728101018",
	teacher_email="18728101018@qq.com",
	teacher_password="9876818"
	)

teach30 = Teacher(
	teacher_name="曹植",
	teacher_phone="18728101019",
	teacher_email="18728101019@qq.com",
	teacher_password="9876819"
	)

teach31 = Teacher(
	teacher_name="严格",
	teacher_phone="18728101020",
	teacher_email="18728101020@qq.com",
	teacher_password="9876820"
	)

teach32 = Teacher(
	teacher_name="华画",
	teacher_phone="18728101021",
	teacher_email="18728101021@qq.com",
	teacher_password="9876821"
	)

teach33 = Teacher(
	teacher_name="金世佳",
	teacher_phone="18728101022",
	teacher_email="18728101022@qq.com",
	teacher_password="9876822"
	)

teach34 = Teacher(
	teacher_name="魏延",
	teacher_phone="18728101023",
	teacher_email="18728101023@qq.com",
	teacher_password="9876823"
	)

teach35 = Teacher(
	teacher_name="姜凉生",
	teacher_phone="18728101024",
	teacher_email="18728101024@qq.com",
	teacher_password="9876824"
	)

teach36 = Teacher(
	teacher_name="戚薇",
	teacher_phone="18728101025",
	teacher_email="18728101025@qq.com",
	teacher_password="9876825"
	)

teach37 = Teacher(
	teacher_name="谢逊",
	teacher_phone="18728101026",
	teacher_email="18728101026@qq.com",
	teacher_password="9876826"
	)

teach38 = Teacher(
	teacher_name="唐伯虎",
	teacher_phone="18728101027",
	teacher_email="18728101027@qq.com",
	teacher_password="9876827"
	)

teach39 = Teacher(
	teacher_name="秋香",
	teacher_phone="18728101028",
	teacher_email="18728101028@qq.com",
	teacher_password="9876828"
	)


L = [teach1, teach2, teach3, teach4, teach5, teach6, teach7, teach8, teach9, teach10,
        teach11, teach12, teach13, teach14, teach15, teach16, teach17, teach18, teach19, teach20,
		teach21, teach22, teach23, teach24, teach27, teach28, teach29, teach30,
		 teach34, teach35, teach36, teach37, teach38, teach39]

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

class1.class_teachers.append(teach1)
class1.class_teachers.append(teach2)
class1.class_teachers.append(teach3)
class1.class_teachers.append(teach4)

class3.class_teachers.append(teach5)
class3.class_teachers.append(teach6)
class3.class_teachers.append(teach7)
class3.class_teachers.append(teach8)

class4.class_teachers.append(teach9)
class4.class_teachers.append(teach10)
class4.class_teachers.append(teach11)
class4.class_teachers.append(teach12)

class5.class_teachers.append(teach13)
class5.class_teachers.append(teach14)
class5.class_teachers.append(teach15)
class5.class_teachers.append(teach16)

class6.class_teachers.append(teach17)
class6.class_teachers.append(teach18)
class6.class_teachers.append(teach19)
class6.class_teachers.append(teach20)

class7.class_teachers.append(teach21)
class7.class_teachers.append(teach22)
class7.class_teachers.append(teach23)
class7.class_teachers.append(teach24)
class7.class_teachers.append(teach25)

class8.class_teachers.append(teach26)
class8.class_teachers.append(teach27)
class8.class_teachers.append(teach28)
class8.class_teachers.append(teach29)

class9.class_teachers.append(teach30)
class9.class_teachers.append(teach31)
class9.class_teachers.append(teach32)
class11.class_teachers.append(teach33)

class10.class_teachers.append(teach34)
class10.class_teachers.append(teach35)
class10.class_teachers.append(teach36)
class10.class_teachers.append(teach37)
class11.class_teachers.append(teach38)
class11.class_teachers.append(teach39)

db_session.add(class1)
db_session.add(class2)
db_session.add(class3)
db_session.add(class4)
db_session.add(class5)
db_session.add(class6)
db_session.add(class7)
db_session.add(class8)
db_session.add(class9)
db_session.add(class10)
db_session.add(class11)

db_session.commit()