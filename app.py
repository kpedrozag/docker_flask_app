#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, redirect, url_for
app = Flask(__name__) 


@app.errorhandler(404)
def page_not_found(e):
    return "The URL does not exist."

@app.route("/")
def index():
	return redirect(url_for("about"))

@app.route("/about")
def about():
	return "Kevin Pedroza Goenaga"


@app.route("/<string:op>/<int:a>/<int:b>")
@app.route("/<string:op>/<int:a>/<float:b>")
@app.route("/<string:op>/<float:a>/<int:b>")
@app.route("/<string:op>/<float:a>/<float:b>")
@app.route("/<string:op>/<int:a>/<int:b>/<string:format>")
@app.route("/<string:op>/<int:a>/<float:b>/<string:format>")
@app.route("/<string:op>/<float:a>/<int:b>/<string:format>")
@app.route("/<string:op>/<float:a>/<float:b>/<string:format>")
def op_gen(op,a,b,format='html'):
	if op == "sum":
		if format == 'json':
			return jsonify(a=a, b=b, result=a+b)
		elif format == 'html':
			return "a = "+str(a)+", b = "+str(b)+", result = "+str(a+b)
		else:
			return "ERROR"
	elif op == "divide":
		if b != 0:
			if format == 'json':
				return jsonify(a=a, b=b, result=a/b)
			elif format == 'html':
				return "a = "+str(a)+", b = "+str(b)+", result = "+str(a/b)
			else:
				return "ERROR"
		else:
			if format == 'json':
				return jsonify(message="Error: Division by zero not supported")
			elif format == 'html':
				return "Error: Division by zero not supported"
			else:
				return "ERROR"
	else:
		if format == 'json':
			return jsonify(message="Error in operation")
		elif format == 'html':
			return "Error in operation"
		else:
			return "ERROR"


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
