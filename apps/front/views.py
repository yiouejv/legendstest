#encoding: utf-8

from flask import Blueprint, render_template, views, request, g, redirect,\
    url_for, session
from apps.front.forms import LoginForm, AddChoiceFrom, AddShortAnswerForm, \
    AddProgramForm, PostTestPagerForm, AddTestPagerForm
from config import session as db_session
from apps.front.models import Student, Teacher, Choice, ShortAnswer, Program,\
    TestPager, Class, Score, StudentChoiceResult, StudentProgramResult, \
    StudentShortAnswerResult
import config
from apps.front.decorators import student_login_required, teacher_login_required
from sqlalchemy import func


front_bp = Blueprint('front', __name__)


@front_bp.route('/')
def index():
    return redirect(url_for("front.student_login"))


@front_bp.route("/login_out/")
@student_login_required
def login_out():
    del session[config.STUDENT_EMAIL]
    return redirect(url_for("front.student_login"))


class StudentLoginView(views.MethodView):
    def __render(self, error=None):
        return render_template('front/front_student_login.html', error=error)

    def get(self):
        return self.__render()

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = request.form.get('email')
            password = request.form.get('password')
            remember = request.form.get('remember')
            user = db_session.query(Student).filter(Student.student_email == email).first()
            if user:
                if user.check_student_password(password):
                    session[config.STUDENT_EMAIL] = user.student_email
                    # 如果勾选了自动登陆
                    if remember:
                        session.permanent = True
                    return redirect(url_for("front.exam"))
                else:
                    return self.__render("密码不正确，请重新输入")
            else:
                return self.__render("用户不存在，请检查邮箱是否输入正确")
        else:
            errors = form.errors
            error = errors.popitem()[1][0]
            return self.__render(error)


class TeacherLoginView(views.MethodView):
    def __render(self, error=None):
        return render_template("front/front_teacher_login.html", error=error)

    def get(self):
        return self.__render()

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = request.form.get('email')
            password = request.form.get('password')
            remember = request.form.get('remember')
            user = db_session.query(Teacher).filter(Teacher.teacher_email == email).first()
            if user:
                if user.check_teacher_password(password):
                    session[config.TEACHER_EMAIL] = user.teacher_email
                    # 如果勾选了自动登陆
                    if remember:
                        session.permanent = True
                    return redirect(url_for('front.teacher_info'))
                else:
                    return self.__render("密码不正确，请重新输入")
            else:
                return self.__render("用户不存在，请检查邮箱是否输入正确")
        else:
            errors = form.errors
            error = errors.popitem()[1][0]
            return self.__render(error)


class ExamView(views.MethodView):
    decorators = [student_login_required]
    def get(self):
        user = db_session.query(Student).filter(Student.student_email==g.student_user.student_email).first()
        Scores = db_session.query(Score).filter(Score.score_student_id==user.student_id).all()
        return render_template('front/front_exam.html', Scores=Scores)


class StudentCenterView(views.MethodView):
    decorators = [student_login_required]
    def get(self):
        return render_template('front/front_student_center.html')


@front_bp.route('/teacher_info/')
@teacher_login_required
def teacher_info():
    return render_template("front/front_teacher_info.html")


@front_bp.route('/teacher_logout/')
@teacher_login_required
def teacher_logout():
    del session[config.TEACHER_EMAIL]
    return redirect(url_for('front.teacher_login'))


# 注册url规则
front_bp.add_url_rule('/student_login/', view_func=StudentLoginView.as_view('student_login'))
front_bp.add_url_rule('/teacher_login/', view_func=TeacherLoginView.as_view('teacher_login'))
front_bp.add_url_rule('/exam/', view_func=ExamView.as_view('exam'))
front_bp.add_url_rule('/studentCenter/', view_func=StudentCenterView.as_view('studentCenter'))


class TeacherAddChoiceView(views.MethodView):
    def __render(self, message=None):
        return render_template("front/front_add_choice.html", message=message)

    decorators = [teacher_login_required]
    def get(self):
        return self.__render()

    def post(self):
        form = AddChoiceFrom(request.form)
        if form.validate():
            type = form.type.data
            content = form.content.data
            option_A = form.option_A.data
            option_B = form.option_B.data
            option_C = form.option_C.data
            option_D = form.option_D.data
            result = form.result.data
            parse = form.parse.data
            choice = Choice(choice_type=type, choice_content=content, choice_option_A=option_A,
                            choice_option_B=option_B, choice_option_C=option_C, choice_option_D=option_D,
                            choice_result=result, choice_parse=parse)
            db_session.add(choice)
            db_session.commit()
            return self.__render('success')
        else:
            message = form.errors.popitem()[1][0]
            return self.__render(message=message)


class TeacherAddShortAnswer(views.MethodView):
    def __render(self, message=None):
        return render_template("front/front_add_short_answer.html", message=message)

    decorators = [teacher_login_required]
    def get(self):
        return self.__render()

    def post(self):
        form = AddShortAnswerForm(request.form)
        if form.validate():
            type = form.type.data
            content = form.content.data
            result = form.result.data
            short_answer = ShortAnswer(short_answer_type=type, short_answer_content=content, short_answer_result=result)
            db_session.add(short_answer)
            db_session.commit()
            return self.__render('success')
        else:
            message = form.errors.popitem()[1][0]
            return self.__render(message=message)


class TeacherAddProgram(views.MethodView):
    def __render(self, message=None):
        return render_template("front/front_add_program.html", message=message)

    decorators = [teacher_login_required]
    def get(self):
        return self.__render()

    def post(self):
        form = AddProgramForm(request.form)
        if form.validate():
            type = form.type.data
            content = form.content.data
            result = form.result.data
            program = Program(program_type=type, program_content=content, program_result=result)
            db_session.add(program)
            db_session.commit()
            return self.__render('success')
        else:
            message = form.errors.popitem()[1][0]
            return self.__render(message=message)


class AddTestPage(views.MethodView):
    decorators = [teacher_login_required]
    def get(self):
        return render_template('front/front_add_test_page.html')

    def post(self):
        form = AddTestPagerForm(request.form)
        if form.validate():
            # 接收前台数据
            choiceSize = int(request.form["choiceSize"])
            choiceScore = int(request.form["choiceScore"])
            shortAnswerSize = int(request.form["shortAnswerSize"])
            shortAnswerScore = int(request.form["shortAnswerScore"])
            programSize = int(request.form["programSize"])
            programScore = int(request.form["programScore"])
            type = request.form["type"]
            name = request.form['name'].strip()
            # 试卷的总分等于 =
            # 选择器的个数*单个选择题的分值 + 简答题的个数*单个简答题的分值 + 程序设计题的个数*单个程序设计提的分值
            totalscore = (choiceSize*choiceScore) + (shortAnswerSize*shortAnswerScore) + (programSize*programScore)
            count_choice = db_session.query(Choice).filter(Choice.choice_type==type).count()
            count_short_answer = db_session.query(ShortAnswer).filter(ShortAnswer.short_answer_type==type).count()
            count_program = db_session.query(Program).filter(Program.program_type==type).count()
            # 如果数据库选择题的个数小于需要生成的个数
            if count_choice < choiceSize:
                # 把所有的题全部抽出来
                choices = db_session.query(Choice).all()
                message1 = '题库中选择题不够%s个, 现已全部引用' % choiceSize
            # 如果需要生成的选择题的个数小于数据库中存储的数量
            else:
                choices = db_session.query(Choice).order_by(func.rand(Choice.choice_id))[0:choiceSize]
            if count_short_answer < shortAnswerSize:
                short_answers = db_session.query(ShortAnswer).all()
                message2 = '题库中简答题不够%s个, 现已全部引用' % shortAnswerSize
            else:
                short_answers = db_session.query(ShortAnswer).order_by(func.rand(ShortAnswer.short_answer_id))[0:shortAnswerSize]
            if count_program < programSize:
                programs = db_session.query(Program).all()
                message3 = '题库中简答题不够%s个, 现已全部引用' % programSize
            else:
                programs = db_session.query(Program).order_by(func.rand(Program.program_id))[0:programSize]
            # 创建试卷对象
            test_pager = TestPager(test_pager_name=name, test_pager_type=type, test_pager_choice_score=choiceScore,
                                   test_pager_short_answer_score=shortAnswerScore, test_pager_program_score=programScore,
                                   test_pager_choice_num=choiceSize, test_pager_short_answer_num=shortAnswerSize,
                                   test_pager_program_num=programSize, test_pager_total_score=totalscore)
            # 选择题，简答题，程序设计题绑定到试卷中
            test_pager.test_pager_choices.extend(choices)
            test_pager.test_pager_short_answers.extend(short_answers)
            test_pager.test_pager_programs.extend(programs)
            db_session.add(test_pager)
            db_session.commit()
            content = {
                # 'message1': message1,
                # 'message2': message2,
                # 'message3': message3,
                'totalScore': totalscore
            }
            return render_template('front/front_add_test_page.html', **content)
        else:
            message = form.errors.popitem()[1][0]
            return render_template('front/front_add_test_page.html', message=message)


front_bp.add_url_rule('/add_choice/', view_func=TeacherAddChoiceView.as_view('add_choice'))
front_bp.add_url_rule('/add_short_answer/', view_func=TeacherAddShortAnswer.as_view('add_short_answer'))
front_bp.add_url_rule('/add_program/', view_func=TeacherAddProgram.as_view('add_program'))
front_bp.add_url_rule('/add_test_page/', view_func=AddTestPage.as_view('add_test_page'))


@front_bp.route('/manager_choice/<int:page>/')
@teacher_login_required
def manager_choice(page):
    start = (page - 1) * config.ChOICE_PAGE_SIZE
    stop = start + config.ChOICE_PAGE_SIZE
    choices = db_session.query(Choice)[start:stop]
    total = len(choices)
    content = {
        'choices': choices,
        'page': page,
        'total': total,
        'ChOICE_PAGE_SIZE': config.ChOICE_PAGE_SIZE
    }
    return render_template('front/front_manager_choice.html', **content)


@front_bp.route('/manager_short_answer/<int:page>/')
@teacher_login_required
def manager_short_answer(page):
    start = (page - 1) * config.SHORT_ANSWER_SIZE
    stop = start + config.SHORT_ANSWER_SIZE
    short_answers = db_session.query(ShortAnswer)[start:stop]
    total = len(short_answers)
    content = {
        'short_answers': short_answers,
        'page': page,
        'total': total,
        'SHORT_ANSWER_SIZE':config.SHORT_ANSWER_SIZE
    }
    return render_template('front/front_manager_short_answer.html', **content)


@front_bp.route('/manager_program/<int:page>/')
@teacher_login_required
def manager_program(page):
    start = (page - 1) * config.PROGRAM_SIZE
    stop = start + config.PROGRAM_SIZE
    programs = db_session.query(Program)[start:stop]
    total = len(programs)
    content = {
        'programs': programs,
        'page': page,
        'total': total,
        'PROGRAM_SIZE':config.PROGRAM_SIZE
    }
    return render_template('front/front_manager_program.html', **content)


@front_bp.route('/manager_test_pager/<int:page>/')
@teacher_login_required
def manager_test_pager(page):
    start = (page - 1) * config.TEST_PAGER_SIZE
    stop = start + config.TEST_PAGER_SIZE
    test_pagers = db_session.query(TestPager)[start:stop]
    total = len(test_pagers)
    class_names = [class_.class_name for class_ in g.teacher_user.teacher_class]
    classes = []
    for class_name in class_names:
        classs = db_session.query(Class).filter(Class.class_name==class_name).all()
        classes.extend(classs)
    for class_ in classes:
        # 如果此班级的学生人数为0，则发布试卷可选班级则不显示此班级
        if not class_.class_students:
            classes.remove(class_)
    classes = [class_.class_name for class_ in classes]
    # 去掉重复的班级名
    classes = list(set(classes))
    content = {
        'test_pagers': test_pagers,
        'page': page,
        'total': total,
        'TEST_PAGER_SIZE': config.TEST_PAGER_SIZE,
        'classes': classes
    }
    return render_template('front/front_manager_test_pager.html', **content)


@front_bp.route('/post_test_pager/', methods=['POST'])
@teacher_login_required
def post_test_pager():
    form = PostTestPagerForm(request.form)
    if form.validate():
        id = form.id.data
        test_time = form.test_time.data
        test_class = form.test_class.data
        test_pager = db_session.query(TestPager).filter(TestPager.test_pager_id==id).first()
        if test_pager:
            try:
                # 编辑试卷
                test_pager.test_pager_test_time = test_time
                test_pager.test_pager_publish = True
                # 考试时间可能设置不满足时间条件
                test_pager.test_pager_classes.append(Class(class_name=test_class))
                db_session.commit()
                # 将试卷信息绑定到班级的学生中
                classes = db_session.query(Class).filter(Class.class_name == test_class).all()
                testPagers = []  # 创建一个列表，用来保存试卷，往前端页面传
                for cls in classes:
                    testPagers.extend(cls.class_test_pagers)
                for cls in classes:
                    if cls.class_test_pagers is not []:  # 存在班级试卷
                        stus = cls.class_students
                        if stus:
                            # 遍历学生，为每个学生绑定上试卷
                            for stu in stus:
                                # 遍历试卷，绑定多份试卷于学生
                                for pager in testPagers:
                                    # 添加本次发布的试卷，避免重复添加数据库
                                    if pager.test_pager_id == int(id):
                                        score = Score(score_test_pager_id=pager.test_pager_id,
                                                      score_student_id=stu.student_id)
                                        db_session.add(score)
                db_session.commit()
                return 'success'
            except Exception as err:
                return '考试时间不合法'
        else:
            return '数据中不存在本张试卷'
    else:
        message = form.errors.popitem()[1][0]
        return  message


class StudentExamPager(views.MethodView):
    decorators = [student_login_required]
    def get(self, test_pager_id=1):
        score = db_session.query(Score).filter(Score.score_student_id == g.student_user.student_id, Score.score_test_pager_id==test_pager_id).first()
        return render_template('front/front_student_exam_pager.html', score=score)

    def post(self, test_pager_id):
        form = request.form
        student_id = g.student_user.student_id
        # 遍历form字典,取出所有的选择题存在数据库中的编号,以及学生所选的选项
        # 返回新的字典---->(选择题id: 学生作答的选项)
        choices = {}  # 创建空字典
        for key in form:
            # 截取前6个字符判断是不是选择题
            if key[:6] == 'choice':
                choice_id = key[6:]
                value = form[key]
                choices[choice_id] = value
        # 遍历选择题,把所有的选择题存入student_choice_result表中
        for choice_id in choices:
            # 以choice_id为条件,查询选择题正确的答案
            cho = db_session.query(Choice).filter(Choice.choice_id==choice_id).first()
            student_choice_result = StudentChoiceResult(
                student_choice_result_student_id=student_id,
                student_choice_result_test_pager_id=test_pager_id,
                student_choice_result_choice_id = choice_id,
                student_choice_result_student_choice_result = value,
                student_choice_result_choice_result = cho.choice_result
            )
            db_session.add(student_choice_result)

        short_answers = {}
        for key in form:
            if key[:3] == 'elm':
                short_answer_id = key[3:]
                short_answers[short_answer_id] = form[key]
        for short_answer_id in short_answers:
            short = db_session.query(ShortAnswer).filter(ShortAnswer.short_answer_id==short_answer_id).first()
            shortA = StudentShortAnswerResult(
                student_short_answer_student_id = student_id,
                student_short_answer_test_pager_id = test_pager_id,
                student_short_answer_short_answer_id = short_answer_id,
                student_short_answer_student_short_answer_result = short_answers[short_answer_id],
                student_short_answer_short_answer_result = short.short_answer_result
            )
            db_session.add(shortA)

        programs = {}
        for key in form:
            if key[:4] == 'code':
                program_id = key[4:]
                programs[program_id] = form[key]
        for program_id in programs:
            pro = db_session.query(Program).filter(Program.program_id==program_id).first()
            pro_ = StudentProgramResult(
                student_program_student_id = student_id,
                student_program__test_pager_id = test_pager_id,
                student_program_program_id = program_id,
                student_program_student_result = programs[program_id],
                student_program_result = pro.program_result
            )
            db_session.add(pro_)
        # 试卷考完后, 分数绑定试卷的
        score = db_session.query(Score).filter(Score.score_student_id==student_id, Score.score_test_pager_id==test_pager_id).first()
        if score:
            score.score_state = '等待阅卷'
            db_session.commit()
            return redirect(url_for("front.exam"))
        else:
            return self.get()


class TeacherExamList(views.MethodView):
    '''老师查看要批改的试卷列表
        由老师所在班级获取班级内学生，由学生拿到学生的考卷
    '''
    decorators = [teacher_login_required]
    def get(self):
        teacher_id = g.teacher_user.teacher_id
        teacher = db_session.query(Teacher).filter(Teacher.teacher_id==teacher_id).first()
        classes = teacher.teacher_class
        classs = []  # 保存班级的名字
        for class_ in classes:
            clss = db_session.query(Class).filter(Class.class_name==class_.class_name).all()
            classs.extend(clss)

        # 老师可能管理多个班级，classs 是一个class对象列表
        # 遍历列表找出所有classs班级中的学生，存储在列表students中
        students = []
        for class_ in classs:
            stus = db_session.query(Student).filter(Student.student_class==class_).all()
            students.extend(stus)

        # 通过学生拿到学生的考卷
        scores = []
        for student in students:
            scos = db_session.query(Score).filter(Score.socre_student==student, Score.score_state=='等待阅卷').all()
            scores.extend(scos)
        content = {
            'scores': scores,
        }
        return render_template("front/front_teacher_exam_list.html", **content)


class TeacherExamTestPager(views.MethodView):
    '''老师批改试卷页面类视图
       由学生id和试卷id拿到学生的考卷，再拿到考卷试题及学生作答
    '''
    decorators = [teacher_login_required]
    def get(self, student_id, test_pager_id):
        stu = db_session.query(Student).filter(Student.student_id==student_id).first()
        score = db_session.query(Score).filter(Score.socre_student==stu, Score.score_test_pager_id==test_pager_id).first()
        # 从数据库中抽取学生答题的结果集
        choice_results = db_session.query(StudentChoiceResult).filter(
            StudentChoiceResult.student_choice_result_student_id == stu.student_id,
            StudentChoiceResult.student_choice_result_test_pager_id == test_pager_id,
        ).all()
        short_answer_results = db_session.query(StudentShortAnswerResult).filter(
            StudentShortAnswerResult.student_short_answer_student_id == student_id,
            StudentShortAnswerResult.student_short_answer_test_pager_id == test_pager_id,
        ).all()
        program_results = db_session.query(StudentProgramResult).filter(
            StudentProgramResult.student_program_student_id == student_id,
            StudentProgramResult.student_program__test_pager_id == test_pager_id,
        ).all()
        content = {
            'score': score,
            'choice_results': choice_results,
            'short_answer_results': short_answer_results,
            'program_results': program_results,
        }
        return render_template('front/front_teacher_exam_pager.html', **content)

    def post(self, student_id, test_pager_id):
        '''把分数表的学生得分改为学生的实际得分
            再把学生对应的每道题的得分存入到对应的学生答案表中
        '''
        form = request.form
        # 创建三个字典，键为题目的id号，值为该题得分
        choice_score = {}  # {"choice_id": 'score'}
        short_answer_score = {}  # {'short_answer_id':'score'}
        program_score = {}  # {'program_id':'score'}
        for item in form:
            # 判断表单项是选择题
            if item[:6] == 'choice':
                choice_score[item[6:]] = int(form[item])
            elif item[:12] == 'short_answer':
                short_answer_score[item[12:]] = int(form[item])
            elif item[:7] == 'program':
                program_score[item[7:]] = int(form[item])
        score = db_session.query(Score).filter(
            Score.score_student_id==student_id,
            Score.score_test_pager_id==test_pager_id
        ).first()
        # 合计学生的总分
        score.score_student_socre = sum(map(sum, ([
            [score for score in choice_score.values()],
            [score for score in short_answer_score.values()],
            [score for score in program_score.values()],
        ])))
        score.score_state = '已经批阅'
        #  保存学生答案表中学生具体每道题的得分
        for choice_id in choice_score:
            choice = db_session.query(StudentChoiceResult).filter(
                StudentChoiceResult.student_choice_result_student_id == student_id,
                StudentChoiceResult.student_choice_result_test_pager_id == test_pager_id,
                StudentChoiceResult.student_choice_result_choice_id == choice_id
            ).first()
            choice.student_choice_result_choice_score = choice_score[choice_id]
            db_session.commit()
        for short_answer_id in short_answer_score:
            short_answer = db_session.query(StudentShortAnswerResult).filter(
                StudentShortAnswerResult.student_short_answer_student_id == student_id,
                StudentShortAnswerResult.student_short_answer_test_pager_id == test_pager_id,
                StudentShortAnswerResult.student_short_answer_short_answer_id == short_answer_id,
            ).first()
            short_answer.student_short_answer_score = short_answer_score[short_answer_id]
            db_session.commit()
        for program_id in program_score:
            program = db_session.query(StudentProgramResult).filter(
                StudentProgramResult.student_program_student_id == student_id,
                StudentProgramResult.student_program__test_pager_id == test_pager_id,
                StudentProgramResult.student_program_program_id == program_id,
            ).first()
            program.student_program_score = program_score[program_id]
            db_session.commit()
        return redirect(url_for('front.teacher_exam_list', page=1))


class StudentViewTestPager(views.MethodView):
    decorators = [student_login_required]
    def get(self, test_pager_id):
        '''老师批阅以后，学生查看自己的试卷详情'''
        stu = db_session.query(Student).filter(Student.student_id == g.student_user.student_id).first()
        score = db_session.query(Score).filter(Score.socre_student == stu,
                                               Score.score_test_pager_id == test_pager_id).first()
        # 从数据库中抽取学生答题的结果集
        choice_results = db_session.query(StudentChoiceResult).filter(
            StudentChoiceResult.student_choice_result_student_id == g.student_user.student_id,
            StudentChoiceResult.student_choice_result_test_pager_id == test_pager_id,
        ).all()
        short_answer_results = db_session.query(StudentShortAnswerResult).filter(
            StudentShortAnswerResult.student_short_answer_student_id == g.student_user.student_id,
            StudentShortAnswerResult.student_short_answer_test_pager_id == test_pager_id,
        ).all()
        program_results = db_session.query(StudentProgramResult).filter(
            StudentProgramResult.student_program_student_id == g.student_user.student_id,
            StudentProgramResult.student_program__test_pager_id == test_pager_id,
        ).all()
        # 拿到学生对应题目的得分
        content = {
            'score': score,
            'choice_results': choice_results,
            'short_answer_results': short_answer_results,
            'program_results': program_results,
        }
        return render_template('front/front_student_view_exam_pager.html', **content)


class ManagerScore(views.MethodView):
    '''成绩管理视图, 展示学生的成绩及试卷状态等信息
        # 通过老师登陆信息,查找到老师所在班级,由班级查找出所有学生,找到学生分数信息
        展示所有的学生信息
    '''
    decorators = [teacher_login_required]
    def get(self, page):
        teacher = g.teacher_user
        start = (page - 1) * config.SCORE_PAGER_SIZE
        stop = start + config.SCORE_PAGER_SIZE
        scores = db_session.query(Score)[start:stop]
        total = len(scores)
        content = {
            'scores': scores,
            'total': total,
            'page': page,
            'SCORE_PAGER_SIZE': config.SCORE_PAGER_SIZE
        }
        return render_template('front/front_manager_score.html', **content)


front_bp.add_url_rule('/student_exam_pager/<int:test_pager_id>', view_func=StudentExamPager.as_view('student_exam_pager'))
front_bp.add_url_rule('/teacher_exam_list/', view_func=TeacherExamList.as_view('teacher_exam_list'))
front_bp.add_url_rule("/teacher_exam_pager/<int:student_id>/<test_pager_id>/", view_func=TeacherExamTestPager.as_view('teacher_exam_pager'))
front_bp.add_url_rule("/student_view_exam_pager/<test_pager_id>/", view_func=StudentViewTestPager.as_view('front_student_view_exam_pager'))
front_bp.add_url_rule("/manager_score/<int:page>/", view_func=ManagerScore.as_view('manager_score'))


# 更改题目视图函数
@front_bp.route('/update_choice/', methods=["POST"])
@teacher_login_required
def update_choice():
    form = request.form
    try:
        choice = db_session.query(Choice).filter(Choice.choice_id==form['choiceId']).first()
        choice.choice_content = form.get('choiceContent')
        choice.choice_option_A = form.get('choiceA')
        choice.choice_option_B = form.get('choiceB')
        choice.choice_option_C = form.get('choiceC')
        choice.choice_option_D = form.get('choiceD')
        choice.choice_result = form.get('choiceResult')
        db_session.commit()
        return 'success'
    except Exception as err:
        return 'fail'


@front_bp.route('/update_short_answer/', methods=['POST'])
@teacher_login_required
def update_short_answer():
    form = request.form
    try:
        short_answer = db_session.query(ShortAnswer).filter(ShortAnswer.short_answer_id==form.get('id')).first()
        short_answer.short_answer_content = form.get("content")
        short_answer.short_answer_result = form.get("result")
        db_session.commit()
        return 'success'
    except Exception as err:
        return 'fail'


@front_bp.route('/update_program/', methods=['POST'])
@teacher_login_required
def update_program():
    form = request.form
    try:
        program = db_session.query(Program).filter(Program.program_id==form.get('id')).first()
        program.program_content = form.get("content")
        program.program_result = form.get("result")
        db_session.commit()
        return 'success'
    except Exception as err:
        return 'fail'


# @front_bp.route("/del_choice/", methods=["POST"])
# def del_choice():
#     choice_id = request.form.get("choiceId")
#     choice = db_session.query(Choice).filter(Choice.choice_id==choice_id).first()
#     if choice:
#         db_session.delete(choice)
#         return 'success'
#     return 'fail'


# 分数计算器
@front_bp.app_template_filter(name='choiceTotalScore')
def choiceScore(choiceScore, num):
    '''考试界面选择题总分统计过滤器
        用于统计选择题的总分
        choiceScore：选择题分值
        num: 选择题个数
    '''
    return choiceScore*num


@front_bp.app_template_filter(name='short_answerTotalScore')
def shortAnswerScore(short_answer_Score, num):
    '''考试界面选择题总分统计过滤器
        用于统计简答的总分
        short_answer_Score：简答题分值
        num: 选择题个数
    '''
    return short_answer_Score*num


@front_bp.app_template_filter(name='programTotalScore')
def programTotalScore(program_Score, num):
    '''考试界面选择题总分统计过滤器
        用于统计简答的总分
        program_Score：程序题分值
        num: 选择题个数
    '''
    return program_Score*num


@front_bp.app_template_filter(name='addOne')
def addOne(self):
    '''自增过滤器， 实现数值的自增'''
    return self + 1


@front_bp.app_template_filter(name='delOne')
def delOne(self):
    '''自增过滤器， 实现数值的自增'''
    return self + 1



