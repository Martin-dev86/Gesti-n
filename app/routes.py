from flask import Blueprint, render_template, request

from .models import db, Task

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    sites = {}
    for task in db:
        sites.setdefault(task.site, []).append(task)
    return render_template('index.html', sites=sites)


@bp.route('/assign', methods=['POST'])
def assign():
    task_id = int(request.form['task_id'])
    assigned = request.form['team']
    if 0 <= task_id < len(db):
        db[task_id].assigned_to = assigned
    return ('', 204)
