import datetime
from app.models import User, Rol

class UserService():

    def find_user_account( self, account ):
        user = User()
        user.id = 1
        user.email = "admin@admin.com"
        user.user_name = "admin"
        user.password = "admin"
        user.confirmed = True
        user.created_date = datetime.datetime.now
        user.updated_date = datetime.datetime.now
        user.rol_id = Rol.admin
        return user
