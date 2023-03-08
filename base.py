from flask import Flask
from flask_migrate import Migrate
from utils.config import Configuration
from core.views import core_app as core_blueprint
from task.views import task as task_blueprint
from auth.views import auth as auth_blueprint
from utils.database import db
from utils.login import login

app = Flask(__name__)
app.register_blueprint(core_blueprint)
app.register_blueprint(task_blueprint)
app.register_blueprint(auth_blueprint)

app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)
