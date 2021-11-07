import flask
from flask import Blueprint, current_app, request, jsonify, render_template, redirect, url_for, flash, session
from werkzeug.utils import import_string
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


def decodeCart():
    if request.cookies.get('WC_a') != None:
        data = []
        decode = jwt.decode(str(request.cookies.get('WC_a')),key=app.config['SECRET_KEY'], algorithms=['HS256', ])
        for id in decode['ids']:
            i = Productions.query.filter_by(id=id).first()
            data.append({'id': i.id ,'name': i.name,'description': i.description,'cash': i.cash,'image': i.image})
        return data
    return None


@admin.route("/logout/", methods=['GET'])
def logout():
    res = flask.make_response(redirect('/'))
    res.delete_cookie("Ippai-session")
    return res

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

@admin.route("/auth", methods=['POST'])
def auth():
    result = User.query.filter_by(email=request.form['email']).first()
    if result and result.password == Controller._encryption(request.form['password']):
        #payload e-commecer client
        payload = {
        "id": result.id
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
        return redirect(url_for("pages.index"))


@admin.route("/update_user", methods=['POST'])
def update_user():
    #update user infos..
    if request.form['password'] != '':
        acess = cookie()
        decode = jwt.decode(str(acess),key=app.config['SECRET_KEY'], algorithms=['HS256', ])
        result = User.query.filter_by(id=decode['id']).first()
        if result.password == Controller._encryption(request.form['password']):
            for i in request.form:
                if i == 'submit':
                    pass
                else:
                    if request.form[i] != '':
                        if i == 'name':
                            result.name = request.form[i]
                        elif i == 'cpf':
                            result.cpf = request.form[i]
                        elif i == 'email':
                            result.email = request.form[i]
                        elif i == 'phone':
                            result.phone = request.form[i]
                        elif i == 'street':
                            result.street = request.form[i]
                        elif i == 'newpass':
                            result.password = Controller._encryption(request.form[i])
            #update Database             
            db.session.commit()
            flash('alert alert-success')
            return redirect(url_for("admin.dashboard"))
        else:
            flash('alert alert-danger')
            return redirect(url_for("admin.dashboard"))
    else:
        flash('alert alert-danger')
        return redirect(url_for("admin.dashboard"))


#function cart
@admin.route("/cart/<item>", methods=['GET'])
def cart(item):
    if cookie() == None:
        return redirect(url_for("pages.index"))
    else:
        if request.cookies.get('WC_a') == None:
            payload = {
                "ids": [item]
            }
            token = jwt.encode(payload,app.config['SECRET_KEY'],algorithm="HS256")
            res = flask.make_response(redirect('/'))
            res.set_cookie("WC_a", value=token)
            return res
        else:
            shop = []
            decode = jwt.decode(str(request.cookies.get('WC_a')),key=app.config['SECRET_KEY'], algorithms=['HS256', ])
            for id in decode['ids']:
                shop.append(id)
            shop.append(item)
            print(shop)
            payload = {
                "ids": shop
            }
            token = jwt.encode(payload,app.config['SECRET_KEY'],algorithm="HS256")
            res = flask.make_response(redirect('/'))
            res.set_cookie("WC_a", value=token)
            return res