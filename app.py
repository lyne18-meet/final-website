from flask import Flask,render_template,request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////tmp/test.db'

@app.route('/')
def index():
	return 'Hello world!'

db=SQLAlchemy(app)

class Users(db.Model):
	__tablename__="Users"
	username=db.Column('username',db.Unicode)
	password=db.Column('password'db.Unicode)
db.create_all()

@app.route('/submit_form',methods=['POST'])
def submit_form():
	username = request.form['username']

users = <Users>.query.all()

if __name__ == "__main__":
	app.run()