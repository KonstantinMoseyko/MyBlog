import os
from flask import Flask, render_template
from flask_migrate import Migrate
from dotenv import load_dotenv
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.auth import login_manager, auth_app
from blog.models.database import db
from blog import commands
from blog.security import flask_bcrypt


load_dotenv()

app = Flask(__name__)
migrate = Migrate(app, db, compare_type=True, render_as_batch=True)

@app.route("/")
def index():
    return render_template("index.html")

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")

app.cli.add_command(commands.create_admin)


cfg_name = os.getenv("CONFIG_NAME") or "ProductionConfig"

app.config.from_object(f"blog.config.{cfg_name}")
db.init_app(app)
login_manager.init_app(app)
flask_bcrypt.init_app(app)
