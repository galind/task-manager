from flask import render_template
from app.main import bp
from app.models.task import Task


@bp.route('/')
def index():
    tasks = [t.__dict__ for t in Task.query.all()]
    return render_template('index.html', tasks=tasks)
