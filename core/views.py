from flask import render_template, Blueprint

core_app = Blueprint('core_app', __name__, template_folder='templates')


@core_app.route("/")
def index():
    greeting: str = "hello ace"
    return render_template("index.html", greet=greeting)
