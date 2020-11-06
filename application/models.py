from application import db  #imports database 


class Todos(db.Model):        #table declared as class
    id = db.Column(db.Integer, primary_key=True)  #defines id as primary key
    task = db.Column(db.String(30), nullable=False) #defines task as string
    complete = db.Column(db.Boolean, default=False) #defines complete as boolean

