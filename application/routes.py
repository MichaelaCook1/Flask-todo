from flask import render_template,redirect,url_for #imports functiosn from flask


from application import db,app #imports database and app to file
from application.models import Todos #imports todo table
from application.forms import TodoForm

@app.route('/') #assigning function to index page
def index():
    all_todos = Todos.query.all() #selects all rows in Todos table
    return render_template('index.html',all_todos=all_todos) #returns template into index

@app.route('/add', methods=['GET','POST']) #assigning function to add page, producing get and post requests
def add():
    form = TodoForm() #creates form
        if form.validate_on_submit(): #validates post method
            new_todo = Todos(name=form.task.data)
            db.session.add(todo) #adds changes to db
            db.session.commit() #commits changes to db
            return redirect(url_for('index')) #redirects to index
    return render_template('add.html', form=form) #renders template 

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = TodoForm() #creates form
    latest = Todos.query.get(todo_id)
    if form.validate_on_submit():
        latest.name = form.task.update
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/complete/<int:id>')
def complete(id):
    latest = Todos.query.get(id) #querys id of latest change
    latest.completed = True # if latest todo is completed
    db.session.commit()
    return(redirect(url_for('index')))


@app.route('/incomplete/<int:id>')
def incomplete(id):
    current = Todos.query.get(id)
    current.completed = False
    db.session.commit()
    return(redirect(url_for('index')))


@app.route('/delete/<int:id>')
def delete(id):
    current = Todos.query.get(id)
    db.session.delete(current)
    db.session.commit()
    return(redirect(url_for('index')))




