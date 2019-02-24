
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)     # app is an instance of class Flask
app.config['SECRET_KEY'] = '7f12a1f7152a6858c852428551e29dab'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# routes import app here !
# We cannot import routes at the top of the file, or else we'll get into
# circular imports again, so we should import routes after application initialization

from flaskblog import routes
