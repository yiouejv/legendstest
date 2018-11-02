# coding=utf-8
from config import Base, session as db_session
from sqlalchemy import Column, String, Boolean, ForeignKey, Integer,\
    Table, DateTime, Text
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

'''
    班级和老师的关系： 多对多的关系
    班级和学生的关系： 一对多的关系
    老师和学生的关系： 多对多的关系
'''


class_teacher = Table(
    'class_teacher',
    Base.metadata,
    Column('class_id', Integer, ForeignKey('class.class_id'), primary_key=True),
    Column('teacher_id', Integer, ForeignKey('teacher.teacher_id'), primary_key=True)
)


class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(50), nullable=False)

    class_teachers = relationship('Teacher', backref=backref('teacher_class'), secondary=class_teacher)

    def __repr__(self):
        return "%s" % self.class_name


class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String(50), nullable=False)
    teacher_phone = Column(String(11), nullable=False, unique=True)
    teacher_email = Column(String(50), nullable=False, unique=True)
    _teacher_password = Column(String(100), nullable=False)
    teacher_is_delete = Column(Boolean, default=False)
    teacher_create_time = Column(DateTime, default=datetime.now)

    @property
    def teacher_password(self):
        return self._teacher_password

    @teacher_password.setter
    def teacher_password(self, raw_teacher_password):
        self._teacher_password = generate_password_hash(raw_teacher_password)

    def check_teacher_password(self, raw_teacher_password):
        result = check_password_hash(self.teacher_password, raw_teacher_password)
        return result


student_teacher = Table(
    'student_teacher',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('student.student_id'), primary_key=True),
    Column('teacher_id', Integer, ForeignKey('teacher.teacher_id'), primary_key=True)
)


class Student(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(50), nullable=False)
    student_phone = Column(String(11), nullable=False)
    student_email = Column(String(50), nullable=False)
    _student_password = Column(String(100), nullable=False)
    student_is_delete = Column(Boolean, default=False)
    student_create_time = Column(DateTime, default=datetime.now)

    # 外键关联班级
    student_class_id = Column(Integer, ForeignKey('class.class_id'))
    # # 外键关联老师
    student_teacher_id = Column(Integer, ForeignKey('teacher.teacher_id'))
    # 和班级表建立多对一关系
    student_class = relationship('Class', backref='class_students')
    # 和老师表建立多对多关系
    student_teachers = relationship('Teacher', backref=backref('teacher_students'), secondary=student_teacher)

    def __init__(self, student_name, student_phone, student_email, student_password,
                 student_is_delete=None, student_create_time=None):
        self.student_name = student_name
        self.student_phone = student_phone
        self.student_email = student_email
        self.student_password = student_password
        self.student_is_delete = student_is_delete
        self.student_create_time = student_create_time

    @property
    def student_password(self):
        return self._student_password

    @student_password.setter
    def student_password(self, raw_student_password):
        self._student_password = generate_password_hash(raw_student_password)

    def check_student_password(self, raw_student_password):
        result = check_password_hash(self.student_password, raw_student_password)
        return result

'''
    单选题
    简答题
    程序设置题
    试卷-
        试卷和单选题：多对多的关系, 但是单选题不引用试卷的关系
        试卷和简答题：多对多的关系，简答题也一样
        试卷和程序设计题：多对多的关系， 程序设计题也一样
        试卷和成绩：一对一的关系
        试卷和班级：多对多的关系，每份试卷给多个班级使用，每个班级可能考过多份试卷
    成绩
        成绩唯一绑定试卷和学生
        
    考生提交试卷
        student_choice_result
        同一道单选题可以对应多张试卷
        同一道单选题可以对应多个学生的答案
        字段
            student_choice_result_id   # 表id
            student_choice_result_student_id  # 学生id
            student_choice_result_choice_id  # 选择题id  
            student_choice_result_choice_result  # 选择题答案
            student_choice_result_student_choice_result  # 学生选择题的答案
            student_choice_result_choice_score  # 该道选择题得分
        
'''
class StudentChoiceResult(Base):
    '''学生提交的试卷，选择题保存模型'''
    __tablename__ = 'student_choice_result'
    student_choice_result_id = Column(Integer, primary_key=True, autoincrement=True)
    student_choice_result_student_id = Column(Integer, nullable=False)
    student_choice_result_test_pager_id = Column(Integer, nullable=False)
    student_choice_result_choice_id = Column(Integer, nullable=False)
    student_choice_result_student_choice_result = Column(String(1), nullable=False)
    student_choice_result_choice_result = Column(String(1), nullable=False)
    student_choice_result_choice_score = Column(String(5), default=0)


class StudentShortAnswerResult(Base):
    '''学生提交的试卷, 简答题保存模型'''
    __tablename__ = 'student_short_answer_result'
    student_short_answer_result_id = Column(Integer, primary_key=True, autoincrement=True)
    student_short_answer_student_id = Column(Integer, nullable=False)  # 考生id
    student_short_answer_test_pager_id = Column(Integer, nullable=False)
    student_short_answer_short_answer_id = Column(Integer, nullable=False)  # 简答题id
    student_short_answer_student_short_answer_result = Column(String(500), nullable=False)  # 考生作答结果
    student_short_answer_short_answer_result = Column(String(500), nullable=False)  # 简答题答案
    student_short_answer_score = Column(String(5), default=0)  # 考生得分


class StudentProgramResult(Base):
    '''学生提交的试卷, 简答题保存模型'''
    __tablename__ = 'student_program_result'
    student_program_result_id = Column(Integer, primary_key=True, autoincrement=True)
    student_program_student_id = Column(Integer, nullable=False)  # 考生id
    student_program__test_pager_id = Column(Integer, nullable=False)
    student_program_program_id = Column(Integer, nullable=False)  # 程序题id
    student_program_student_result = Column(String(500), nullable=False)  # 考生作答结果
    student_program_result = Column(String(500), nullable=False)  # 程序题答案
    student_program_score = Column(String(5), default=0)  # 考生得分


class ShortAnswer(Base):
    '''简答题模型'''
    __tablename__ = 'short_answer'
    short_answer_id = Column(Integer, primary_key=True, autoincrement=True)
    short_answer_type = Column(String(50), default='python')
    short_answer_content = Column(Text, nullable=False)  # 题干
    short_answer_result = Column(Text, nullable=False)  # 答案
    short_answer_create_time = Column(DateTime, default=datetime.now)
    short_answer_update_time = Column(DateTime, default=datetime.now)


class Choice(Base):
    '''单选题模型'''
    __tablename__ = 'choice'
    choice_id = Column(Integer, primary_key=True, autoincrement=True)
    choice_type = Column(String(50), default='python')
    choice_content = Column(Text, nullable=False)  # 题干
    choice_option_A = Column(Text, nullable=False)  # 选项A的内容
    choice_option_B = Column(Text, nullable=False)  # 选项B的内容
    choice_option_C = Column(Text, nullable=False)  # 选项C的内容
    choice_option_D = Column(Text, nullable=False)  # 选项D的内容
    choice_result = Column(String(1), nullable=False)
    choice_parse = Column(String(500))
    short_answer_create_time = Column(DateTime, default=datetime.now)
    short_answer_update_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "%s" % self.choice_id


class Program(Base):
    '''程序设计题模型'''
    __tablename__ = 'program'
    program_id = Column(Integer, primary_key=True, autoincrement=True)
    program_type = Column(String(50), default='python')
    program_content = Column(Text, nullable=False)  # 题干
    program_result = Column(Text, nullable=False)  # 答案
    program_create_time = Column(DateTime, default=datetime.now)
    program_update_time = Column(DateTime, default=datetime.now)


class Score(Base):
    '''成绩表模型'''
    __tablename__ = 'score'
    score_id = Column(Integer, primary_key=True, autoincrement=True)
    score_student_socre = Column(Integer, default=0)  # 考试成绩
    score_state = Column(String(10), default='未参加考试')

    score_student_id = Column(Integer, ForeignKey('student.student_id'))
    score_test_pager_id = Column(Integer, ForeignKey('test_pager.test_pager_id'))

    socre_test_pager = relationship('TestPager')
    socre_student = relationship('Student')


test_pager_class = Table(
    'test_pager_class',
    Base.metadata,
    Column('test_pager_id', Integer, ForeignKey('test_pager.test_pager_id'), primary_key=True),
    Column('class_id', Integer, ForeignKey('class.class_id'), primary_key=True)
)

test_pager_choice = Table(
    'test_pager_choice',
    Base.metadata,
    Column('test_pager_id', Integer, ForeignKey('test_pager.test_pager_id'), primary_key=True),
    Column('choice_id', Integer, ForeignKey('choice.choice_id'), primary_key=True)
)

test_pager_short_answer = Table(
    'test_pager_short_answer',
    Base.metadata,
    Column('short_answer_id', Integer, ForeignKey('short_answer.short_answer_id'), primary_key=True),
    Column('test_pager_id', Integer, ForeignKey('test_pager.test_pager_id'), primary_key=True)
)


test_pager_program = Table(
    'test_pager_program',
    Base.metadata,
    Column('program_id', Integer, ForeignKey('program.program_id'), primary_key=True),
    Column('test_pager_id', Integer, ForeignKey('test_pager.test_pager_id'), primary_key=True)
)


class TestPager(Base):
    '''试卷模型'''
    __tablename__ = 'test_pager'
    test_pager_id = Column(Integer, primary_key=True, autoincrement=True)
    test_pager_type = Column(String(50), default='python')
    test_pager_name = Column(String(50), nullable=False)  # 考试名称
    test_pager_total_score = Column(Integer)
    test_pager_create_time = Column(DateTime, default=datetime.now)  # 生成试卷的时间
    test_pager_test_time = Column(DateTime, nullable=True)  # 学生参加考试的时间
    test_pager_publish = Column(Boolean, default=False)  # 试卷是否发布，默认不发布

    # 每种题型的个数
    test_pager_choice_num = Column(Integer)
    test_pager_short_answer_num = Column(Integer)
    test_pager_program_num = Column(Integer)

    # 每种题型的分值
    test_pager_choice_score = Column(Integer)
    test_pager_short_answer_score = Column(Integer)
    test_pager_program_score = Column(Integer)

    test_pager_classes = relationship('Class', backref=backref('class_test_pagers'), secondary=test_pager_class, lazy='dynamic')
    test_pager_choices = relationship('Choice', secondary=test_pager_choice)
    test_pager_short_answers = relationship('ShortAnswer', secondary=test_pager_short_answer)
    test_pager_programs = relationship('Program', secondary=test_pager_program)


if __name__ == '__main__':
    Base.metadata.drop_all()
    Base.metadata.create_all()
    #### 老师学生班级三表关系测试
    # class1 = Class(class_name='AID1807')
    # teacher1 = Teacher(teacher_name='于中磊', teacher_phone='15866668888', teacher_email='yuzhonglei@tude.com',
    #                      teacher_password='123456'
    # )
    # teacher2 = Teacher(teacher_name='邓莉莉', teacher_phone='18888886666', teacher_email='denglili@tude.com',
    #                    teacher_password='123456'
    #                    )
    # student1 = Student(student_name='杨文俊', student_email='yiouejv@126.com', student_phone='15210212773',
    #                    student_password='123456'
    #                    )
    # student2 = Student(student_name='林祖宏', student_email='linzuhong@126.com', student_phone='15211212773',
    #                    student_password='123456'
    #                    )
    # class1.class_teachers.append(teacher1)
    # class1.class_teachers.append(teacher2)
    # student1.student_teachers.append(teacher1)
    # student1.student_teachers.append(teacher2)
    # student1.student_class = class1
    # db_session.add(student1)
    # db_session.commit()
    #
    # stu = db_session.query(Student)[:1][0]
    # print(stu.student_teachers)
    # print(stu.student_class)
    # cls = db_session.query(Class)[:1][0]
    # print(cls.class_students)
    # print(cls.class_teachers)
    # teach = db_session.query(Teacher)[:1][0]
    # print(teach.teacher_students)
    # print(teach.teacher_class)
    #### 老师学生班级三表关系测试结束
    #### 试卷和班级关系测试
    # test_pager1 = TestPager(test_pager_name='2018年09月-AID1807-月考',
    #                        test_pager_total_score=100, test_pager_test_time="2018-09-27 18:27:20")
    # test_pager2 = TestPager(test_pager_name='2018年08月-AID1807-月考',
    #                         test_pager_total_score=100, test_pager_test_time="2018-08-31 18:27:20")
    # class1 = Class(class_name='AID1807')
    # class1.class_test_pagers.append(test_pager1)
    # class1.class_test_pagers.append(test_pager2)
    # db_session.add(class1)
    # db_session.commit()
    #### 试卷和班级关系测试结束
    #### 试卷和单选题测试
    # test_pager1 = TestPager(test_pager_name='2018年09月-AID1807-月考',
    #                        test_pager_total_score=100, test_pager_test_time="2018-09-27 18:27:20")
    # choice1 = Choice(choice_content='timu', choice_option_A='aaa', choice_option_B='bbb',
    #                  choice_option_C='ccc', choice_option_D='ddd', choice_result='A')
    # choice2 = Choice(choice_content='timu', choice_option_A='aaa', choice_option_B='bbb',
    #                  choice_option_C='ccc', choice_option_D='ddd', choice_result='B')
    # test_pager1.test_pager_choices.append(choice1)
    # test_pager1.test_pager_choices.append(choice2)
    # db_session.add(test_pager1)
    # db_session.commit()
    #
    # test_pager1 = db_session.query(TestPager).first()
    # print(test_pager1)
    # print(test_pager1.test_pager_choices)
    #### 试卷和单选题测试结束

    ### 试卷和简答题测试
    # test_pager1 = TestPager(test_pager_name='2018年09月-AID1807-月考',
    #                        test_pager_total_score=100, test_pager_test_time="2018-09-27 18:27:20")
    # short_answer1 = ShortAnswer(short_answer_content='简答题', short_answer_result='dsadsadsad')
    # short_answer2 = ShortAnswer(short_answer_content='简答题', short_answer_result='dsadsadsad')
    # test_pager1.test_pager_short_answers.append(short_answer1)
    # test_pager1.test_pager_short_answers.append(short_answer2)
    #
    # db_session.add(test_pager1)
    # db_session.commit()
    #
    # test_pager1 = db_session.query(TestPager).first()
    # print(test_pager1)
    # print(test_pager1.test_pager_short_answers)
    ### 试卷和简答题测试结束
    ### 试卷和程序设计题测试
    # test_pager1 = TestPager(test_pager_name='2018年09月-AID1807-月考',
    #                        test_pager_total_score=100, test_pager_test_time="2018-09-27 18:27:20")
    # program1 = Program(program_content='题目', program_result='dsadsa')
    # program2 = Program(program_content='题目', program_result='dsadsa')
    # test_pager1.test_pager_programs.append(program1)
    # test_pager1.test_pager_programs.append(program2)
    # db_session.add(test_pager1)
    # db_session.commit()
    #
    # test_pager1 = db_session.query(TestPager).first()
    # print(test_pager1)
    # print(test_pager1.test_pager_programs)
    ### 试卷和程序设计题测试结束

    ### 试卷和分数测试
    # test_pager1 = TestPager(test_pager_name='2018年09月-AID1807-月考',
    #                        test_pager_total_score=100, test_pager_test_time="2018-09-27 18:27:20")
    # score = Score(score_student_socre=100)
    # score.socre_test_pager = test_pager1
    # db_session.add(score)
    # db_session.commit()
    #
    # score = db_session.query(Score).first()
    # print(score)
    # print(score.socre_test_pager)
    ### 试卷和分数测试结束

    student = Student(student_name='杨文俊', student_phone='15210212773', student_email='yiouejv@126.com',
                    student_password='123456')
    student.student_class = Class(class_name='AID1087')
    db_session.add(student)
    db_session.commit()
    pass

