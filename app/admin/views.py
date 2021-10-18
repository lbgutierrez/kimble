from . import admin
from app.admin.forms import CategoryForm, SubcategoryForm
from app.admin.service import CategoryService, SubcategoryService
from flask import flash, render_template, redirect, url_for
from flask_login import login_required
from app.utils.context import Context


@admin.route( "/", methods=["GET"] )
@login_required
def index():
    ctx = Context( "admin" )
    ctx.setBackward( url_for( "web.index" ) )

    return render_template( "/admin/adm_index.html", ctx=ctx.generate() )


@admin.route( "/category", methods=["GET"] )
@login_required
def category():
    ctx = Context( "admin" )
    ctx.setBackward( url_for( "admin.index" ) )

    catservice = CategoryService()
    categorys = catservice.find_all()

    data = {
        "categorys": categorys
    }

    return render_template( "/admin/category/index.html", ctx=ctx.generate(), data=data )


@admin.route( "/category/new", methods=["GET", "POST"] )
@login_required
def new_category():
    ctx = Context( "admin" )
    ctx.setBackward( url_for( "admin.category" ) )

    form = CategoryForm()
    if form.validate_on_submit():

        name = form.name.data
        alias = form.alias.data
        desc = form.description.data

        service = CategoryService()
        service.save( name, alias, desc )

        flash( "Categoría creada satisfactoriamente" )
        return redirect( url_for( "admin.category" ) )

    return render_template( "/admin/category/new.html", ctx=ctx.generate(), form=form)

def modificar_categoria():
    return "categorias"


@admin.route( "/cat-defx/subcategory", methods=["GET"] )
@admin.route( "/cat-<cat_alias>/subcategorys/", methods=["GET"] )
@login_required
def subcategory( cat_alias=None ):
    ctx = Context( "admin" )
    ctx.setBackward( url_for( "admin.index" ) )

    catservice = CategoryService()
    categorys = catservice.find_all()
    
    subcategorys = []
    if cat_alias != None:
        subcatservice = SubcategoryService()
        subcategorys = subcatservice.find_by_category( cat_alias )

    data = {
        "cat_alias": cat_alias,
        "categorys": categorys,
        "subcategorys": subcategorys
    }

    return render_template( "/admin/subcategory/index.html", ctx=ctx.generate(), data=data )

@admin.route( "/cat-<cat_alias>/subcategorys/new", methods=["GET", "POST"] )
@login_required
def new_subcategory( cat_alias ):
    ctx = Context( "admin" )
    ctx.setBackward( url_for( "admin.subcategory", cat_alias=cat_alias ) )

    data = {
        "cat_alias": cat_alias
    }

    form = SubcategoryForm()
    if form.validate_on_submit():

        name = form.name.data
        alias = form.alias.data
        desc = form.description.data

        service = SubcategoryService()
        service.save( name, alias, desc, cat_alias )

        flash( "Subategoría creada satisfactoriamente" )
        return redirect( url_for( "admin.subcategory", cat_alias=cat_alias ) )

    return render_template( "/admin/subcategory/new.html", ctx=ctx.generate(), form=form, data=data)

