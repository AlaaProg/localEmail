from flask import Flask 
# from flask_user import login_required, UserManager, UserMixin

# from flask_jwt_extended import JWTManager #, create_access_token
from Site.views import index, messages, login, logout, register, before_request


# jwt = JWTManager()

def create_app(config):

	app = Flask(__name__)


	app.config.from_object(config)

	# print(dir(app))
	app.before_request(before_request)
	app.add_url_rule("/", view_func=index)
	app.add_url_rule("/login", view_func=login, methods={'POST', 'GET'})
	app.add_url_rule("/logout", view_func=logout)
	app.add_url_rule("/register", view_func=register, methods={'POST', 'GET'})
	app.add_url_rule("/message/<int:mesage_id>", 'message',view_func=messages, methods={'GET'})

	return app 