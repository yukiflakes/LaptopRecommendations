from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
#updating schema
migrate = Migrate(app, db)
login = LoginManager(app)

from configure import Config
app.config.from_object(Config)
#to avoid circular imports
from laptop import routes,models,errors
login.login_view = 'login'

