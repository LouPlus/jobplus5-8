from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField\
    , SubmitField, BooleanField, TextAreaField, ValidationError, HiddenField
from wtforms.validators import Length, Email, EqualTo, Required, Regexp, URL, NumberRange
from jobplus.models import db,User,check_password_hash


class UserForm(FlaskForm):
    nickname = StringField('昵称', validators=[Required(), Length(2,32)])
    pwd = PasswordField('密码', validators=[Required(), Length(8,16)])
    email = StringField('邮箱', validators=[Required(), Email(), Length(4, 32)])
    submit = SubmitField('提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).count() > 0:
            raise ValidationError('该邮箱已经注册')

    def validate_nickname(self, field):
        print('昵称长度是',len(field.data))


class RegisterForm(UserForm):
    nickname = StringField('昵称', validators=[Required(), Length(2, 32)])
    username = StringField('用户名（唯一）', validators=[Required(), Length(4,16)
        , Regexp('^[A-Za-z][A-Za-z0-9_]+$', 0, '用户名只能包含数字字母,并且以字母数字开头')])
    email = StringField('邮箱', validators=[Required(), Email(), Length(4, 32)])
    pwd = PasswordField('密码', validators=[Required(), Length(8, 16)])
    repeat_pwd = PasswordField('再次确认密码', validators=[Required(), Length(8,16),EqualTo('pwd')])
    submit = SubmitField('提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).count() > 0:
            raise ValidationError('该邮箱已经注册')

    def validate_nickname(self, field):
        print('昵称长度是',len(field.data))

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.nickname = self.nickname.data
        user.email = self.email.data
        user.password = self.pwd.data
        db.session.add(user)
        try:
            db.session.commit()
            return user
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

class UpdateUserForm(FlaskForm):
    nickname = StringField('昵称', validators=[Required(), Length(2, 32)])

    email = StringField('邮箱', validators=[Required(), Email(), Length(4, 32)])
    repeat_pwd = PasswordField('再次确认密码', validators=[Required(), Length(8,16),EqualTo('pwd')])
    pwd = PasswordField('密码', validators=[Required(), Length(8, 16)])
    submit = SubmitField('提交')

    # def validate_email(self, field):
    #     if User.query.filter_by(email=field.data).count() > 1:
    #         raise ValidationError('该邮箱已经注册')

    def update_user(self,id):
        user = User.query.filter(User.id == id).first()
        user.nickname = self.nickname.data
        user.email = self.email.data
        user.password = self.pwd.data
        db.session.add(user)
        try:
            db.session.commit()
            return user
        except Exception as e:
            print(e)
            db.session.rollback()
            return None


class LoginForm(FlaskForm):
    email_or_username = StringField('邮箱或用户名', validators=[Required(), Email(), Length(4,32)])
    pwd = PasswordField('密码', validators=[Required(), Length(4,16)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

    def validate_email_or_username(self, field):
        user = User.query.filter((User.email==field.data) | (User.username==field.data)).first()
        if not user:
            return ValidationError('用户名或密码不正确')

    def validate_pwd(self, field):
        user = self.who
        if not user:
            return ValidationError('用户名或密码不正确')
        flag = check_password_hash(user.password, field.data)
        if not flag:
            return ValidationError('用户名或密码不正确')

    @property
    def who(self):
        user = User.query.filter( (User.email == self.email_or_username.data)
           | (User.username == self.email_or_username.data)).first()
        return user

# class CourseForm(FlaskForm):
#     name = StringField('课程名称', validators=[Required(), Length(5, 32)])
#     description = TextAreaField('课程简介', validators=[Required(), Length(20, 256)])
#     image_url = StringField('封面图片地址', validators=[Required(), URL()])
#     author_id = IntegerField('作者ID', validators=[Required(), NumberRange(min=1, message='无效的用户ID')])
#     submit = SubmitField('提交')
#
#     def validate_author_id(self, field):
#         if not User.query.get(self.author_id.data):
#             raise ValidationError('用户不存在')
#
#     def create_course(self):
#         course = Course()
#         self.populate_obj(course)
#         db.session.add(course)
#         db.session.commit()
#         return course
#
#     def update_course(self, course):
#         self.populate_obj(course)
#         db.session.add(course)
#         db.session.commit()
#         return course