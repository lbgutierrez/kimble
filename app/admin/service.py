from app import db
from app.models import Category, Subcategory

class CategoryService():

    def save( self, name, alias, description ):
        category = Category()
        category.name = name
        category.alias = alias
        category.description = description
        db.session.add( category )
        db.session.commit()

    def update( self, scat_alias, name, alias, description ):
        category = self.find_by_alias( scat_alias )
        category.name = name
        category.alias = alias
        category.description = description
        db.session.commit()

    def delete( self, name, alias, description ):
        category = Category.query.filter_by( name=name )\
            .filter_by( alias=alias )\
                .filter_by( description=description )\
                    .one_or_none()
        db.session.delete( category )
        db.session.commit()
        
        if category != None:
            return True
        
        return False


    def find_all( self ):
        return Category.query.all()

    def find_by_name( self, name ):
        return Category.query.filter_by( name=name ).one_or_none()

    def find_by_alias( self, alias ):
        return Category.query.filter_by( alias=alias ).one_or_none()


class SubcategoryService():

    def save( self, name, alias, description, cat_alias ):

        cat_service = CategoryService()
        category = cat_service.find_by_alias( cat_alias )

        subcategory = Subcategory()
        subcategory.name = name
        subcategory.alias = alias
        subcategory.description = description
        subcategory.category_id = category.id
        db.session.add( subcategory )
        db.session.commit()

    def update( self, cat_alias, name, alias, description ):
        subcategory = self.find_by_alias( cat_alias )
        subcategory.name = name
        subcategory.alias = alias
        subcategory.description = description
        db.session.commit()

    def delete( self, name, alias, description ):
        subcategory = Subcategory.query.filter_by( name=name )\
            .filter_by( alias=alias )\
                .filter_by( description=description )\
                    .one_or_none()
        db.session.delete( subcategory )
        db.session.commit()
        
        if subcategory != None:
            return True
        
        return False

    def find_by_category( self, cat_name ):
        cat_service = CategoryService()
        category = cat_service.find_by_alias( cat_name )
        return category.subcategorys

    def find_by_alias( self, alias ):
        return Subcategory.query.filter_by( alias=alias ).one_or_none()

class SiteService():

    def find_all( self ):
        return []