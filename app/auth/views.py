from . import auth
from flask import flash, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import LoginForm
from app import db
from app.auth.services import UserService

@auth.before_app_request
def before_request():
        if current_user.is_authenticated:
            if not current_user.confirmed \
                and request.endpoint \
                and request.blueprint != "auth" \
                and request.endpoint != "static":
                return redirect( url_for( "auth.auth_unconfirmed" ) ) 


@auth.route( "/login", methods=[ "GET", "POST" ] )
def auth_login():
    form = LoginForm()

    if form.validate_on_submit():
        account = form.account.data.lower()
        password = form.password.data

        service = UserService()
        user = service.find_user_account( account )

        if user is not None and user.verify_password( password ):
            print("OK")
            login_user( user, form.remember_me.data )
            next = request.args.get( "next" )

            if next is None or not next.startswith("/"):
                next = url_for( "web.index" )

            return redirect( next )

        flash( "Usuario o contraseña inválida" )

    return render_template("auth/login.html", form=form)

@auth.route( "/logout" )
@login_required
def auth_logout():
        logout_user()

        flash( "Tu sesion se ha cerrado." )

        return redirect( url_for( "web.index" ) )

@auth.route( "/confirm/<token>" )
@login_required
def auth_confirm( token ):
    if current_user.confirmed:
        return redirect( url_for( "web.index" )  )
    
    if current_user.confirm( token ):
        db.session.commit()
        flash( "Tú cuenta ya está confirmada, Gracias!" )
    
    else:
        flash( "El enlace de confirmacion es invalido o ha expirado." )

    return redirect( url_for( "main.index" ) )


@auth.route( "/unconfirmed" )
def auth_unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect( url_for( "web.index" ) )

    return render_template( "auth/unconfirmed.html" )