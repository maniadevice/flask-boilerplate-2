from flask import render_template, redirect, url_for, request, Blueprint
from flask_login import login_required

from .models import Category
from core.models import Todo
# from . import task
from .forms import TaskForm
from datetime import datetime
from utils.database import db

task = Blueprint('task', __name__, template_folder='templates')


@task.route('/create-task', methods=['GET', 'POST'])
@login_required
def tasks():
    check = None
    todo = Todo.query.all()
    date = datetime.now()
    now = date.strftime("%Y-%m-%d")

    form = TaskForm()
    form.category.choices = [(category.id, category.name) for category in Category.query.all()]

    if request.method == "POST":
        if request.form.get('taskDelete') is not None:
            deleteTask = request.form.get('checkedbox')
            if deleteTask is not None:
                todo = Todo.query.filter_by(id=int(deleteTask)).one()
                db.session.delete(todo)
                db.session.commit()
                return redirect(url_for('task.tasks'))
            else:
                check = 'Please check-box of task to be deleted'

        elif form.validate_on_submit():
            selected = form.category.data
            category = Category.query.get(selected)
            todo = Todo(title=form.title.data, date=form.date.data, time=form.time.data, category=category.name)
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('task.tasks'))

    return render_template('tasks.html', title='Create Tasks', form=form, todo=todo, DateNow=now, check=check)
