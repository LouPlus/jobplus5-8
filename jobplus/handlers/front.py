from flask import Blueprint\
    , render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from simpledu.models import Course

from ..forms import *
import time

front = Blueprint('front', __name__)


@front.route('/')
def index():
    page = request.args.get('page',default=0, type=int)
    courses_pg = Course.query.paginate(
        page=page, per_page=5, error_out=False
    )
    return render_template('index.html', pg=courses_pg)


@front.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('登录成功, 欢迎回来', 'success')
        user = form.who
        login_user(user, form.remember_me.data)
        return redirect(url_for('front.index'))
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
        if user == None:
            flash('注册失败,请联系管理员', 'error')
            return render_template('register.html', form=form)
        flash('注册成功, 请登录', 'success')
        time.sleep(3)
        return redirect(url_for('front.login'))
    return render_template('register.html', form = form)