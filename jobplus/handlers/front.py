from flask import Blueprint\
    , render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required

from ..forms import *

front = Blueprint('front', __name__)


@front.route('/')
@login_required
def index():
    return render_template('index.html')


@front.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.who
        if user and user.check_password(form.pwd.data):
            login_user(user, form.remember_me.data)
            flash('登录成功, 欢迎回来', 'success')
            return redirect(url_for('front.index'))
        else:
            flash('用户名或者密码不正确','error')
    return render_template('login.html', form=form)

@front.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('front.index'))


@front.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = form.create_user()
        if user :
            flash('注册成功, 请登录', 'success')
            return redirect(url_for('front.login'))
        else:
            flash('注册失败, 请联系管理员', 'error')
    return render_template('register.html', form = form)