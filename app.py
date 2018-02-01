from flask import Flask,render_template,request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./test.db'

@app.route('/')
def index():
	return render_template("login-pg.html")

db=SQLAlchemy(app)

class Users(db.Model):
	__tablename__="Users"
	id = db.Column(db.Integer, primary_key=True)
	username=db.Column(db.String(30))
	password=db.Column(db.String(30))

	def __init__(self,username,password):
		self.username = username
		self.password = password

db.create_all()

@app.route('/submit_form',methods=['POST'])
def submit_form():
	username = request.form['email']
	password = request.form['psw']
	users = Users.query.filter_by(username=username).first()
	if password == users.password:
		return render_template("home.html")
	else:
		print('password did not match')

@app.route('/signup_form',methods=['POST'])
def signup_form():
	username = request.form['email']
	password = request.form['psw']
	x = Users(username,password)
	db.session.add(x)
	db.session.commit()
	return render_template("home.html")
    
@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/search')
def search():
	return render_template("search.html")

@app.route('/profile')
def profile():
	return render_template("profile.html",users=users)

if __name__ == "__main__":
	app.run()