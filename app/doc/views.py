from . import doc
from flask import render_template, url_for
from flask_login import login_required
from app.utils.context import Context
from app.admin.service import CategoryService

@doc.route( "/", methods=["GET"] )
@login_required
def index():
    ctx = Context( "doc" )
    ctx.setBackward( url_for( "web.index" ) )

    service = CategoryService()
    categorys = service.find_all()

    data = {
        "categorys": categorys
    }

    return render_template( "/doc/index.html", ctx=ctx.generate(), data=data )