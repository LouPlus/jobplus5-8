from flask import Flask, render_template
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from jobplus.config import configs
from jobplus.models import db,  User

def register_blueprints(app):
    from .handlers import front, job, admin, user
    app.register_blueprint(front)
    app.register_blueprint(job)
    app.register_blueprint(admin)
    app.register_blueprint(user)

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    Bootstrap(app)
    login_manager = LoginManager()
    login_manager.login_view = 'front.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app)
    register_blueprints(app)
    return app

