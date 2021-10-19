from . import admin
from app.admin.forms import CategoryForm, SubcategoryForm
from app.admin.service import CategoryService, SubcategoryService, SiteService
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

    form = CategoryForm()

    catservice = CategoryService()
    categorys = catservice.find_all()

    data = {
        "categorys": categorys
    }

    return render_template( "/admin/category/index.html", ctx=ctx.generate(), data=data, form=form )


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


@admin.route( "/category/<cat_alias>/update", methods=["GET", "POST"] )
@login_required
def update_category( cat_alias ):
    ctx = Context( "admin" )
    ctx.setBackward( url_for( "admin.category" ) )

    service = CategoryService()

    form = CategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        alias = form.alias.data
        desc = form.description.data

        service.update( cat_alias, name, alias, desc )

        flash( "Categoría actualizada satisfactoriamente" )
        return redirect( url_for( "admin.category" ) )
    else:
        category = service.find_by_alias( cat_alias )
        form.name.data = category.name
        form.alias.data = category.alias
        form.description.data = category.description

    data = {
        "cat_alias": cat_alias
    }

    return render_template( "/admin/category/update.html", ctx=ctx.generate(), form=form, data=data)


@admin.route( "/category/delete", methods=["POST"] )
@login_required
def delete_category():
    service = CategoryService()

    form = CategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        alias = form.alias.data
        desc = form.description.data

        if service.delete( name, alias, desc ):
            flash( "Categoría " + name + ", eliminada satisfactoriamente" )
        else:
            flash( "No fue posible eliminar la categoría " + name  )
    
    return redirect( url_for( "admin.category" ) )


@admin.route( "/cat-defx/subcategory", methods=["GET"] )
@admin.route( "/cat-<cat_alias>/subcategorys/", methods=["GET"] )
@login_required
def subcategory( cat_alias=None ):
    ctx = Context( "admin" )
    ctx.setBackward( url_for( "admin.index" ) )

    form = SubcategoryForm()

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

    return render_template( "/admin/subcategory/index.html", ctx=ctx.generate(), data=data, form=form )


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


@admin.route( "/cat-<cat_alias>/subcategory/<scat_alias>/update", methods=["GET", "POST"] )
@login_required
def update_subcategory( cat_alias, scat_alias ):
    ctx = Context( "admin" )
    ctx.setBackward( url_for( "admin.subcategory", cat_alias=cat_alias ) )

    service = SubcategoryService()

    form = SubcategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        alias = form.alias.data
        desc = form.description.data

        service.update( scat_alias, name, alias, desc )

        flash( "Subcategoría actualizada satisfactoriamente" )
        return redirect( url_for( "admin.subcategory", cat_alias=cat_alias ) )
    else:
        subcategory = service.find_by_alias( scat_alias )
        form.name.data = subcategory.name
        form.alias.data = subcategory.alias
        form.description.data = subcategory.description

    data = {
        "cat_alias": cat_alias,
        "scat_alias": scat_alias
    }
    
    return render_template( "/admin/subcategory/update.html", ctx=ctx.generate(), form=form, data=data)



@admin.route( "/cat-<cat_alias>/subcategory/delete", methods=["POST"] )
@login_required
def delete_subcategory( cat_alias ):
    service = SubcategoryService()

    form = SubcategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        alias = form.alias.data
        desc = form.description.data

        if service.delete( name, alias, desc ):
            flash( "Subcategoría " + name + ", eliminada satisfactoriamente" )
        else:
            flash( "No fue posible eliminar la subcategoría " + name  )
    
    return redirect( url_for( "admin.subcategory", cat_alias=cat_alias ) )


@admin.route( "/sites", methods=["GET"] )
@login_required
def sites():
    ctx = Context( "admin" )
    ctx.setBackward( url_for( "admin.index" ) )

    siteservice = SiteService()
    sites = siteservice.find_all()

    data = {
        "sites": sites
    }

    return render_template( "/admin/sites/index.html", ctx=ctx.generate(), data=data )
