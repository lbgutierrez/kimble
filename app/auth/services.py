import datetime
from app.models import User, Rol

class UserService():

    def find_user_account( self, account ):
        return User.query.filter_by( user_name=account ).one_or_none()