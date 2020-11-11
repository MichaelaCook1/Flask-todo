from flask import render_template,redirect,url_for #imports functiosn from flask
from application import db, app #imports database and app to file
from application.models import Todos #imports todo table
from application.forms import TodoForm, OrderTodo

@app.route('/', methods=['POST', 'GET']) #assigning function to index page
def index():
    form = OrderTodo()
    totals = {
            "total": Todos.query.count(),
            "total_completed": Todos.query.filter_by(complete=True).count()
            }
    if form.order_with.data == "id":
        todos = Todos.query.order_by(Todos.id.desc()).all()
    elif form.order_with.data =="complete":
        todos = Todos.query.order_by(Todos.complete.desc()).all()
    elif form.order_with.data == "incomplete":
        todos = Todos.query.order_by(Todos.complete).all()
    else:
        todos = Todos.query.all()
        return render_template('index.html', title="Todo List App", todos=todos, form=form, totals=totals)

@app.route('/add', methods=['GET','POST']) #assigning function to add page, producing get and post requests
def add():
    form = TodoForm() #creates form
    if form.validate_on_submit(): #validates post method
        todo = Todos(
                task = form.task.data,
                complete = False
                )
        db.session.add(todo) #adds changes to db
        db.session.commit() #commits changes to db
        return redirect(url_for('index')) #redirects to index
    return render_template('add.html',title="Add a new todo", form=form) #renders template 

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = TodoForm() #creates form
    todo = Todos.query.get(id)
    if form.validate_on_submit():
        todo.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = todo.task
        return render_template('update.html', title='Update your todo',form=form)

@app.route('/complete/<int:id>')
def complete(id):
    todo = Todos.query.get(id) #querys id of latest change
    todo.completed = True # if latest todo is completed
    db.session.commit()
    return(redirect(url_for('index')))


@app.route('/incomplete/<int:id>')
def incomplete(id):
    todo = Todos.query.get(id)
    todo.complete = False
    db.session.commit()
    return(redirect(url_for('index')))


@app.route('/delete/<int:id>')
def delete(id):
    current = Todos.query.get(id)
    db.session.delete(current)
    db.session.commit()
    return(redirect(url_for('index')))




