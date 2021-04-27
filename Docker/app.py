#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	html = "<H1>##### П Р И В Е Т  #####</H1>"
	return html

if __name__=="__main__":
	app.run(host="0.0.0.0", port=80)

