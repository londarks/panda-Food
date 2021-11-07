import flask
from controller.controller import Controller
from flask import Flask,request, jsonify, render_template, redirect, url_for, send_file

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False
Controller = Controller()


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
