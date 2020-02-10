from functools       import wraps
from flask           import request, render_template, redirect, session, g, flash
from werkzeug        import generate_password_hash, check_password_hash
from Database.models import User, Email


def auth_required(view):
	@wraps(view)
	def decorated(*argv, **kwargs):
		if g.user is None:
			return redirect("/login")
		return view(*argv, **kwargs)
	return decorated

def not_auth_required(view):
	@wraps(view)
	def decorated(*argv, **kwargs):
		if g.user :
			return redirect("/")
		return view(*argv, **kwargs)
	return decorated	


def before_request():
	g.user = None
	if session.get('login') and g:
		g.user = User.get_or_none(User.username == session.get('login'))
		if not g.user:
			session.clear()


@not_auth_required
def register():

	if request.method == 'POST':
		username = request.form['username']+"@local.com"
		user = User.get_or_none(User.username == username)
		if not user:
			User.create(
					username=username,
					fullname=request.form['fullname'],
					password=generate_password_hash(request.form['password'])
				)

			session['login'] = username
			return redirect("/")

		flash({'error' : "Email `{}` is already registered".format(user.username)})

	return render_template('register.html')

@not_auth_required
def login():

	if request.method == 'POST':

		user = User.get_or_none(User.username == request.form['username'])

		if user and check_password_hash(user.password, request.form['password']):
			session['login'] = request.form['username']

			return redirect("/")

		flash({'error':'Incorrect Email/Password'})

	return render_template("login.html") 


@auth_required
def logout():
	session.clear()
	return redirect('/')

@auth_required
def index():

	return render_template("index.html", email=Email.select().where(Email.mailto == g.user.username).dicts()) 

@auth_required
def messages(mesage_id):
	
	messages =Email.select().where(Email.id == mesage_id ).first()

	return render_template("message.html",message=messages)
