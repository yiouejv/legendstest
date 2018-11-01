from wtforms import Form, StringField
from wtforms.validators import Email, Length, InputRequired, DataRequired


class LoginForm(Form):
    '''前台登陆验证'''
    email = StringField(validators=[Email(message='请输入正确格式的邮箱'), InputRequired('请输入邮箱')])
    password = StringField(validators=[Length(min=6, max=20, message='请输入正确格式的密码')])
    remember = StringField(validators=[])


class StudentLoginForm(LoginForm):
    pass


class TeacherLoginForm(LoginForm):
    pass


class AddChoiceFrom(Form):
    type = StringField(validators=[])
    content = StringField(validators=[InputRequired(message='请输入题干')])
    option_A = StringField(validators=[InputRequired(message='请输入A选项')])
    option_B = StringField(validators=[InputRequired(message='请输入B选项')])
    option_C = StringField(validators=[InputRequired(message='请输入C选项')])
    option_D = StringField(validators=[InputRequired(message='请输入D选项')])
    result = StringField(validators=[])
    parse = StringField(validators=[InputRequired(message='请输入该题解析')])


class AddShortAnswerForm(Form):
    content = StringField(validators=[InputRequired('请输入题干')])
    result = StringField(validators=[InputRequired('请输入答案')])
    type = StringField(validators=[])


class AddProgramForm(AddShortAnswerForm):
    pass


class PostTestPagerForm(Form):
    '''发布试卷验证表单'''
    id = StringField(validators=[])
    test_time = StringField(validators=[Length(8, 19, message='考试时间不合法'),InputRequired('请输入考试时间')])
    test_class = StringField(validators=[])


class AddTestPagerForm(Form):
    name = StringField(validators=[InputRequired('请输入试卷名称')])