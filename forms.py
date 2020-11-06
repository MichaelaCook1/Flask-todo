from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from application.models import Todos


class TodoCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_todos = Todos.query.all()
        for todo in all_todos:
            if todo.task == field.data:
                raise ValidationError(self.message)


class TodoForm(FlaskForm):
    task = StringField('Task',
                validators =[
                    DataRequired(),
                    TodoCheck(message= 'That todo already exists')
                    ]
                )
    submit = SubmitField('Add Todo')


