from flask_wtf import FlaskForm
from wtforms import HiddenField
from wtforms.fields.core import BooleanField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length

class UserForm( FlaskForm ):
    user_name = HiddenField( "User Name", validators=[ DataRequired() ] )
    email = EmailField( "Email", validators=[ DataRequired() ] )

class LoginForm( FlaskForm ):
    account = StringField( "Account", validators=[ DataRequired(), Length( 1, 64 ) ] ) 
    password = PasswordField( "Password", validators=[ DataRequired() ] )
    remember_me = BooleanField( "Keep me logged in" )