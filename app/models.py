from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Enum
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import db, login_manager
import enum, datetime


class Rol( enum.Enum ):
    admin=0
    ux=1
    webdesigner=2
    developer=3

class User( UserMixin, db.Model ):
    __tablename__ = "auth_users"
    id = db.Column( db.Integer, primary_key=True )
    email = db.Column( db.String(64), unique=True, index=True )
    user_name = db.Column( db.String(64), unique=True, index=True )
    password_hash = db.Column( db.String(128) )
    confirmed = db.Column( db.Boolean, default=False )
    created_date = db.Column( db.DateTime, default=datetime.datetime.now )
    created_by = db.Column( db.Integer, db.ForeignKey( "auth_users.id" ) )
    updated_date = db.Column( db.DateTime, default=datetime.datetime.now )
    updated_by = db.Column( db.Integer, db.ForeignKey( "auth_users.id" ) )
    rol_id = db.Column( Enum( Rol ) )

    @property
    def password( self ):
        raise AttributeError( "Password is not a readable attribute" )

    @password.setter
    def password( self, password ):
        self.password_hash = generate_password_hash( password )

    def verify_password( self, password ):
        return check_password_hash( self.password_hash, password )

    def generate_confirmation_token( self, expiration=3600 ):
        s = Serializer( current_app.config[ "SECRET_KEY" ] )
        return s.dumps( { "confirm": self.id } ).decode( "utf-8" )

    def confirm( self, token ):
        s = Serializer( current_app.config[ "SECRET_KEY" ] )
        try:
            data = s.loads( token.encode( "utf-8" ) )
        except:
            return False

        if data.get( "confirm" ) != self.id:
            return False

        self.confirmed = True
        db.session.add( self )

        return True

class Category( db.Model ):
    __tablename__ = "fntk_category"
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String )
    alias = db.Column( db.String, unique=True, index=True )
    description = db.Column( db.String(250) )
    subcategorys = db.relationship("Subcategory", back_populates="category")
    created_date = db.Column( db.DateTime, default=datetime.datetime.now )
    created_by = db.Column( db.Integer, db.ForeignKey( "auth_users.id" ) )


class Subcategory( db.Model ):
    __tablename__ = "fntk_subcategory"
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String )
    alias = db.Column( db.String, unique=True, index=True )
    description = db.Column( db.String(250) )
    category = db.relationship("Category", back_populates="subcategorys")
    category_id = db.Column( db.Integer, db.ForeignKey( "fntk_category.id" ) )
    created_date = db.Column( db.DateTime, default=datetime.datetime.now )
    created_by = db.Column( db.Integer, db.ForeignKey( "auth_users.id" ) )


@login_manager.user_loader
def load_user( user_id ):
    return User.query.get( int( user_id ) )

class Setup():

    def install( self ):
        self.gen_default_users()

    def gen_default_users( self ):
        user = User()
        user.user_name = "admin"
        user.email = "admin@kimble.org"
        user.confirmed = True
        user.password = "admin"
        user.created_by = None
        db.session.add( user )
        db.session.commit()