from flask import Blueprint, current_app, request, jsonify, render_template,session
from flask import request, render_template, make_response
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_file

import jwt
import ast

from datetime import datetime as dt
from flask import current_app as app

from project.route.admin import cart
from ..models.model import User, Productions,db

pages = Blueprint('pages', __name__,
                  template_folder='templates',
                  static_folder='static')


# cookie
def cookie():
    login = request.cookies.get('panda-session')
    return login


def decodeCart():
    if request.cookies.get('WC_a') != None:
        data = []
        total = 0
        decode = jwt.decode(str(request.cookies.get('WC_a')),key=app.config['SECRET_KEY'], algorithms=['HS256', ])
        for id in decode['ids']:
            First = True
            for a in data:
                if int(a['id']) == int(id):
                    a['cash'] += i.cash
                    a['amount'] += 1
                    total += i.cash
                    First = False
                    break
            if First:
                i = Productions.query.get(id)
                data.append({'id': i.id ,'name': i.name,'description': i.description,'cash': i.cash,'image': i.image, 'amount': 1})
                total += i.cash
        return data, total
    return None,None

# rotas
@pages.route("/", methods=['GET', 'POST'])
def index():
    data = decodeCart()
    print(data[0])
    return render_template("index.html", cookie=cookie(), items=None, cart=data[0], total=data[1])


@pages.route('/product/<name>')
def get_product(name):
    data = decodeCart()
    produtos = []
    result = Productions.query.filter_by(category=name)
    for i in result:
        produtos.append({'id': i.id ,'name': i.name,'description': i.description,'cash': i.cash,'image': i.image})
    return render_template("index.html", cookie=cookie(), items=produtos, cart=data[0], total=data[1])



@pages.route("/dashboard", methods=['GET'])
def dashboard():
    #protect
    if cookie() == None:
        return redirect(url_for("pages.index"))
    else:
        data = decodeCart()
        acess = cookie()
        decode = jwt.decode(str(acess),key=app.config['SECRET_KEY'], algorithms=['HS256', ])
        result = User.query.filter_by(id=decode['id']).first()
        payload = {
            "id": result.id,
            "name": result.name,
            "cpf" : result.cpf,
            "email": result.email,
            "phone": result.phone,
            "street": result.street,
        }
        return render_template("dashboard.html", cookie=cookie(), data=payload, cart=data[0], total=data[1])

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
    return render_template("pedidos.html",cookie=cookie())


@pages.route("/contact", methods=['GET'])
def contact():
    data = decodeCart()
    return render_template("contatos.html", cookie=cookie(), cart=data[0], total=data[1])