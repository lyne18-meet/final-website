from flask import Flask,render_template,request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////tmp/test.db'

@app.route('/')
def index():
	return render_template("login-pg.html")

db=SQLAlchemy(app)

class Users(db.Model):
	__tablename__="Users"
	id = db.Column(db.Integer, primary_key=True)
	username=db.Column('username',db.String)
	password=db.Column('password',db.String)
db.create_all()

@app.route('/submit_form',methods=['POST'])
def submit_form():
	username = request.form['username']

@app.route('/signup_form',methods=['POST'])
def signup_form():
	username = request.form['username']

users = Users.query.all()

if __name__ == "__main__":
	app.run()