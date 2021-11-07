import flask
from flask import Blueprint, current_app, request, jsonify, render_template, redirect, url_for, flash
from flask_jwt_extended import create_access_token, create_refresh_token
from flask import current_app as app

import jwt

from datetime import datetime, date, timedelta

from ..models.model import User, Productions,db
from ..controller.controller import Controller

admin = Blueprint('admin', __name__,
                  template_folder='templates',
                  static_folder='static')

Controller = Controller()

# cookie
def cookie():
    login = request.cookies.get('Ippai-session')
    return login


@admin.route("/register", methods=['POST'])
def register():
    # encryption password
    password = Controller._encryption(request.form['password'])
    us = User(name=request.form['name'],
              created=date.today(),
              email=request.form['email'],
              password=password,
              admin=False)

    db.session.add(us)
    db.session.commit()
    return redirect(url_for("pages.index"))

@admin.route('/product/<name>')
def get_product(name):
    produtos = []
    result = Productions.query.filter_by(category=name)
    for i in result:
        produtos.append({'name': i.name,'description': i.description,'cash': i.cash,'image': i.image})
    return render_template("index.html", cookie=cookie(), items=produtos)

@admin.route("/auth", methods=['POST'])
def auth():
    result = User.query.filter_by(email=request.form['email']).first()
    if result and result.password == Controller._encryption(request.form['password']):
        #payload e-commecer client
        payload = {
        "id": result.id,
        "name": result.name,
        "cpf" : result.cpf,
        "email": result.email,
        "phone": result.phone,
        "street": result.street,
        }
        token = jwt.encode(payload,app.config['SECRET_KEY'],algorithm="HS256")
        #access_token = create_access_token(payload, expires_delta=timedelta(minutes=120)) 
        #print(access_token)
        res = flask.make_response(redirect('/'))
        res.set_cookie("Ippai-session", value=token)
        return res
    else:
        #alert fail login.
        flash('Email ou Senha Estão Incorretos.!')
        return render_template("index.html", cookie=cookie(), items=None)


@admin.route("/update_user", methods=['POST'])
def update_user():
    #update user infos..
    acess = cookie()
    decode = jwt.decode(str(acess),key=app.config['SECRET_KEY'], algorithms=['HS256', ])
