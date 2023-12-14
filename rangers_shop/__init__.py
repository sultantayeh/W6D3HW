from flask import Flask 
from flask_migrate import Migrate 


#internal imports 
from .blueprints.site.routes import site 
from .blueprints.auth.routes import auth
from .blueprints.catalog.routes import catalog
from config import Config 
from .models import login_manager, db 

#instantiating our Flask app
app = Flask(__name__) #passing in the __name__ variable which just takes the name of the folder we're in
app.config.from_object(Config)


login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in'
login_manager.login_message = "Hey you log in"
login_manager.login_message_category = 'warning'


#we are going to use a decorator to create our first route
# @app.route("/")
# def hello_world():
#     return "<p>Hello World!</p>"


app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(catalog)



db.init_app(app)
Migrate = Migrate(app, db)