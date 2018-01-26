# -*- coding: cp1252 -*-

from bottle import *
import os
@route('/')
def index():
    return '''
          <div>
          <a href='/sida/sida1'>Sida 1</a> </b><a href='/sida/sida2'>Sida 2</a> <a href='/sida/sida3'>Sida 3</a>
          </div>

          <div>
          <a href='/sida/mynd1'><img src='myndir/One.png'>
          <a href='/sida/mynd2'><img src='myndir/Two.png'>
          <a href='/sida/mynd3'><img src='myndir/Three.png'>          
          </div>
          '''

@route('/sida/<id>')
def index(id):
    if id == "sida1":
        return "Her er ", id
    if id == "sida2":
        return "Her er ", id 
    if id == "sida3":
        return "Her er ", id
    if id == "mynd1":
        return "Her er mynd ", id, "<br><img src='myndir/One.png'>"
    if id == "mynd2":
        return "Her er mynd ", id, "<br><img src='myndir/Two.png'>"
    if id == "mynd3":
        return "Her er mynd ", id, "<br><img src='myndir/Three.png'>"


def page():
    l = request.query.nr
    
@route('/gaman')
def index():
    x = request.query.tala
    return "Þetta er gildi breytunnar tala", x

@route('/myndir/<nafn>')
def myndir_static(nafn):
    return static_file(nafn,root='myndir')

@error(404)
def villa(error):
    return "<br><h1>Þessi síða er ekki til</h1>"

run(host="localhost", port=8080);
