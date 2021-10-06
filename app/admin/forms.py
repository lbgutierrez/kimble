from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length

class CategoriaForm( FlaskForm ):
    nombre = StringField( "Nombre", validators=[ DataRequired(), Length( 1, 64 ) ] ) 
    descripcion = StringField( "Descripcion", widget=TextArea() )

class SubcategoriaForm( FlaskForm ):
    nombre = StringField( "Nombre", validators=[ DataRequired(), Length( 1, 64 ) ] ) 
    descripcion = StringField( "Descripcion", widget=TextArea(), validators=[ DataRequired(), Length( 1, 64 ) ] )