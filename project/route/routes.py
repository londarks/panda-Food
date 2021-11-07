from flask import Blueprint, current_app, request, jsonify, render_template
from flask import request, render_template, make_response
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_file
import jwt
from datetime import datetime as dt
from flask import current_app as app
#from models.models import db, User

pages = Blueprint('pages', __name__,
                  template_folder='templates',
                  static_folder='static')


# cookie
def cookie():
    login = request.cookies.get('Ippai-session')
    return login

# rotas
@pages.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", cookie=cookie(), items=None)


@pages.route("/admin", methods=['GET'])
def admin():
    return render_template("admin.html")


@pages.route("/login", methods=['GET'])
def login():
    return render_template("login.html")


@pages.route("/forgot", methods=['GET'])
def forgot():
    return render_template("forgot.html")


@pages.route("/singup", methods=['GET'])
def singup():
    return render_template("create.html")


@pages.route("/pedidos", methods=['GET'])
def pedidos():
    return render_template("pedidos.html")


@pages.route("/contact", methods=['GET'])
def contact():
    return render_template("contatos.html")


@pages.route("/dashboard", methods=['GET'])
def dashboard():
    #protect
    if cookie() == None:
        return redirect(url_for("pages.index"))
    else:
        acess = cookie()
        decode = jwt.decode(str(acess),key=app.config['SECRET_KEY'], algorithms=['HS256', ])
        print(decode['name'])
        #return page
        return render_template("dashboard.html", cookie=cookie(), data=decode)