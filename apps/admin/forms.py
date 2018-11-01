from wtforms import Form, StringField, IntegerField, ValidationError
from wtforms.validators import Length, Email, InputRequired, EqualTo, Regexp
from config import session as db_session
from apps.admin.models import Admin
from apps.front.models import Student, Teacher


class LoginForms(Form):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱'), InputRequired('请输入邮箱')])
    password = StringField(validators=[Length(min=6, max=20, message='请输入正确格式的密码')])
    remember = IntegerField(validators=[])


class ResetPwdForms(Form):
    '''修改密码验证表单'''
    oldpwd = StringField(validators=[Length(6, 20, message='密码的长度要在6-20之间'), InputRequired('请输入旧密码')])
    newpwd = StringField(validators=[Length(6, 20, message='密码的长度要在6-20之间'), InputRequired('请输入新密码')])
    newpwd2 = StringField(validators=[EqualTo('newpwd', message='两次输入的密码不一致'), InputRequired('请重复新密码')])


class AddUserForms(Form):
    '''添加用户验证表单'''
    name = StringField(validators=[InputRequired('请输入姓名')])
    phone = StringField(validators=[Regexp("1[358][0-9]{9}", message='输入的手机号码格式不正确')])
    email = StringField(validators=[Email(message='请输入正确格式的邮箱'), InputRequired('请输入邮箱')])
    password = StringField(validators=[Length(6, 20, message='密码的长度要在6-20之间'), InputRequired('请输入密码')])
    password2 = StringField(validators=[EqualTo('password', message='两次输入的密码不一致'), InputRequired('请重复密码')])
    is_super = IntegerField(validators=[])

    def validate_phone(self, field):
        phones = db_session.query(Admin.admin_phone).all()
        if (str(field.data),) in phones:
            raise ValidationError('手机号已经存在')

    def validate_email(self, field):
        emails = db_session.query(Admin.admin_email).all()
        if (str(field.data),) in emails:
            raise ValidationError('该邮箱已经存在')


class AddStudentForm(AddUserForms):
    class_ = StringField(validators=[])  # 所属班级

    def validate_phone(self, field):
        phones = db_session.query(Student.student_phone).all()
        if (str(field.data),) in phones:
            raise ValidationError('手机号已经存在')

    def validate_email(self, field):
        emails = db_session.query(Student.student_email).all()
        if (str(field.data),) in emails:
            raise ValidationError('该邮箱已经存在')


class AddTeacherForm(AddUserForms):
    class_ = StringField(validators=[])  # 所属班级

    def validate_phone(self, field):
        phones = db_session.query(Teacher.teacher_phone).all()
        if (str(field.data),) in phones:
            raise ValidationError('手机号已经存在')

    def validate_email(self, field):
        emails = db_session.query(Teacher.teacher_email).all()
        if (str(field.data),) in emails:
            raise ValidationError('该邮箱已经存在')


class UpdateUserForm(Form):
    uid = StringField(validators=[])
    name = StringField(validators=[InputRequired('请输入姓名')])
    phone = StringField(validators=[Regexp("1[358][0-9]{9}", message='输入的手机号码格式不正确')])
    email = StringField(validators=[Email(message='请输入正确格式的邮箱'), InputRequired('请输入邮箱')])
    is_super = IntegerField(validators=[])


class UpdateTeacherForm(Form):
    id = StringField(validators=[])
    name = StringField(validators=[InputRequired('请输入姓名')])
    phone = StringField(validators=[Regexp("1[358][0-9]{9}", message='输入的手机号码格式不正确')])
    email = StringField(validators=[Email(message='请输入正确格式的邮箱'), InputRequired('请输入邮箱')])
    class_ = StringField(validators=[InputRequired('请输入班级')])

    def validate_class_(self, field):
        classes = field.data
        if len(classes)>10 and ',' not in classes:
            raise ValidationError('多个班级请以英文逗号隔开')
        if '[' not in classes or ']' not in classes:
            raise ValidationError('班级请放在[]里，多个班级以英文逗号隔开')

class UpdateStudentForm(Form):
    id = StringField(validators=[])
    name = StringField(validators=[InputRequired('请输入姓名')])
    phone = StringField(validators=[Regexp("1[358][0-9]{9}", message='输入的手机号码格式不正确')])
    email = StringField(validators=[Email(message='请输入正确格式的邮箱'), InputRequired('请输入邮箱')])
    class_ = StringField(validators=[InputRequired('请输入班级')])