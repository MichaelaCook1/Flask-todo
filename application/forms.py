from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from application.models import Todos


class CheckIfExists:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        for todo in all_todos:
            if todo.name == field.data:
                raise ValidationError(self.message)


class TodoForm(FlaskForm):
    task= StringField('Task', validators=[
        DataRequired(),
        CheckTodo(message='This Todo already exists')
    ])
    submit = SubmitField('Add Todo')
