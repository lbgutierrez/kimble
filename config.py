import os

basedir = os.path.abspath( os.path.dirname( __file__ ) )

class Config():
    DEBUG = False
    SECRET_KEY = os.environ.get( "SECRET_KEY" ) or "03r2jkg24239urhtjrg924j3rgj249rg"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app( app ):
        pass

class DevelopmentConfig( Config ):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get( "DEV_DATABASE_URI" ) or "sqlite:///" + os.path.join( basedir, "data-dev.sqlite" ) 

class TestConfig( Config ):
    SQLALCHEMY_DATABASE_URI = os.environ.get( "TEST_DATABASE_URI" ) or "sqlite:///" + os.path.join( basedir, "data-test.sqlite" ) 

class ProductionConfig( Config ):
    SQLALCHEMY_DATABASE_URI = os.environ.get( "DATABASE_URI" )

config = {
    "development": DevelopmentConfig,
    "test": TestConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}