from flask import Blueprint, render_template
from flask_login import login_required
from jobplus.models import db,Job

job = Blueprint('job', __name__, url_prefix='/jobs')

@job.route('/<int:id>')
@login_required
def course_detail(id):
    course = Job.query.get_or_404(id)
    return render_template('job.html', course=course)

