from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
from simpledu.decorators import admin_required
from simpledu.models import db,Course, User
from simpledu.forms import CourseForm, UpdateUserForm, RegisterForm

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/courses')
@admin_required
def courses():
    page = request.args.get('page', default=1, type=int)
    pagination = Course.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/courses.html', pg=pagination)


@admin.route('/courses/create', methods=['GET', 'POST'])
@admin_required
def create_course():
    form = CourseForm()
    if form.validate_on_submit():
        form.create_course()
        flash('课程创建成功', 'success')
        return redirect(url_for('admin.courses'))
    return render_template('admin/create_course.html', form=form)


@admin.route('/courses/<int:course_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    form = CourseForm(obj=course)
    if form.validate_on_submit():
        form.update_course(course)
        flash('课程更新成功', 'success')
        return redirect(url_for('admin.courses'))
    return render_template('admin/edit_course.html', form=form, course=course)



@admin.route('/users')
@admin_required
def users():
    page = request.args.get('page', default=1, type=int)
    pagination = User.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/users.html', pg=pagination)

@admin_required
@admin.route('/users/<int:user_id>/update', methods=['GET', 'POST'])
def update_user(user_id):
    # user_id = request.args.get('user_id', type=int)
    print('id是',user_id)
    user = User.query.get(user_id)
    form = UpdateUserForm()
    form.nickname.default = user.nickname
    form.email.default = user.email
    if form.validate_on_submit():
        form.update_user(user_id)
        flash('修改成功', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/edit_user.html',form=form)

@admin.route('/users/delete', methods=['GET', 'POST'])
@admin_required
def delete_user():
    user_id = request.args.get('user_id',type=int)
    user = User.query.get(user_id)
    print('要删除的是:', user)
    if user:
        if user.is_admin:
            flash('管理员账户,无法删除')
            return redirect(url_for('admin.users'))
        User.query.filter_by(id=user_id).delete()
        db.session.commit()
        flash('删除成功')
    return redirect(url_for('admin.users'))

    # return redirect(url_for('admin.users'))


@admin.route('/users/create', methods=['GET','POST'])
def create_user():
    form = RegisterForm()
    if form.validate_on_submit():
        user = form.create_user()
        if user is None:
            flash('注册失败,请联系开发人员', 'error')
            return render_template('register.html', form=form)
        flash('创建成功', 'success')
        return redirect(url_for('admin.users'))
    return render_template('register.html', form = form)
