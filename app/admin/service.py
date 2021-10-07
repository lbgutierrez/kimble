from app import db
from app.models import Category, Subcategory

class CategoryService():

    def save( self, name, description ):
        category = Category()
        category.name = name
        category.description = description
        db.session.add( category )
        db.session.commit()

    def find_all( self ):
        return Category.query.all()

    def find_by_name( self, name ):
        return Category.query.filter_by( name=name ).one_or_none()


class SubCategoryService():

    def find_by_category( self, cat_name ):
        cat_service = CategoryService()
        category = cat_service.find_by_name( cat_name )
        return category.subcategorys
