from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length

class CategoryForm( FlaskForm ):
    name = StringField( "Nombre", validators=[ DataRequired(), Length( 1, 64 ) ] ) 
    alias = StringField( "Alias", validators=[ DataRequired(), Length( 1, 20 ) ] )
    description = StringField( "Descripcion", widget=TextArea() )

class SubcategoryForm( FlaskForm ):
    name = StringField( "Nombre", validators=[ DataRequired(), Length( 1, 64 ) ] ) 
    alias = StringField( "Alias", validators=[ DataRequired(), Length( 1, 20 ) ] )
    description = StringField( "Descripcion", widget=TextArea(), validators=[ DataRequired(), Length( 1, 64 ) ] )