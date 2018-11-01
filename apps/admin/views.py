#encoding: utf-8

from flask import Blueprint, render_template, views, request,\
    session, redirect, url_for, g, jsonify, Response
from apps.admin.forms import LoginForms, ResetPwdForms, AddUserForms,\
    AddTeacherForm, AddStudentForm, UpdateUserForm, UpdateTeacherForm, UpdateStudentForm
from apps.admin.models import Admin
from config import session as db_session
from .decorators import login_required
from apps.front.models import Student, Teacher, Class
import config
from uuid import uuid4

admin_bp = Blueprint('admin', __name__, subdomain='admin')


@admin_bp.route('/')
@login_required
def index():
    return render_template('admin/admin_index.html')


@admin_bp.route('/admin_profile/')
@login_required
def admin_profile():
    return render_template('admin/admin_profile.html')


class LoginView(views.MethodView):
    def __render(self, message=None):
        return render_template('admin/admin_login.html', message=message)

    def get(self):
        return self.__render()

    def post(self):
        form = LoginForms(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = db_session.query(Admin).filter(Admin.admin_email==email).first()
            if user and user.check_admin_password(password):
                session[config.ADMIN_UUID] = user.admin_email
                if remember:
                    # 如果设置session.permanent = True
                    # 那么过期时间为31天
                    session.permanent = True
                return redirect(url_for('admin.index'))
            else:
                return self.__render(message='用户名或密码错误')
        else:
            email_err = form.errors.get('email')
            password_err = form.errors.get('password')
            message = email_err if email_err else password_err
            return self.__render(message=message[0])


class ResetPwdView(views.MethodView):
    def __render(self, message=None):
        return render_template('admin/admin_reset_password.html', message=message)

    decorators = [login_required]
    def get(self):
        return self.__render()

    def post(self):
        form = ResetPwdForms(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.admin_user
            if user.check_admin_password(oldpwd):
                user.admin_password = newpwd
                db_session.commit()
                return self.__render('密码修改成功')
            else:
                return self.__render('旧密码不正确')
        else:
            errors = form.errors
            error = errors.popitem()[1][0]
            return self.__render(error)


class ResetEmailView(views.MethodView):
    def __render(self, message=None):
        return render_template("admin/admin_reset_email.html", message=message)

    decorators = [login_required]
    def get(self):
        return self.__render()

    def post(self):
        return self.__render()


class ManagerUserView(views.MethodView):
    '''提供用户管理视图，每页显示10个用户'''
    decorators = [login_required]
    def get(self, page):
        start = (page - 1) * config.ADMIN_PAGE_SIZE
        stop = start + config.ADMIN_PAGE_SIZE
        users = db_session.query(Admin)[start:stop]
        total = len(users)
        return render_template("admin/admin_manager_user.html", users=users, page=page, total=total)


class ManagerStudentView(ManagerUserView):
    decorators = [login_required]
    def get(self, page):
        start = (page - 1) * config.ADMIN_PAGE_SIZE
        stop = start + config.ADMIN_PAGE_SIZE
        students = db_session.query(Student)[start:stop]
        total = len(students)
        return render_template("admin/admin_manager_student.html", students=students, page=page, total=total)


class ManagerTeacherView(ManagerUserView):
    decorators = [login_required]
    def get(self, page):
        start = (page - 1) * config.ADMIN_PAGE_SIZE
        stop = start + config.ADMIN_PAGE_SIZE
        teachers = db_session.query(Teacher)[start:stop]
        total = len(teachers)
        return render_template("admin/admin_manager_teacher.html", teachers=teachers, page=page, total=total)


class AddUserView(views.MethodView):
    def __render(self, message=None):
        return render_template("admin/admin_add_user.html", message=message)

    decorators = [login_required]
    def get(self):
        return self.__render()

    def post(self):
        form = AddUserForms(request.form)
        if form.validate():
            name = form.name.data
            phone = form.phone.data
            email = form.email.data
            password = form.password.data
            is_super = form.is_super.data
            user = Admin(admin_uuid=str(uuid4()), admin_name=name, admin_phone=phone, admin_email=email, admin_password=password, admin_is_super=is_super)
            db_session.add(user)
            db_session.commit()
            return self.__render(message='恭喜您！用户添加成功')
        else:
            errors = form.errors
            error = errors.popitem()[1][0]
            return self.__render(error)


class SearchUserView(views.MethodView):
    def __render(self, message=None):
        return render_template("admin/admin_search_user.html", message=message)

    decorators = [login_required]
    def get(self):
        return self.__render()

    def post(self):
        return self.__render()


class AddStudentView(AddUserView):
    def __render(self, message=None):
        return render_template("admin/admin_add_student.html", message=message)

    decorators = [login_required]
    def get(self):
        return self.__render()

    def post(self):
        form = AddStudentForm(request.form)
        if form.validate():
            name = form.name.data
            phone = form.phone.data
            email = form.email.data
            password = form.password.data
            class_ = form.class_.data
            stu = Student(student_name=name, student_phone=phone, student_email=email, student_password=password)
            stu.student_class = Class(class_name=class_)
            db_session.add(stu)
            db_session.commit()
            return self.__render(message='恭喜您！用户添加成功')
        else:
            errors = form.errors
            error = errors.popitem()[1][0]
            return self.__render(error)


class AddTeacherView(AddUserView):
    def __render(self, message=None):
        return render_template("admin/admin_add_teacher.html", message=message)

    decorators = [login_required]
    def get(self):
        return self.__render()

    def post(self):
        form = AddTeacherForm(request.form)
        if form.validate():
            name = form.name.data
            phone = form.phone.data
            email = form.email.data
            password = form.password.data
            class_ = form.class_.data
            teach = Teacher(teacher_name=name, teacher_phone=phone, teacher_email=email, teacher_password=password)
            class1 = Class(class_name=class_)
            class1.class_teachers.append(teach)
            db_session.add(teach)
            db_session.commit()
            return self.__render(message='恭喜您！用户添加成功')
        else:
            errors = form.errors
            error = errors.popitem()[1][0]
            return self.__render(error)


admin_bp.add_url_rule('/admin_login/', view_func=LoginView.as_view('admin_login'))
admin_bp.add_url_rule('/admin_reset_password/', view_func=ResetPwdView.as_view('admin_reset_password'))
admin_bp.add_url_rule('/admin_reset_email/', view_func=ResetEmailView.as_view('admin_reset_email'))
admin_bp.add_url_rule('/admin_manager_user/<int:page>/', view_func=ManagerUserView.as_view('admin_manager_user'))
admin_bp.add_url_rule('/admin_manager_student/<int:page>/', view_func=ManagerStudentView.as_view('admin_manager_student'))
admin_bp.add_url_rule('/admin_manager_teacher/<int:page>/', view_func=ManagerTeacherView.as_view('admin_manager_teacher'))
admin_bp.add_url_rule('/admin_add_user/', view_func=AddUserView.as_view('admin_add_user'))
admin_bp.add_url_rule('/admin_search_user/', view_func=SearchUserView.as_view('admin_search_user'))
admin_bp.add_url_rule('/admin_add_student/', view_func=AddStudentView.as_view('admin_add_student'))
admin_bp.add_url_rule('/admin_add_teacher/', view_func=AddTeacherView.as_view('admin_add_teacher'))


@admin_bp.route('/logout/')
@login_required
def logout():
    # 注销删除session信息
    del session[config.ADMIN_UUID]
    return redirect(url_for('admin.admin_login'))


@admin_bp.route('/update_user/', methods=['POST'])
@login_required
def update_user():
    form = UpdateUserForm(request.form)
    if form.validate():
        uid = form.uid.data
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        is_super = form.is_super.data
        user = db_session.query(Admin).filter(Admin.admin_uuid==uid).first()
        required_phone = db_session.query(Admin).filter(Admin.admin_phone==phone)[:]
        required_email = db_session.query(Admin).filter(Admin.admin_email==email)[:]
        if len(required_phone)>1:  # 判断是否本人的手机号码
            return '该手机号已被使用'
        elif len(required_email)>1:
            return '该邮箱已被使用'
        elif len(required_phone)==1 and user.admin_phone != phone:
            return '该手机号已被使用'
        elif len(required_email)==1 and user.admin_email != email:
            return '该邮箱已被使用'
        else:
            user.admin_name = name
            user.admin_email = email
            user.admin_phone = phone
            user.admin_is_super = is_super
            db_session.commit()
        return "success"
    else:
        errors = form.errors
        error = errors.popitem()[1][0]
        return error


@admin_bp.route('/update_teacher/', methods=['POST'])
@login_required
def update_teahcer():
    form = UpdateTeacherForm(request.form)
    if form.validate():
        id = form.id.data
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        class_ = form.class_.data
        user = db_session.query(Teacher).filter(Teacher.teacher_id == id).first()
        required_phone = db_session.query(Teacher).filter(Teacher.teacher_phone == phone)[:]
        required_email = db_session.query(Teacher).filter(Teacher.teacher_email == email)[:]
        if len(required_phone) > 1:  # 判断是否本人的手机号码
            return '该手机号已被使用'
        elif len(required_email) > 1:
            return '该邮箱已被使用'
        elif len(required_phone) == 1 and user.teacher_phone != phone:
            return '该手机号已被使用'
        elif len(required_email) == 1 and user.teacher_email != email:
            return '该邮箱已被使用'
        else:
            user.teacher_name = name
            user.teacher_email = email
            user.teacher_phone = phone
            # 前台传过来的数据格式为：[AID1807,AID1808], 取得AID1807,AID1808字符串
            classes = class_[1:-1]
            class_lst = classes.split(',')
            # 先将该老师的班级置为空
            user.teacher_class = []
            # 遍历班级列表，创建班级对象
            for cls in class_lst:
                cls = Class(class_name=cls.strip())
                user.teacher_class.append(cls)
            db_session.commit()
        return "success"
    else:
        errors = form.errors
        error = errors.popitem()[1][0]
        return error


@admin_bp.route('/update_student/', methods=['POST'])
@login_required
def update_student():
    form = UpdateStudentForm(request.form)
    if form.validate():
        id = form.id.data
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        class_ = form.class_.data
        user = db_session.query(Student).filter(Student.student_id == id).first()
        required_phone = db_session.query(Student).filter(Student.student_phone == phone)[:]
        required_email = db_session.query(Student).filter(Student.student_email == email)[:]
        if len(required_phone) > 1:  # 判断是否本人的手机号码
            return '该手机号已被使用'
        elif len(required_email) > 1:
            return '该邮箱已被使用'
        elif len(required_phone) == 1 and user.student_phone != phone:
            return '该手机号已被使用'
        elif len(required_email) == 1 and user.student_email != email:
            return '该邮箱已被使用'
        else:
            user.student_name = name
            user.student_email = email
            user.student_phone = phone
            user.student_class = Class(class_name=class_)
            db_session.commit()
        return "success"
    else:
        errors = form.errors
        error = errors.popitem()[1][0]
        return error


@admin_bp.route('/delete_user/', methods=['POST'])
@login_required
def delete_user():
    if request.method == 'POST':
        uid = request.form['uid']
        admin = db_session.query(Admin).filter(Admin.admin_uuid==uid).first()
        if admin:  # 如果存在该用户
            admin.admin_is_delete = True
            db_session.commit()
            return 'success'
        else:
            return '不存在该用户'


@admin_bp.route('/delete_student/', methods=['POST'])
@login_required
def delete_student():
    if request.method == 'POST':
        id = request.form['id']
        student = db_session.query(Student).filter(Student.student_id==id).first()
        if student:  # 如果存在该用户
            student.student_is_delete = True
            db_session.commit()
            return 'success'

        else:
            return '不存在该用户'


@admin_bp.route('/delete_teacher/', methods=['POST'])
@login_required
def delete_teacher():
    if request.method == 'POST':
        id = request.form['id']
        teacher = db_session.query(Teacher).filter(Teacher.teacher_id==id).first()
        if teacher:  # 如果存在该用户
            teacher.teacher_is_delete = True
            db_session.commit()
            return 'success'
        else:
            return '不存在该用户'

