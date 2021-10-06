from . import web
from flask import render_template
from flask_login import login_required


@web.route( "/" )
@login_required
def index():
    return render_template( "web/index.html" )

@web.route( "/prueba" )
@login_required
def prueba():
    return "prueba"