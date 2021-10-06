from . import admin
from app.admin.forms import CategoriaForm, SubcategoriaForm
from app.admin.service import CategoryService, SubCategoryService
from flask import render_template
from flask_login import login_required

ctx = {
    "activemenu": "admin"
}


@admin.route( "/", methods=["GET"] )
@login_required
def index():
    return render_template( "/admin/adm_index.html", ctx=ctx )


@admin.route( "/categorias", methods=["GET"] )
@login_required
def categorys():
    catservice = CategoryService()
    categorys = catservice.find_all()

    data = {
        "categorys": categorys
    }
    return render_template( "/admin/category/categorys.html", ctx=ctx, data=data )



def nueva_categoria():
    return "categorias"

def modificar_categoria():
    return "categorias"

def subcategorias():
    return "subcategorias"

def nueva_subcategoria():
    return "categorias"