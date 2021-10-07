from . import admin
from app.admin.forms import CategoryForm, SubcategoryForm
from app.admin.service import CategoryService, SubCategoryService
from flask import flash, render_template, redirect, url_for
from flask_login import login_required
from app.utils.context import Context


@admin.route( "/", methods=["GET"] )
@login_required
def index():
    ctx = Context( "admin" )
    ctx.setBackward( "web.index" )

    return render_template( "/admin/adm_index.html", ctx=ctx.generate() )


@admin.route( "/category", methods=["GET"] )
@login_required
def category():
    ctx = Context( "admin" )
    ctx.setBackward( "admin.index" )

    catservice = CategoryService()
    categorys = catservice.find_all()

    data = {
        "categorys": categorys
    }

    return render_template( "/admin/category/categorys.html", ctx=ctx.generate(), data=data )


@admin.route( "/category/new", methods=["GET", "POST"] )
@login_required
def new_category():
    ctx = Context( "admin" )
    ctx.setBackward( "admin.category" )

    form = CategoryForm()
    if form.validate_on_submit():

        name = form.name.data
        desc = form.description.data

        service = CategoryService()
        service.save( name, desc )

        flash( "Categoría creada satisfactoriamente" )
        return redirect( url_for( "admin.category" ) )

    return render_template( "/admin/category/new.html", ctx=ctx.generate(), form=form)

def modificar_categoria():
    return "categorias"

def subcategorias():
    return "subcategorias"

def nueva_subcategoria():
    return "categorias"