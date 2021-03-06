from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager


db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = "auth.auth_login"

def create_app( config_name ):
    app = Flask( __name__ )
    app.config.from_object( config[ config_name ] )

    config[ config_name ].init_app( app )

    csrf.init_app( app )
    db.init_app( app )
    login_manager.init_app( app )


    from .main import main as main_blueprint
    app.register_blueprint( main_blueprint, url_prefix="/" )

    from .web import web as web_blueprint
    app.register_blueprint( web_blueprint, url_prefix="/web" )

    from .admin import admin as admin_blueprint
    app.register_blueprint( admin_blueprint, url_prefix="/web/admin" )

    from .doc import doc as doc_blueprint
    app.register_blueprint( doc_blueprint, url_prefix="/web/documentation" )

    from .auth import auth as auth_blueprint
    app.register_blueprint( auth_blueprint, url_prefix="/auth" )

    return app